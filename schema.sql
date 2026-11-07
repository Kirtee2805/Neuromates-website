-- ====================================================================
-- NEURO MATES — PostgreSQL Database Schema
-- Tables: demo_requests, contact_enquiries
-- ====================================================================

-- 1. Demo Requests Table
CREATE TABLE IF NOT EXISTS demo_requests (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    organisation VARCHAR(150),
    role VARCHAR(100),
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(50) NOT NULL,
    product_interest VARCHAR(100),
    contact_method VARCHAR(50),
    message VARCHAR(2000),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    status VARCHAR(20) DEFAULT 'new',
    source VARCHAR(255)
);

-- Index for querying demo requests by status and date
CREATE INDEX IF NOT EXISTS idx_demo_requests_status ON demo_requests(status);
CREATE INDEX IF NOT EXISTS idx_demo_requests_created_at ON demo_requests(created_at DESC);

-- 2. Contact Enquiries Table
CREATE TABLE IF NOT EXISTS contact_enquiries (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(50) NOT NULL,
    organisation VARCHAR(150),
    interest VARCHAR(100),
    message VARCHAR(2000) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    status VARCHAR(20) DEFAULT 'new',
    source VARCHAR(255)
);

-- Index for querying contact enquiries by status and date
CREATE INDEX IF NOT EXISTS idx_contact_enquiries_status ON contact_enquiries(status);
CREATE INDEX IF NOT EXISTS idx_contact_enquiries_created_at ON contact_enquiries(created_at DESC);

