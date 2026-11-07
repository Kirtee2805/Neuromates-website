# NEURO MATES — Master Project Memory & Architecture Reference

> **Persistent In-Project Memory**: This document preserves all reference documents, visual styles, 3D animation requirements, page copy, safety rules, asset registries, and architectural decisions directly within the repository.

---

## 1. Project Overview & Identity
- **Brand Name**: Neuro Mates
- **Tagline**: *Monitor · Detect · Alert · Care*
- **Core Concept**: An AI and IoT-based smart care ecosystem designed to support people living with Parkinson's, Alzheimer's, Epilepsy, and Paralysis. It bridges the gap between clinical appointments through continuous monitoring, personalized rehabilitation, medication/activity support, and connected multi-role portals (Patient, Caretaker, Doctor, Admin).
- **Core Philosophy**: "Advancing connected care for neurological health." Technology designed around care and real human needs beyond the clinic.

---

## 2. 3D Animation & Visual Direction (From Reference Video)
*Reference source: `assets/reference/reference_3d_animation.mp4` / extracted video frames*

### Key 3D Animation Pillars:
1. **Luminous Neural Brain (Hero Scene)**:
   - Translucent, glassmorphic / bioluminescent 3D human brain model (deep violet/indigo cortex with electric cyan and magenta neural impulse pathways firing internally).
   - Smooth mouse-parallax and scroll-driven rotation.
   - Elegant "Scroll to explore" cue with warm, soft-shadow ambient lighting (sage green to warm sand gradient backdrop).

2. **Scroll-Driven Exploded Wearable View (Hardware Showcase)**:
   - Parkinson's & Alzheimer's safety wearable in 3D.
   - Smooth disassembly / exploded projection on scroll: the outer ergonomic casing lifts, exposing the internal micro-circuitry, PCB, sensors, and charging interface.
   - Glowing aura/status pulse indicating active monitoring.

3. **Floating Connected Ecosystem (Software & Portals)**:
   - 3D floating hardware devices: a modern laptop displaying the Patient Portal / BioAmp signal graphs alongside floating smartphones displaying Caretaker & Doctor Portals (with real-time GPS boundary rings and health telemetry).
   - Contextual floating notification cards: dynamic WhatsApp alert simulation sliding into 3D space (`"Neuro Mates Alert: Normal-State Confirmation. Movement patterns returned to normal..."`).

---

## 3. Product Suite & Hardware Mapping
*Extracted image assets stored in `assets/images/`*

| Product | Sensed Signals | Hardware Description | Core Flow | Key Asset Reference |
| :--- | :--- | :--- | :--- | :--- |
| **Parkinson's Care** | Hand tremor, sudden acceleration (falls) | Lightweight ergonomic back-of-hand wearable with adjustable strap, compact casing & status LED | *Sense → Analyze → Alert → Recover → Exercise* | `page_4_*.jpg`, `page_13_*.jpg`, `page_14_*.jpg` |
| **Alzheimer's Care** | Continuous GPS location & safe-zone tracking | Upper-arm / wrist safety wearable with tamper-resistant adjustable strap & status LED | *Track → Record → Remember → Remind → Share* | `page_3_*.jpg`, `page_5_*.jpg`, `page_10_*.jpg`, `page_11_*.jpg` |
| **Epilepsy Care** | Continuous EEG brain signals (Alpha, Beta, Gamma, Delta, Theta) | Comfortable headband with forehead EEG electrodes, behind-ear reference electrode & ESP32/BioAmp | *Monitor → Detect → Alert → Respond → Recover → Resume* | `page_15_*.jpg` |
| **Paralysis Care** | Muscle electrical activity (EMG), facial mimics & movement | Skin surface electrodes, BioAmp EXG sensor modules, interactive PC display | *Move → Play → Exercise* | `page_6_*.jpg` - `page_9_*.jpg`, `page_12_*.jpg` |

---

## 4. Four Connected Portals
All disease-specific devices connect to a single platform with role-based access:
1. **Patient Portal**: Daily activities, condition-specific monitoring, interactive gamified rehabilitation, Alzheimer's memory quizzes, medication & appointment reminders.
2. **Caretaker Portal**: Live emergency alerts (WhatsApp + siren triggers), real-time GPS location with boundary status, daily routine timelines, normal-state confirmations.
3. **Doctor Portal**: Multi-axis sensor telemetry, historical tremor/EEG/EMG logs, progress reports (daily, weekly, monthly), clinical consultation insights.
4. **Admin Portal**: Device configuration, safe-zone geofence radii definition, user-caretaker relationship binding, system operational telemetry.

---

## 5. Strict Content & Safety Rules
- **Epilepsy Wording**: ALWAYS use: *"abnormal EEG signals that may indicate a seizure"*. NEVER claim diagnosis, prediction, prevention, or guaranteed detection.
- **No Fabricated Numbers**: No fake statistics, outcome metrics, recovery percentages, or testimonials.
- **No Made-Up Profiles**: No fake doctor quotes, fake patient testimonials, or mock clinical credentials. Medical advisors are listed strictly as:
  - *Dr. Kirit Shukla — Neuro Physician*
  - *Dr. Nishit Patel — Neuro Physician*
  - *Dr. G. B. Yadav — MS, PhD*
- **Tone**: Empathetic, scientifically grounded, calm, dignified, and editorial.

---

## 6. Open Decisions Tracker
1. **Safe-Zone Radius**: Approved website copy specifies **1 km radius** (older prototype note mentions 200m; keep 1 km as primary standard with caption clarity).
2. **Medical Guidance Heading**: Kept as **"Guided by medical professionals"** (reflecting advisory consultation rather than clinical validation).
3. **Seizure Diary**: Maintained as an elective doctor-review feature.
4. **Form Endpoints**: Contact and Demo requests require target webhook/email handler (e.g., Formspree, Netlify Forms, or custom API).

---

## 7. Existing Codebase & Implementation State
- `Neuro Mates _ Connected neurological care.html`: Complete Home page covering all 11 sections with Three.js WebGL canvas integration, custom typography (`DM Sans` + `Fraunces`), and responsive layout.
- `Products _ Neuro Mates.html`: Comprehensive products showcase covering Overview, Parkinson's, Alzheimer's, Epilepsy, and Paralysis sections with interactive demos (geofence drag demo, memory quiz, fall simulation).
- `assets/images/`: 15 high-resolution UI and product photography assets extracted from the specification PDF.
- `assets/reference/`: Reference video, DOCX content document, and PDF image book preserved.

