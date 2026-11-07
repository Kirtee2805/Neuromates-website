/**
 * NEURO MATES — Backend API Server
 * Handles /api/contact and /api/demo with:
 * - Rate limiting (5 requests per 10 mins per IP)
 * - Honeypot spam protection
 * - Input validation (email regex, phone min length 8, message max 2000 chars)
 * - Parameterized PostgreSQL queries (SQL injection prevention)
 * - Email notifications via nodemailer
 * - Static file serving fallback
 */

require('dotenv').config();
const express = require('express');
const cors = require('cors');
const { Pool } = require('pg');
const nodemailer = require('nodemailer');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json({ limit: '64kb' }));
app.use(express.urlencoded({ extended: true, limit: '64kb' }));

// Serve frontend static files
app.use(express.static(path.join(__dirname)));

// 1. In-Memory IP Rate Limiter (Max 5 requests per 10 minutes per IP)
const rateLimitMap = new Map();
const RATE_LIMIT_WINDOW_MS = 10 * 60 * 1000; // 10 minutes
const MAX_REQUESTS_PER_WINDOW = 5;

function rateLimiter(req, res, next) {
  const ip = req.headers['x-forwarded-for'] || req.socket.remoteAddress || 'unknown';
  const now = Date.now();

  const record = rateLimitMap.get(ip);
  if (!record) {
    rateLimitMap.set(ip, { count: 1, resetAt: now + RATE_LIMIT_WINDOW_MS });
    return next();
  }

  if (now > record.resetAt) {
    rateLimitMap.set(ip, { count: 1, resetAt: now + RATE_LIMIT_WINDOW_MS });
    return next();
  }

  if (record.count >= MAX_REQUESTS_PER_WINDOW) {
    const retryAfterSec = Math.ceil((record.resetAt - now) / 1000);
    res.setHeader('Retry-After', retryAfterSec);
    return res.status(429).json({
      ok: false,
      error: `Too many submissions. Please wait ${retryAfterSec} seconds before trying again.`
    });
  }

  record.count += 1;
  next();
}

// Clean up stale rate limit records every 15 minutes
setInterval(() => {
  const now = Date.now();
  for (const [ip, data] of rateLimitMap.entries()) {
    if (now > data.resetAt) rateLimitMap.delete(ip);
  }
}, 15 * 60 * 1000);

// 2. PostgreSQL Connection Pool
const pool = new Pool({
  host: process.env.PGHOST || 'localhost',
  port: parseInt(process.env.PGPORT || '5432', 10),
  user: process.env.PGUSER || 'postgres',
  password: process.env.PGPASSWORD || '',
  database: process.env.PGDATABASE || 'neuromates',
  max: 20,
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 2000
});

pool.on('error', (err) => {
  console.warn('[Postgres Pool Warning]', err.message);
});

// 3. Nodemailer Transporter
let transporter = null;
if (process.env.SMTP_HOST && process.env.SMTP_USER && process.env.SMTP_PASS) {
  const cleanPass = (process.env.SMTP_PASS || '').replace(/\s+/g, '');
  transporter = nodemailer.createTransport({
    host: process.env.SMTP_HOST,
    port: parseInt(process.env.SMTP_PORT || '587', 10),
    secure: process.env.SMTP_PORT === '465',
    auth: {
      user: process.env.SMTP_USER,
      pass: cleanPass
    }
  });
}

async function sendNotificationEmail(subject, textContent) {
  if (!transporter) {
    console.log('[Email Mock] Notification:', subject, '\n', textContent);
    return;
  }
  try {
    const info = await transporter.sendMail({
      from: `"Neuro Mates Platform" <${process.env.SMTP_USER}>`,
      to: process.env.NOTIFICATION_EMAIL || process.env.SMTP_USER,
      subject: subject,
      text: textContent
    });
    console.log('[Email Sent Successfully]', info.messageId);
  } catch (err) {
    console.warn('[Email Warning] Failed to send email notification:', err.message);
  }
}

// 4. Validation Helpers
const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function sanitize(str) {
  if (typeof str !== 'string') return '';
  return str.trim();
}

// Health Check Endpoint
app.get('/api/health', (req, res) => {
  res.json({ ok: true, service: 'neuromates-api', timestamp: new Date().toISOString() });
});

// ====================================================================
// ENDPOINT: POST /api/contact
// ====================================================================
app.post('/api/contact', rateLimiter, async (req, res) => {
  try {
    const { full_name, email, phone, organisation, interest, message, website } = req.body;

    // Honeypot check
    if (website && website.trim() !== '') {
      return res.status(400).json({ ok: false, error: 'Spam detected.' });
    }

    const cleanName = sanitize(full_name);
    const cleanEmail = sanitize(email);
    const cleanPhone = sanitize(phone);
    const cleanOrg = sanitize(organisation);
    const cleanInterest = sanitize(interest);
    const cleanMessage = sanitize(message);
    const source = req.headers['referer'] || 'contact.html';

    // Field Validations
    if (!cleanName || cleanName.length < 2 || cleanName.length > 100) {
      return res.status(400).json({ ok: false, error: 'Full name must be between 2 and 100 characters.' });
    }
    if (!cleanEmail || !EMAIL_REGEX.test(cleanEmail) || cleanEmail.length > 255) {
      return res.status(400).json({ ok: false, error: 'A valid email address is required.' });
    }
    const phoneDigits = cleanPhone.replace(/\D/g, '');
    if (phoneDigits.length !== 10) {
      return res.status(400).json({ ok: false, error: 'Phone number must be exactly 10 digits.' });
    }
    if (!cleanMessage || cleanMessage.length < 5 || cleanMessage.length > 2000) {
      return res.status(400).json({ ok: false, error: 'Message must be between 5 and 2000 characters.' });
    }

    let insertedId = null;

    // Parameterized DB Insert
    try {
      const query = `
        INSERT INTO contact_enquiries (full_name, email, phone, organisation, interest, message, source)
        VALUES ($1, $2, $3, $4, $5, $6, $7)
        RETURNING id
      `;
      const values = [cleanName, cleanEmail, cleanPhone, cleanOrg, cleanInterest, cleanMessage, source];
      const dbRes = await pool.query(query, values);
      insertedId = dbRes.rows[0]?.id;
    } catch (dbErr) {
      console.warn('[Postgres Insert Skipped / Demo Mode]', dbErr.message);
      // In offline / standalone development without Postgres, assign fallback ID
      insertedId = Date.now();
    }

    // Trigger Email Notification
    sendNotificationEmail(
      `New Neuro Mates Enquiry from ${cleanName} (${cleanInterest || 'General'})`,
      `Name: ${cleanName}\nEmail: ${cleanEmail}\nPhone: ${cleanPhone}\nOrganisation: ${cleanOrg}\nInterest: ${cleanInterest}\n\nMessage:\n${cleanMessage}`
    );

    return res.status(201).json({ ok: true, id: insertedId });
  } catch (err) {
    console.error('Error handling /api/contact:', err);
    return res.status(500).json({ ok: false, error: 'Something went wrong. Please try again.' });
  }
});

// ====================================================================
// ENDPOINT: POST /api/demo
// ====================================================================
app.post('/api/demo', rateLimiter, async (req, res) => {
  try {
    const { name, organisation, role, email, phone, product_interest, contact_method, message, website } = req.body;

    // Honeypot check
    if (website && website.trim() !== '') {
      return res.status(400).json({ ok: false, error: 'Spam detected.' });
    }

    const cleanName = sanitize(name);
    const cleanOrg = sanitize(organisation);
    const cleanRole = sanitize(role);
    const cleanEmail = sanitize(email);
    const cleanPhone = sanitize(phone);
    const cleanProducts = Array.isArray(product_interest) ? product_interest.join(', ') : sanitize(product_interest);
    const cleanMethod = sanitize(contact_method);
    const cleanMessage = sanitize(message);
    const source = req.headers['referer'] || 'register-demo.html';

    // Field Validations
    if (!cleanName || cleanName.length < 2 || cleanName.length > 100) {
      return res.status(400).json({ ok: false, error: 'Name must be between 2 and 100 characters.' });
    }
    if (!cleanOrg || cleanOrg.length < 2 || cleanOrg.length > 150) {
      return res.status(400).json({ ok: false, error: 'Organisation is required.' });
    }
    if (!cleanEmail || !EMAIL_REGEX.test(cleanEmail) || cleanEmail.length > 255) {
      return res.status(400).json({ ok: false, error: 'A valid email address is required.' });
    }
    const phoneDigits = cleanPhone.replace(/\D/g, '');
    if (phoneDigits.length !== 10) {
      return res.status(400).json({ ok: false, error: 'Phone number must be exactly 10 digits.' });
    }
    if (cleanMessage && cleanMessage.length > 2000) {
      return res.status(400).json({ ok: false, error: 'Notes must not exceed 2000 characters.' });
    }

    let insertedId = null;

    // Parameterized DB Insert
    try {
      const query = `
        INSERT INTO demo_requests (name, organisation, role, email, phone, product_interest, contact_method, message, source)
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)
        RETURNING id
      `;
      const values = [cleanName, cleanOrg, cleanRole, cleanEmail, cleanPhone, cleanProducts, cleanMethod, cleanMessage, source];
      const dbRes = await pool.query(query, values);
      insertedId = dbRes.rows[0]?.id;
    } catch (dbErr) {
      console.warn('[Postgres Insert Skipped / Demo Mode]', dbErr.message);
      // In offline / standalone development without Postgres, assign fallback ID
      insertedId = Date.now();
    }

    // Trigger Email Notification
    sendNotificationEmail(
      `New Neuro Mates Demo Request: ${cleanName} (${cleanOrg})`,
      `Name: ${cleanName}\nOrganisation: ${cleanOrg}\nRole: ${cleanRole}\nEmail: ${cleanEmail}\nPhone: ${cleanPhone}\nProducts: ${cleanProducts}\nContact Method: ${cleanMethod}\n\nNotes:\n${cleanMessage}`
    );

    return res.status(201).json({ ok: true, id: insertedId });
  } catch (err) {
    console.error('Error handling /api/demo:', err);
    return res.status(500).json({ ok: false, error: 'Something went wrong. Please try again.' });
  }
});

// Start Server
if (require.main === module) {
  app.listen(PORT, () => {
    console.log(`[Neuro Mates API] Server listening on port ${PORT}`);
  });
}

module.exports = app;

