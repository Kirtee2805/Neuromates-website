# Script to generate a high quality vector SVG diagram for the Connected Care Platform
svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="100%" height="100%" style="display:block;background:radial-gradient(circle at center, #FFFFFF 0%, #F5F9FA 75%, #EAF2F4 100%);border-radius:28px;">
  <defs>
    <!-- Gradients -->
    <linearGradient id="coreGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B7A7C" />
      <stop offset="50%" stop-color="#0E3B43" />
      <stop offset="100%" stop-color="#072328" />
    </linearGradient>

    <linearGradient id="patientGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2F7FE0" />
      <stop offset="100%" stop-color="#19559B" />
    </linearGradient>

    <linearGradient id="caretakerGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF7562" />
      <stop offset="100%" stop-color="#D94330" />
    </linearGradient>

    <linearGradient id="doctorGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7C6CFF" />
      <stop offset="100%" stop-color="#5544DF" />
    </linearGradient>

    <linearGradient id="adminGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2BB58A" />
      <stop offset="100%" stop-color="#177D5D" />
    </linearGradient>

    <filter id="cardShadow" x="-15%" y="-15%" width="130%" height="130%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#0E3B43" flood-opacity="0.10" />
    </filter>

    <filter id="coreGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="14" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Background Decorative Grid & Wave Rings -->
  <g opacity="0.4">
    <circle cx="400" cy="300" r="230" fill="none" stroke="#0B7A7C" stroke-width="1.2" stroke-dasharray="6 6" />
    <circle cx="400" cy="300" r="160" fill="none" stroke="#0B7A7C" stroke-width="1" stroke-dasharray="4 4" opacity="0.6" />
  </g>

  <!-- Dynamic Connecting Data Channels (Spokes) -->
  <!-- Center to Patient (Top) -->
  <path d="M 400 230 L 400 135" stroke="#2F7FE0" stroke-width="3" stroke-linecap="round" stroke-dasharray="6 4" opacity="0.8" />
  <!-- Center to Caretaker (Right) -->
  <path d="M 470 300 L 580 300" stroke="#FF7562" stroke-width="3" stroke-linecap="round" stroke-dasharray="6 4" opacity="0.8" />
  <!-- Center to Doctor (Bottom) -->
  <path d="M 400 370 L 400 465" stroke="#7C6CFF" stroke-width="3" stroke-linecap="round" stroke-dasharray="6 4" opacity="0.8" />
  <!-- Center to Admin (Left) -->
  <path d="M 330 300 L 220 300" stroke="#2BB58A" stroke-width="3" stroke-linecap="round" stroke-dasharray="6 4" opacity="0.8" />

  <!-- Flowing pulse dots -->
  <circle cx="400" cy="180" r="4.5" fill="#2F7FE0" />
  <circle cx="525" cy="300" r="4.5" fill="#FF7562" />
  <circle cx="400" cy="420" r="4.5" fill="#7C6CFF" />
  <circle cx="275" cy="300" r="4.5" fill="#2BB58A" />

  <!-- CENTRAL HUB: Neuro Mates Care Platform -->
  <g transform="translate(400, 300)">
    <!-- Outer Aura -->
    <circle cx="0" cy="0" r="82" fill="#0B7A7C" opacity="0.12" filter="url(#coreGlow)" />
    <!-- Outer Ring -->
    <circle cx="0" cy="0" r="70" fill="url(#coreGrad)" stroke="#7FD6D0" stroke-width="3.5" filter="url(#cardShadow)" />
    <!-- Inner Core Halo -->
    <circle cx="0" cy="0" r="54" fill="none" stroke="rgba(127,214,208,0.4)" stroke-width="1.5" stroke-dasharray="5 3" />
    
    <!-- Central Brain Symbol & Heartbeat -->
    <g transform="translate(-18, -26) scale(0.9)">
      <path d="M20 5C14 5 10 9 10 14C7 15 5 18 5 22C5 27 9 31 14 31C15 36 20 40 26 40C30 40 33 38 35 35C37 38 40 40 44 40C50 40 55 36 56 31C61 31 65 27 65 22C65 18 63 15 60 14C60 9 56 5 50 5C45 5 41 8 39 12C37 10 33 9 30 9C27 9 23 10 21 12C19 8 15 5 20 5Z" fill="none" stroke="#7FD6D0" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M15 22L24 22L28 15L33 28L37 19L41 24L48 22" fill="none" stroke="#5BE7C4" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    </g>

    <!-- Platform Text -->
    <text x="0" y="16" text-anchor="middle" font-family="'DM Sans', system-ui, sans-serif" font-weight="800" font-size="12" fill="#FFFFFF" letter-spacing="1">NEURO MATES</text>
    <text x="0" y="30" text-anchor="middle" font-family="'DM Sans', system-ui, sans-serif" font-weight="600" font-size="9.5" fill="#7FD6D0" letter-spacing="0.5">CARE PLATFORM</text>
  </g>

  <!-- 1. PATIENT PORTAL (TOP) -->
  <g class="diagram-node" id="node-patient" transform="translate(400, 85)" style="cursor:pointer;transition:transform 0.3s ease;">
    <rect x="-115" y="-36" width="230" height="72" rx="20" fill="#FFFFFF" stroke="#2F7FE0" stroke-width="2" filter="url(#cardShadow)" />
    <!-- Avatar Icon Circle -->
    <circle cx="-75" cy="0" r="22" fill="url(#patientGrad)" />
    <path d="M -75 -7 A 5 5 0 1 1 -75 3 A 5 5 0 1 1 -75 -7 M -85 11 C -85 7 -79 5 -75 5 C -71 5 -65 7 -65 11" fill="none" stroke="#FFFFFF" stroke-width="2" stroke-linecap="round" />
    <!-- Node Text -->
    <text x="-42" y="-6" font-family="'DM Sans', system-ui, sans-serif" font-weight="700" font-size="14" fill="#0E3B43">Patient Portal</text>
    <text x="-42" y="12" font-family="'DM Sans', system-ui, sans-serif" font-weight="500" font-size="10" fill="#587377">Vitals · Activities · Memory Recall</text>
    <!-- Badge -->
    <rect x="52" y="-12" width="50" height="20" rx="10" fill="rgba(47,127,224,0.12)" />
    <text x="77" y="2" text-anchor="middle" font-family="'DM Sans', system-ui, sans-serif" font-weight="700" font-size="9" fill="#2F7FE0">ACTIVE</text>
  </g>

  <!-- 2. CARETAKER PORTAL (RIGHT) -->
  <g class="diagram-node" id="node-caretaker" transform="translate(635, 300)" style="cursor:pointer;transition:transform 0.3s ease;">
    <rect x="-105" y="-36" width="210" height="72" rx="20" fill="#FFFFFF" stroke="#FF7562" stroke-width="2" filter="url(#cardShadow)" />
    <!-- Avatar Icon Circle -->
    <circle cx="-68" cy="0" r="22" fill="url(#caretakerGrad)" />
    <path d="M -71 -4 A 4 4 0 1 1 -71 4 A 4 4 0 1 1 -71 -4 M -78 11 C -78 8 -74 6 -71 6 C -68 6 -64 8 -64 11 M -63 -2 A 3.5 3.5 0 1 1 -63 5 M -60 11 C -60 9 -57 7 -54 7 C -51 7 -48 9 -48 11" fill="none" stroke="#FFFFFF" stroke-width="1.8" stroke-linecap="round" />
    <!-- Node Text -->
    <text x="-36" y="-6" font-family="'DM Sans', system-ui, sans-serif" font-weight="700" font-size="14" fill="#0E3B43">Caretaker Portal</text>
    <text x="-36" y="12" font-family="'DM Sans', system-ui, sans-serif" font-weight="500" font-size="10" fill="#587377">Alerts · Geofence · Daily Care</text>
  </g>

  <!-- 3. DOCTOR PORTAL (BOTTOM) -->
  <g class="diagram-node" id="node-doctor" transform="translate(400, 515)" style="cursor:pointer;transition:transform 0.3s ease;">
    <rect x="-115" y="-36" width="230" height="72" rx="20" fill="#FFFFFF" stroke="#7C6CFF" stroke-width="2" filter="url(#cardShadow)" />
    <!-- Avatar Icon Circle -->
    <circle cx="-75" cy="0" r="22" fill="url(#doctorGrad)" />
    <!-- Stethoscope / Cross Icon -->
    <path d="M -75 -8 L -75 8 M -83 0 L -67 0" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" />
    <!-- Node Text -->
    <text x="-42" y="-6" font-family="'DM Sans', system-ui, sans-serif" font-weight="700" font-size="14" fill="#0E3B43">Doctor Portal</text>
    <text x="-42" y="12" font-family="'DM Sans', system-ui, sans-serif" font-weight="500" font-size="10" fill="#587377">Clinical Telemetry · Trends · Reports</text>
  </g>

  <!-- 4. ADMIN PORTAL (LEFT) -->
  <g class="diagram-node" id="node-admin" transform="translate(165, 300)" style="cursor:pointer;transition:transform 0.3s ease;">
    <rect x="-105" y="-36" width="210" height="72" rx="20" fill="#FFFFFF" stroke="#2BB58A" stroke-width="2" filter="url(#cardShadow)" />
    <!-- Avatar Icon Circle -->
    <circle cx="-68" cy="0" r="22" fill="url(#adminGrad)" />
    <!-- Gear / Config Icon -->
    <circle cx="-68" cy="0" r="6" fill="none" stroke="#FFFFFF" stroke-width="2.5" />
    <path d="M -68 -11 L -68 -8 M -68 8 L -68 11 M -79 0 L -76 0 M -60 0 L -57 0 M -76 -8 L -74 -6 M -62 6 L -60 8 M -76 8 L -74 6 M -62 -6 L -60 -8" stroke="#FFFFFF" stroke-width="2.5" stroke-linecap="round" />
    <!-- Node Text -->
    <text x="-36" y="-6" font-family="'DM Sans', system-ui, sans-serif" font-weight="700" font-size="14" fill="#0E3B43">Admin Portal</text>
    <text x="-36" y="12" font-family="'DM Sans', system-ui, sans-serif" font-weight="500" font-size="10" fill="#587377">Devices · Safe Zones · Fleet</text>
  </g>
</svg>"""

with open(r"D:\Neuromates(website)\assets\images\connected-care-diagram.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)
print("Saved assets/images/connected-care-diagram.svg successfully.")

