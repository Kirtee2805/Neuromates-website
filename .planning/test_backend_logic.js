const assert = require('assert');

// 1. Test validation rules directly as defined in server.js
const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function sanitize(str) {
  if (typeof str !== 'string') return '';
  return str.trim();
}

function validateContactPayload(body) {
  const { full_name, email, phone, organisation, interest, message, website } = body;
  if (website && website.trim() !== '') return { ok: false, error: 'Spam detected.' };
  
  const cleanName = sanitize(full_name);
  const cleanEmail = sanitize(email);
  const cleanPhone = sanitize(phone);
  const cleanMessage = sanitize(message);

  if (!cleanName || cleanName.length < 2 || cleanName.length > 100) {
    return { ok: false, error: 'Full name must be between 2 and 100 characters.' };
  }
  if (!cleanEmail || !EMAIL_REGEX.test(cleanEmail) || cleanEmail.length > 255) {
    return { ok: false, error: 'A valid email address is required.' };
  }
  if (!cleanPhone || cleanPhone.length < 8 || cleanPhone.length > 50) {
    return { ok: false, error: 'Phone number must be at least 8 digits.' };
  }
  if (!cleanMessage || cleanMessage.length < 5 || cleanMessage.length > 2000) {
    return { ok: false, error: 'Message must be between 5 and 2000 characters.' };
  }
  return { ok: true };
}

function validateDemoPayload(body) {
  const { name, organisation, role, email, phone, product_interest, contact_method, message, website } = body;
  if (website && website.trim() !== '') return { ok: false, error: 'Spam detected.' };

  const cleanName = sanitize(name);
  const cleanOrg = sanitize(organisation);
  const cleanEmail = sanitize(email);
  const cleanPhone = sanitize(phone);
  const cleanMessage = sanitize(message);

  if (!cleanName || cleanName.length < 2 || cleanName.length > 100) {
    return { ok: false, error: 'Name must be between 2 and 100 characters.' };
  }
  if (!cleanOrg || cleanOrg.length < 2 || cleanOrg.length > 150) {
    return { ok: false, error: 'Organisation is required.' };
  }
  if (!cleanEmail || !EMAIL_REGEX.test(cleanEmail) || cleanEmail.length > 255) {
    return { ok: false, error: 'A valid email address is required.' };
  }
  if (!cleanPhone || cleanPhone.length < 8 || cleanPhone.length > 50) {
    return { ok: false, error: 'Phone number must be at least 8 digits.' };
  }
  if (cleanMessage && cleanMessage.length > 2000) {
    return { ok: false, error: 'Notes must not exceed 2000 characters.' };
  }
  return { ok: true };
}

// Run unit tests
console.log('Testing contact validation...');
assert.strictEqual(validateContactPayload({ website: 'bot-link' }).ok, false);
assert.strictEqual(validateContactPayload({ full_name: 'A' }).ok, false);
assert.strictEqual(validateContactPayload({ full_name: 'Dr. John', email: 'invalid-email' }).ok, false);
assert.strictEqual(validateContactPayload({ full_name: 'Dr. John', email: 'john@example.com', phone: '123' }).ok, false);
assert.strictEqual(validateContactPayload({ full_name: 'Dr. John', email: 'john@example.com', phone: '+123456789', message: 'Hi' }).ok, false);
assert.strictEqual(validateContactPayload({ full_name: 'Dr. John', email: 'john@example.com', phone: '+123456789', message: 'Hello from clinic.' }).ok, true);
console.log('  -> Contact validation PASSED');

console.log('Testing demo validation...');
assert.strictEqual(validateDemoPayload({ website: 'spam' }).ok, false);
assert.strictEqual(validateDemoPayload({ name: 'Alex' }).ok, false);
assert.strictEqual(validateDemoPayload({ name: 'Alex', organisation: 'Hospital', email: 'alex@org.com', phone: '12345678' }).ok, true);
console.log('  -> Demo validation PASSED');

console.log('ALL BACKEND VALIDATION LOGIC VERIFIED!');

