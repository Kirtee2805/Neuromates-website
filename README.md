# Neuro Mates — Connected Neurological Care Platform

> Advancing connected care for neurological health — bridging the gap between clinical appointments through continuous monitoring, personalized rehabilitation, medication/activity support, and connected multi-role portals.

---

## 1. Multi-Page Site Architecture

The Neuro Mates website is built as an independent multi-page architecture without front-end build steps or monolithic SPA routing:

- **Home**: [`index.html`](./index.html) (`neuromates-home.html`)
- **Products**: [`neuromates-products.html`](./neuromates-products.html) (`products.html`, 5 views: Overview, Parkinson's, Alzheimer's, Epilepsy, Paralysis)
- **Technology**:
  - [`technology/index.html`](./technology/index.html) — 4-Layer 3D Stack (Sensing, Connectivity, Intelligence, Platform)
  - [`technology/connected-devices.html`](./technology/connected-devices.html) — 4 Rotating 3D Devices & 1 km Safe-Zone Geofence Simulator
  - [`technology/ai-machine-learning.html`](./technology/ai-machine-learning.html) — Neural Particle Canvas & 4 Live Signal Visualizers
  - [`technology/monitoring-analytics.html`](./technology/monitoring-analytics.html) — Flow Strip & 3 Self-Drawing Editorial Signal Charts
  - [`technology/connected-care-platform.html`](./technology/connected-care-platform.html) — 3D Hub-and-Spoke Ecosystem & 4 Interactive Portals
- **Insights**:
  - [`insights/index.html`](./insights/index.html) — Editorial Overview & Ambient Canvas Dual Wave
  - [`insights/research.html`](./insights/research.html) — 5 Scientific Literature Citations & Research Disclaimer
  - [`insights/resources.html`](./insights/resources.html) — Signal Wave & Editorial Resources Directory
- **About Us**:
  - [`about/index.html`](./about/index.html) — Ken Burns 3-Photo Collage, 2D Canvas Relationship Diagram, Medical Advisory List
  - [`about/vision-mission.html`](./about/vision-mission.html) — Pinned Dual Manifesto Quotes with Three.js 460-Point Cloud
  - [`about/our-approach.html`](./about/our-approach.html) — Kinetic Typography Letter-Spacing Tweens & Expanding Pills
  - [`about/impact.html`](./about/impact.html) — Focus-Scale Words (MONITOR, ALERT, CONNECT, SUPPORT) with 4 Live 2D Canvas Visuals
- **Contact & Demo**:
  - [`contact.html`](./contact.html) — Staggered Form Entrance, Chip Selectors, Rate Limiter, Self-Drawing Checkmark
  - [`register-demo.html`](./register-demo.html) — Split Layout with 3D Orbiting Core & Glass Demo Booking Form
  - [`404.html`](./404.html) — Minimal Editorial Error Page with 2D Canvas Flat-Line Blip Monitor

---

## 2. Database & Backend Setup (PostgreSQL + Express)

### Prerequisites
- Node.js >= 18
- PostgreSQL 14+ (optional for local static preview, required for production DB persistence)

### Database Installation
1. Create a PostgreSQL database:
   ```sql
   CREATE DATABASE neuromates;
   ```
2. Run the database schema:
   ```bash
   psql -U postgres -d neuromates -f schema.sql
   ```
   This creates the `demo_requests` and `contact_enquiries` tables along with status and timestamp indexes.

### Environment Configuration
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
Fill in your database and SMTP credentials:
```env
PORT=3000
PGHOST=localhost
PGPORT=5432
PGUSER=postgres
PGPASSWORD=your_secure_password
PGDATABASE=neuromates
SMTP_HOST=smtp.example.com
SMTP_PORT=587
SMTP_USER=notifications@neuromates.example.com
SMTP_PASS=your_smtp_password
NOTIFICATION_EMAIL=clinical-team@neuromates.example.com
```

### Running the API Server
```bash
npm install
npm start
```
The server will run on `http://localhost:3000` handling:
- `POST /api/contact` — Full name, email, phone, organisation, interest, message, honeypot rejection.
- `POST /api/demo` — Name, organisation, role, email, phone, product interest, contact method, notes.
- In-memory rate limiting: 5 submissions per 10 minutes per IP.
- Parameterized SQL queries prevent SQL injection.
- Email dispatch via nodemailer.

> [!IMPORTANT]
> **Privacy Policy Requirement**: A comprehensive Privacy Policy and Terms of Use covering data storage, consent, and patient information protection must be deployed before publicly accepting real user data.

---

## 3. Strict Safety & Content Contracts
1. **Epilepsy Wording**: Strictly restricted to *"abnormal EEG signals that may indicate a seizure"*. Never claim diagnosis, prediction, prevention, or guaranteed detection.
2. **Hardware Component Names**: Strictly described by function (*motion sensor, brain-signal sensor, location tracker, muscle-signal sensor*). No chip or component part numbers.
3. **No Fabricated Statistics or Testimonials**: Only qualitative impact statements. Every chart and interactive demo carries the label *"Illustration, not real patient data"*.
4. **Medical Advisors**: Listed strictly as advisors (*Dr. Kirit Shukla — Neuro Physician*, *Dr. Nishit Patel — Neuro Physician*, *Dr. G. B. Yadav — MS, PhD*) without unverified quotes or biographies.

