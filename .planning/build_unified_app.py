# Build master index.html with single-URL SPA router and authentic photography
import os

html_content = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
  <title>Neuro Mates | Connected Neurological Care</title>
  <link rel="stylesheet" href="assets/css/tokens.css">
  <link rel="stylesheet" href="assets/css/spa-views.css">
  <style>
    /* Specific interactive styling */
    .hero-home {
      padding: clamp(130px, 16vw, 190px) 0 clamp(64px, 8vw, 100px);
      background: radial-gradient(circle at 75% 30%, rgba(127,214,208,0.2) 0%, rgba(246,244,238,0) 60%);
      position: relative;
    }
    .condition-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-top: 36px;
    }
    .cond-pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 18px;
      border-radius: 99px;
      background: #FFFFFF;
      border: 1px solid rgba(14,59,67,0.1);
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--ink);
      box-shadow: 0 4px 14px rgba(14,59,67,0.04);
      transition: all 0.25s var(--sp);
      cursor: pointer;
    }
    .cond-pill:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(14,59,67,0.1);
      border-color: var(--te);
      color: var(--te);
    }
    .cond-pill::before {
      content: "";
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--pill-color, var(--te));
    }

    /* Problem words pinned section */
    .problem-words-strip {
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
      margin-top: 32px;
    }
    .problem-word {
      font-family: var(--fd);
      font-size: clamp(1.4rem, 2.8vw, 2.2rem);
      font-weight: 700;
      color: var(--te);
      padding: 10px 22px;
      border-radius: 20px;
      background: rgba(11,122,124,0.06);
      border: 1px solid rgba(11,122,124,0.12);
    }

    /* Product Grid */
    .product-showcase-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 32px;
      margin-top: 48px;
    }
    .product-card {
      background: #FFFFFF;
      border: 1px solid rgba(14,59,67,0.08);
      border-radius: 28px;
      overflow: hidden;
      box-shadow: 0 16px 40px rgba(14,59,67,0.05);
      transition: transform 0.35s var(--sp), box-shadow 0.35s;
      display: flex;
      flex-direction: column;
    }
    .product-card:hover {
      transform: translateY(-6px);
      box-shadow: 0 24px 50px rgba(14,59,67,0.12);
    }
    .product-card-img {
      width: 100%;
      height: 280px;
      object-fit: cover;
      display: block;
      background: #EDF7F5;
    }
    .product-card-body {
      padding: 32px 30px;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }
    .product-flow-tag {
      font-size: 0.76rem;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--mu);
      margin-bottom: 12px;
    }

    /* Role Switcher */
    .role-switcher {
      margin-top: 48px;
      background: #FFFFFF;
      border-radius: 28px;
      border: 1px solid rgba(14,59,67,0.08);
      padding: clamp(24px, 4vw, 40px);
      box-shadow: 0 16px 40px rgba(14,59,67,0.06);
    }
    .role-tabs {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      border-bottom: 1px solid rgba(14,59,67,0.08);
      padding-bottom: 20px;
      margin-bottom: 32px;
    }
    .role-tab-btn {
      padding: 10px 22px;
      border-radius: 99px;
      font-family: var(--fb);
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--mu);
      background: rgba(14,59,67,0.04);
      transition: all 0.2s;
    }
    .role-tab-btn.active {
      background: var(--te);
      color: #FFFFFF;
      box-shadow: 0 6px 18px rgba(11,122,124,0.25);
    }
    .role-content-grid {
      display: grid;
      grid-template-columns: 1fr 1.2fr;
      gap: 36px;
      align-items: center;
    }

    /* Step line */
    .steps-timeline {
      display: flex;
      flex-direction: column;
      gap: 24px;
      margin-top: 48px;
      position: relative;
      border-left: 3px solid rgba(11,122,124,0.2);
      padding-left: 32px;
      margin-left: 12px;
    }
    .step-item {
      position: relative;
    }
    .step-item::before {
      content: "";
      position: absolute;
      left: -40px;
      top: 6px;
      width: 15px;
      height: 15px;
      border-radius: 50%;
      background: var(--te);
      box-shadow: 0 0 0 4px #FFFFFF, 0 0 0 6px var(--te);
    }
    .step-num {
      font-size: 0.8rem;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: var(--te);
    }
    .step-title {
      font-family: var(--fd);
      font-size: 1.35rem;
      font-weight: 700;
      color: var(--ink);
      margin: 4px 0 6px;
    }

    /* Forms */
    .form-card {
      background: #FFFFFF;
      border-radius: 32px;
      padding: clamp(32px, 5vw, 54px);
      box-shadow: 0 20px 50px rgba(14,59,67,0.08);
      border: 1px solid rgba(14,59,67,0.08);
      max-width: 680px;
      margin: 40px auto 0;
    }
    .form-group {
      margin-bottom: 22px;
    }
    .form-group label {
      display: block;
      font-weight: 700;
      font-size: 0.92rem;
      color: var(--ink);
      margin-bottom: 8px;
    }
    .form-input, .form-textarea, .form-select {
      width: 100%;
      padding: 14px 18px;
      border-radius: 14px;
      border: 1px solid rgba(14,59,67,0.16);
      background: var(--bg);
      font-family: var(--fb);
      font-size: 1rem;
      color: var(--ink);
      transition: border-color 0.2s, box-shadow 0.2s;
    }
    .form-input:focus, .form-textarea:focus, .form-select:focus {
      border-color: var(--te);
      box-shadow: 0 0 0 4px rgba(11,122,124,0.14);
      background: #FFFFFF;
    }
    .chips-group {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 6px;
    }
    .chip-item {
      padding: 8px 16px;
      border-radius: 99px;
      font-size: 0.85rem;
      font-weight: 600;
      border: 1px solid rgba(14,59,67,0.15);
      background: var(--bg);
      cursor: pointer;
      transition: all 0.2s;
    }
    .chip-item.selected {
      background: var(--te);
      color: #FFFFFF;
      border-color: var(--te);
    }

    /* Video frame */
    .video-wrapper {
      position: relative;
      width: 100%;
      aspect-ratio: 16 / 9;
      border-radius: 28px;
      overflow: hidden;
      box-shadow: 0 24px 60px rgba(14,59,67,0.16);
      margin-top: 36px;
      background: #000;
    }
    .video-wrapper iframe {
      width: 100%;
      height: 100%;
      border: none;
    }

    @media(max-width: 900px) {
      .product-showcase-grid,
      .role-content-grid {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>
  <div id="care"></div>

  <!-- Shared Global Sticky Navbar -->
  <nav id="nav">
    <a class="lg" href="#home" aria-label="Neuro Mates Home">
      <img src="assets/images/logo.png" alt="Neuro Mates">
    </a>
    <button id="mb" aria-label="Toggle menu">Menu</button>
    <ul>
      <li class="dd">
        <a href="#products">Products</a>
        <div>
          <a href="#products">Products Overview</a>
          <a href="#parkinsons-care">Parkinson’s Care</a>
          <a href="#alzheimers-care">Alzheimer’s Care</a>
          <a href="#epilepsy-care">Epilepsy Care</a>
          <a href="#paralysis-care">Paralysis Care</a>
        </div>
      </li>
      <li class="dd">
        <a href="#technology">Technology</a>
        <div>
          <a href="#technology">Technology Overview</a>
          <a href="#connected-devices">Connected Devices</a>
          <a href="#ai-machine-learning">AI &amp; Machine Learning</a>
          <a href="#monitoring-analytics">Monitoring &amp; Analytics</a>
          <a href="#connected-care-platform">Connected Care Platform</a>
        </div>
      </li>
      <li class="dd">
        <a href="#insights">Insights</a>
        <div>
          <a href="#insights">Insights Overview</a>
          <a href="#research">Research</a>
          <a href="#articles">Articles</a>
          <a href="#case-studies">Case Studies</a>
          <a href="#resources">Resources</a>
        </div>
      </li>
      <li class="dd">
        <a href="#about">About Us</a>
        <div>
          <a href="#about">About Neuro Mates</a>
          <a href="#vision-mission">Vision &amp; Mission</a>
          <a href="#our-approach">Our Approach</a>
          <a href="#impact">Impact</a>
        </div>
      </li>
      <li><a href="#contact">Contact Us</a></li>
      <li><a class="btn" href="#register-demo">Register for a Demo</a></li>
    </ul>
  </nav>

  <main id="spa-container">
    <!-- ========================================== -->
    <!-- VIEW: HOME (#home)                         -->
    <!-- ========================================== -->
    <div class="page-view active" id="view-home">
      <!-- 1.1 Hero -->
      <section class="hero-home">
        <div class="w">
          <span class="ey">CONNECTED NEUROLOGICAL CARE</span>
          <h1>Advancing connected care for <em>neurological health</em>.</h1>
          <p class="lead">Neuro Mates is an AI and IoT-based smart care system designed to support people living with Parkinson’s, Alzheimer’s, Epilepsy and Paralysis through continuous monitoring, personalised rehabilitation, medication and activity support, and connected care for patients, caretakers and doctors.</p>
          <div class="bt-group">
            <a class="btn" href="#products">Explore our products &rarr;</a>
            <a class="b2" href="#register-demo">Register for a demo &rarr;</a>
          </div>
          <!-- Condition Quick Previews -->
          <div class="condition-pills">
            <a class="cond-pill" style="--pill-color:#2F7FE0;" href="#parkinsons-care">Parkinson’s Care</a>
            <a class="cond-pill" style="--pill-color:#7C6CFF;" href="#alzheimers-care">Alzheimer’s Care</a>
            <a class="cond-pill" style="--pill-color:#2BB58A;" href="#epilepsy-care">Epilepsy Care</a>
            <a class="cond-pill" style="--pill-color:#F5A623;" href="#paralysis-care">Paralysis Care</a>
          </div>
        </div>
      </section>

      <!-- 1.2 Introduction -->
      <section style="background:#FFFFFF;border-top:1px solid rgba(14,59,67,0.06);border-bottom:1px solid rgba(14,59,67,0.06);">
        <div class="w">
          <span class="ey">BEYOND THE CLINIC</span>
          <h2>Neurological care extends beyond the clinic.</h2>
          <p class="body-text" style="font-size:1.15rem;max-width:56ch;margin-top:20px;">
            Patients living with neurological conditions may require support long after a clinical appointment ends. Monitoring daily activities, remembering medication, maintaining rehabilitation routines, responding to emergencies and keeping doctors informed can place a significant burden on patients and their families.
          </p>
          <p class="body-text" style="font-size:1.15rem;max-width:56ch;">
            Neuro Mates brings these elements together through a connected care platform designed to support patients, caretakers and doctors throughout the care journey.
          </p>
          <!-- Six Problem Words -->
          <div class="problem-words-strip">
            <span class="problem-word">Continuous monitoring</span>
            <span class="problem-word">Falls</span>
            <span class="problem-word">Seizures</span>
            <span class="problem-word">Missed medicines</span>
            <span class="problem-word">Getting lost</span>
            <span class="problem-word">Rehabilitation</span>
          </div>
        </div>
      </section>

      <!-- 1.3 Our Products -->
      <section>
        <div class="w">
          <span class="ey">DISEASE-SPECIFIC SYSTEMS</span>
          <h2>Four products. One connected approach to neurological care.</h2>
          <p class="lead">Neuro Mates develops disease-specific care solutions that combine connected devices, monitoring, intelligent software and personalised support.</p>

          <div class="product-showcase-grid">
            <!-- Parkinson's -->
            <div class="product-card">
              <img class="product-card-img" src="assets/images/parkinsons-wearable.jpg" alt="Parkinson's Wearable">
              <div class="product-card-body">
                <div class="product-flow-tag" style="color:var(--parkinsons-1);">Flow: Sense &bull; Analyze &bull; Alert &bull; Recover &bull; Exercise</div>
                <h3 style="color:var(--ink);">Parkinson’s Care</h3>
                <p class="body-text">Movement monitoring and interactive rehabilitation. Designed to support movement monitoring and interactive rehabilitation through movement-based activities and exercise.</p>
                <div style="margin-top:auto;padding-top:20px;">
                  <a class="btn" href="#parkinsons-care">Explore &rarr;</a>
                </div>
              </div>
            </div>

            <!-- Alzheimer's -->
            <div class="product-card">
              <img class="product-card-img" src="assets/images/alzheimers-wearable.jpg" alt="Alzheimer's Patient Safety Wearable">
              <div class="product-card-body">
                <div class="product-flow-tag" style="color:var(--alzheimers-1);">Flow: Track &bull; Record &bull; Remember &bull; Remind &bull; Share</div>
                <h3 style="color:var(--ink);">Alzheimer’s Care</h3>
                <p class="body-text">Memory support and patient safety. Supports daily activity tracking, personalised memory-recall activities, medication reminders and location-based safety monitoring.</p>
                <div style="margin-top:auto;padding-top:20px;">
                  <a class="btn" href="#alzheimers-care">Explore &rarr;</a>
                </div>
              </div>
            </div>

            <!-- Epilepsy -->
            <div class="product-card">
              <img class="product-card-img" src="assets/images/epilepsy-headband.jpg" alt="Epilepsy Monitoring Wearable Headband">
              <div class="product-card-body">
                <div class="product-flow-tag" style="color:var(--epilepsy-1);">Flow: Monitor &bull; Detect &bull; Alert &bull; Respond &bull; Recover &bull; Resume</div>
                <h3 style="color:var(--ink);">Epilepsy Care</h3>
                <p class="body-text">Continuous brain-activity monitoring and connected response. Continuously monitors brain activity and connects abnormal EEG activity with family alerts, emergency response and continued monitoring.</p>
                <div style="margin-top:auto;padding-top:20px;">
                  <a class="btn" href="#epilepsy-care">Explore &rarr;</a>
                </div>
              </div>
            </div>

            <!-- Paralysis -->
            <div class="product-card">
              <img class="product-card-img" src="assets/images/rehab-platform.jpg" alt="Interactive Physiotherapy Platform">
              <div class="product-card-body">
                <div class="product-flow-tag" style="color:var(--paralysis-1);">Flow: Move &bull; Play &bull; Exercise</div>
                <h3 style="color:var(--ink);">Paralysis Care</h3>
                <p class="body-text">Interactive rehabilitation and recovery support. Uses interactive exercises and movement-based activities to make rehabilitation more engaging and support regular exercise.</p>
                <div style="margin-top:auto;padding-top:20px;">
                  <a class="btn" href="#paralysis-care">Explore &rarr;</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 1.4 How It Works -->
      <section style="background:linear-gradient(180deg, var(--bg), #EDF7F5);">
        <div class="w">
          <span class="ey">SYSTEM WORKFLOW</span>
          <h2>From clinical recommendation to connected care.</h2>
          <p class="lead">Neuro Mates connects the people involved in a patient’s care through a structured referral and patient management system.</p>

          <div class="steps-timeline">
            <div class="step-item">
              <span class="step-num">Step 01</span>
              <div class="step-title">Doctor recommends Neuro Mates</div>
              <p class="body-text">A doctor introduces the appropriate Neuro Mates product based on the patient’s care requirements.</p>
            </div>
            <div class="step-item">
              <span class="step-num">Step 02</span>
              <div class="step-title">Patient receives a referral code</div>
              <p class="body-text">The doctor provides a unique referral ID for the patient registration process.</p>
            </div>
            <div class="step-item">
              <span class="step-num">Step 03</span>
              <div class="step-title">Patient profile is created</div>
              <p class="body-text">The patient receives a unique identity within the Neuro Mates Platform and is connected to the relevant disease-specific care environment.</p>
            </div>
            <div class="step-item">
              <span class="step-num">Step 04</span>
              <div class="step-title">Product and monitoring begin</div>
              <p class="body-text">The appropriate Neuro Mates product and connected devices can be used according to the patient’s care requirements.</p>
            </div>
            <div class="step-item">
              <span class="step-num">Step 05</span>
              <div class="step-title">Platform receives relevant information</div>
              <p class="body-text">Relevant monitoring, activity and care information reaches the connected software environment.</p>
            </div>
            <div class="step-item">
              <span class="step-num">Step 06</span>
              <div class="step-title">Four portals keep the ecosystem connected</div>
              <p class="body-text">Patient, Caretaker, Doctor and Admin portals provide role-specific access to the appropriate information and functions.</p>
            </div>
            <div class="step-item">
              <span class="step-num">Step 07</span>
              <div class="step-title">Alerts and care actions happen</div>
              <p class="body-text">Relevant alerts, reminders, reports and care information are communicated through the appropriate channels.</p>
            </div>
            <div class="step-item">
              <span class="step-num">Step 08</span>
              <div class="step-title">Monitoring continues</div>
              <p class="body-text">The system continues supporting the patient’s ongoing care journey.</p>
            </div>
          </div>
        </div>
      </section>

      <!-- 1.5 Four People, One Platform (Interactive Role Switcher) -->
      <section style="background:#FFFFFF;">
        <div class="w">
          <span class="ey">ROLE-BASED ECOSYSTEM</span>
          <h2>Connected to the people who matter.</h2>

          <div class="role-switcher">
            <div class="role-tabs" role="tablist">
              <button class="role-tab-btn active" data-role="patient">Patient Portal</button>
              <button class="role-tab-btn" data-role="caretaker">Caretaker Portal</button>
              <button class="role-tab-btn" data-role="doctor">Doctor Portal</button>
              <button class="role-tab-btn" data-role="admin">Admin Portal</button>
            </div>

            <div class="role-content-grid">
              <div>
                <h3 id="role-title" style="color:var(--te);font-size:1.8rem;margin-bottom:14px;">Patient Portal</h3>
                <p id="role-desc" class="body-text" style="font-size:1.15rem;line-height:1.7;">
                  Personal care environment with disease-specific monitoring/status, daily activity entry where applicable, medication reminders, appointment reminders, interactive rehabilitation and Alzheimer memory-recall activities.
                </p>
                <div style="margin-top:24px;">
                  <span class="demo-tag">Illustration, not real patient data</span>
                </div>
              </div>
              <div class="device-img-card">
                <img id="role-img" src="assets/images/page_11_Image-979344929.jpg" alt="Connected Care Portals">
                <div class="device-img-badge" id="role-badge">Patient Portal Environment</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 1.6 Technology Section Preview -->
      <section>
        <div class="w">
          <span class="ey">INTELLIGENT HEALTHCARE</span>
          <h2>Technology designed around care.</h2>
          <p class="lead">Neuro Mates combines connected sensing, IoT, AI and machine learning with a web-based care platform to support disease-specific monitoring and rehabilitation.</p>

          <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(260px, 1fr));gap:24px;margin-top:40px;">
            <div style="background:#FFFFFF;padding:28px;border-radius:20px;border:1px solid rgba(14,59,67,0.08);">
              <h4 style="color:var(--te);margin-bottom:8px;">Connected sensing</h4>
              <p class="body-text">Movement, location and other disease-specific sensing technologies.</p>
            </div>
            <div style="background:#FFFFFF;padding:28px;border-radius:20px;border:1px solid rgba(14,59,67,0.08);">
              <h4 style="color:var(--te);margin-bottom:8px;">Intelligent monitoring</h4>
              <p class="body-text">AI and machine-learning approaches for analysing patient information.</p>
            </div>
            <div style="background:#FFFFFF;padding:28px;border-radius:20px;border:1px solid rgba(14,59,67,0.08);">
              <h4 style="color:var(--te);margin-bottom:8px;">Personalised support</h4>
              <p class="body-text">Disease-specific activities, reminders and rehabilitation.</p>
            </div>
            <div style="background:#FFFFFF;padding:28px;border-radius:20px;border:1px solid rgba(14,59,67,0.08);">
              <h4 style="color:var(--te);margin-bottom:8px;">Connected care platform</h4>
              <p class="body-text">Information shared through Patient, Caretaker, Doctor and Admin role-based environments.</p>
            </div>
          </div>
          <div style="margin-top:36px;">
            <a class="btn" href="#technology">Explore our technology &rarr;</a>
          </div>
        </div>
      </section>

      <!-- 1.7 Project Video Section -->
      <section style="background:var(--dark-video-grad);color:#FFFFFF;">
        <div class="w" style="text-align:center;">
          <span class="ey" style="color:var(--aq);">PROOF OF CONCEPT</span>
          <h2 style="color:#FFFFFF;margin:0 auto;">See Neuro Mates in action.</h2>
          <p style="color:rgba(255,255,255,0.85);font-size:1.15rem;max-width:48ch;margin:16px auto 0;">
            A walkthrough of the Neuro Mates proof of concept across Parkinson’s, Alzheimer’s, Epilepsy and Paralysis care.
          </p>

          <div class="video-wrapper">
            <iframe 
              src="https://www.youtube-nocookie.com/embed/eN_GKuE5eUw" 
              title="Neuro Mates Proof of Concept Demonstration" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen>
            </iframe>
          </div>
          <div style="margin-top:24px;">
            <span class="demo-tag" style="background:rgba(255,255,255,0.15);color:#FFFFFF;">Proof-of-concept demonstration</span>
          </div>
          <div style="margin-top:28px;">
            <a class="btn" href="#register-demo" style="background:#FFFFFF;color:var(--te);">Register for a demo &rarr;</a>
          </div>
        </div>
      </section>

      <!-- 1.8 Trust & Safety -->
      <section>
        <div class="w">
          <span class="ey">RELIABILITY &amp; PRIVACY</span>
          <h2>Built with patient safety in mind.</h2>
          <p class="lead">Healthcare technology must be designed with reliability, privacy and responsible use of patient information in mind. Neuro Mates considers sensor validation, connectivity limitations, patient-specific AI performance and secure role-based access as important parts of the system.</p>

          <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(260px, 1fr));gap:24px;margin-top:40px;">
            <div style="background:#FFFFFF;padding:28px;border-radius:20px;border:1px solid rgba(14,59,67,0.08);">
              <h4 style="color:var(--ink);margin-bottom:8px;">Sensor Validation</h4>
              <p class="body-text">Multiple checks can help reduce false alerts.</p>
            </div>
            <div style="background:#FFFFFF;padding:28px;border-radius:20px;border:1px solid rgba(14,59,67,0.08);">
              <h4 style="color:var(--ink);margin-bottom:8px;">Data Security</h4>
              <p class="body-text">Role-based access separates patient, caretaker, doctor and admin information/functions.</p>
            </div>
            <div style="background:#FFFFFF;padding:28px;border-radius:20px;border:1px solid rgba(14,59,67,0.08);">
              <h4 style="color:var(--ink);margin-bottom:8px;">Reliable Connectivity</h4>
              <p class="body-text">Data can be stored locally and synchronised when connectivity is restored.</p>
            </div>
            <div style="background:#FFFFFF;padding:28px;border-radius:20px;border:1px solid rgba(14,59,67,0.08);">
              <h4 style="color:var(--ink);margin-bottom:8px;">Patient-Specific Intelligence</h4>
              <p class="body-text">AI and ML models can be improved through patient-specific data and testing.</p>
            </div>
          </div>
        </div>
      </section>

      <!-- 1.9 Medical & Research Foundation -->
      <section style="background:#FFFFFF;">
        <div class="w">
          <span class="ey">CLINICAL PERSPECTIVE</span>
          <h2>Technology informed by healthcare needs.</h2>
          <p class="body-text" style="font-size:1.15rem;max-width:54ch;margin-top:20px;">
            Neuro Mates is being developed with an understanding of real-world neurological care challenges and the role of wearable sensing, AI, IoT and remote healthcare technologies. Medical guidance has included consultation with neurological specialists to understand patient-care challenges, monitoring requirements and medical considerations.
          </p>

          <div style="margin-top:36px;display:flex;flex-wrap:wrap;gap:20px;">
            <div style="background:var(--bg);padding:18px 24px;border-radius:16px;border:1px solid rgba(14,59,67,0.08);">
              <strong style="color:var(--ink);display:block;font-size:1.1rem;">Dr. Kirit Shukla</strong>
              <span style="color:var(--mu);font-size:0.9rem;">Neuro Physician</span>
            </div>
            <div style="background:var(--bg);padding:18px 24px;border-radius:16px;border:1px solid rgba(14,59,67,0.08);">
              <strong style="color:var(--ink);display:block;font-size:1.1rem;">Dr. Nishit Patel</strong>
              <span style="color:var(--mu);font-size:0.9rem;">Neuro Physician</span>
            </div>
            <div style="background:var(--bg);padding:18px 24px;border-radius:16px;border:1px solid rgba(14,59,67,0.08);">
              <strong style="color:var(--ink);display:block;font-size:1.1rem;">Dr. G. B. Yadav</strong>
              <span style="color:var(--mu);font-size:0.9rem;">MS, PhD</span>
            </div>
          </div>
          <div style="margin-top:32px;">
            <a class="b2" href="#research">Explore the research &rarr;</a>
          </div>
        </div>
      </section>

      <!-- 1.10 Impact -->
      <section>
        <div class="w">
          <span class="ey">WHAT WE ARE WORKING TO CHANGE</span>
          <h2>Our Impact</h2>
          <div style="display:flex;flex-direction:column;gap:18px;margin-top:36px;">
            <div style="font-family:var(--fd);font-size:clamp(1.2rem,2.2vw,1.6rem);color:var(--ink);"><strong style="color:var(--te);">24/7 support</strong> &mdash; Continuous patient monitoring from home.</div>
            <div style="font-family:var(--fd);font-size:clamp(1.2rem,2.2vw,1.6rem);color:var(--ink);"><strong style="color:var(--te);">Earlier awareness</strong> &mdash; Support for identifying falls, seizures and unsafe situations.</div>
            <div style="font-family:var(--fd);font-size:clamp(1.2rem,2.2vw,1.6rem);color:var(--ink);"><strong style="color:var(--te);">Greater independence</strong> &mdash; Reduce dependence on full-time caretaker support.</div>
            <div style="font-family:var(--fd);font-size:clamp(1.2rem,2.2vw,1.6rem);color:var(--ink);"><strong style="color:var(--te);">Personalised rehabilitation</strong> &mdash; Make regular rehabilitation more accessible and engaging.</div>
            <div style="font-family:var(--fd);font-size:clamp(1.2rem,2.2vw,1.6rem);color:var(--ink);"><strong style="color:var(--te);">Connected care</strong> &mdash; Improve communication between patients, families and doctors.</div>
          </div>
        </div>
      </section>

      <section class="cta"></section>
    </div>

    <!-- ========================================== -->
    <!-- VIEW: PRODUCTS (#products, #parkinsons-care...) -->
    <!-- ========================================== -->
    <div class="page-view" id="view-products">
      <header class="hero">
        <div class="w">
          <span class="ey">PRODUCTS</span>
          <h1>Neurological care, <em>designed around the condition</em>.</h1>
          <p class="lead">Neuro Mates brings together disease-specific products for Parkinson’s, Alzheimer’s, Epilepsy and Paralysis. Each product combines appropriate monitoring, connected technology and personalised care support for the needs of the condition.</p>
          <div class="subnav-pills">
            <button class="subnav-pill active" onclick="location.hash='#products'">Overview</button>
            <button class="subnav-pill" onclick="location.hash='#parkinsons-care'">Parkinson’s Care</button>
            <button class="subnav-pill" onclick="location.hash='#alzheimers-care'">Alzheimer’s Care</button>
            <button class="subnav-pill" onclick="location.hash='#epilepsy-care'">Epilepsy Care</button>
            <button class="subnav-pill" onclick="location.hash='#paralysis-care'">Paralysis Care</button>
          </div>
        </div>
      </header>

      <!-- Subview: Parkinson's -->
      <section id="sec-parkinsons" style="padding-top:20px;">
        <div class="w">
          <div style="display:grid;grid-template-columns:1.2fr 1fr;gap:48px;align-items:center;">
            <div>
              <span class="ey" style="color:var(--parkinsons-1);">PARKINSON’S CARE</span>
              <h2>Supporting movement. Encouraging rehabilitation.</h2>
              <p class="lead">Parkinson’s can affect movement, balance and everyday physical activity. Neuro Mates is designed to support movement monitoring and make rehabilitation more engaging through interactive exercises.</p>
              <div style="margin-top:24px;">
                <h4 style="color:var(--ink);margin-bottom:8px;">Movement monitoring</h4>
                <p class="body-text">A lightweight wearable worn on the back of the hand uses motion sensors to continuously collect movement data. Real-time analysis can identify abnormal conditions such as hand tremors or falls.</p>
                <div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:14px;">
                  <span class="demo-tag">&bull; Tremor and motion tracking</span>
                  <span class="demo-tag">&bull; Lightweight, ergonomic wearable</span>
                  <span class="demo-tag">&bull; Adjustable strap</span>
                  <span class="demo-tag">&bull; Status light</span>
                </div>
              </div>
            </div>
            <div class="device-img-card">
              <img src="assets/images/parkinsons-wearable.jpg" alt="Parkinson's Wearable on Hand">
              <div class="device-img-badge">Back of Hand Wearable</div>
            </div>
          </div>

          <!-- Emergency Response Demo -->
          <div style="background:#FFFFFF;border-radius:28px;padding:36px;margin-top:48px;border:1px solid rgba(14,59,67,0.08);">
            <span class="ey" style="color:var(--co);">INTERACTIVE DEMONSTRATION</span>
            <h3>When something is wrong, the family knows.</h3>
            <p class="body-text" style="max-width:54ch;">
              When abnormal activity is detected, a WhatsApp alert can be sent to the family and an emergency siren can be activated through the speaker. The patient can also raise an alert with a manual emergency switch. When the condition returns to normal, a recovery/safe confirmation is sent.
            </p>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:32px;align-items:center;margin-top:24px;">
              <div>
                <button class="btn" id="btn-fall-sim" style="background:var(--co);">Simulate a fall &rarr;</button>
                <div id="fall-sim-status" style="margin-top:18px;font-weight:700;color:var(--gr);font-size:1.05rem;">
                  Status: 1. Normal movement monitored.
                </div>
                <div style="margin-top:10px;"><span class="demo-tag">Illustration, not real patient data</span></div>
              </div>
              <div class="device-img-card" style="max-height:280px;">
                <img src="assets/images/parkinsons-dashboard.jpg" alt="WhatsApp Alert and Dashboard Confirmation">
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Subview: Alzheimer's -->
      <section id="sec-alzheimers" style="background:#FFFFFF;border-top:1px solid rgba(14,59,67,0.06);">
        <div class="w">
          <div style="display:grid;grid-template-columns:1.2fr 1fr;gap:48px;align-items:center;">
            <div>
              <span class="ey" style="color:var(--alzheimers-1);">ALZHEIMER’S CARE</span>
              <h2>Supporting memory, routine and patient safety.</h2>
              <p class="lead">Neuro Mates Alzheimer’s Care combines daily activity tracking, personalised memory-recall activities, medication support and location-based safety monitoring to support patients and their families.</p>
              <div style="margin-top:20px;">
                <h4 style="color:var(--ink);">Daily Activity Recording</h4>
                <p class="body-text">Patients can record daily activities from 8 AM to 10 PM at two-hour intervals, creating a structured view of their daily routine.</p>
                <div style="display:flex;gap:12px;margin-top:12px;">
                  <span class="demo-tag">Breakfast</span>
                  <span class="demo-tag">Medicine</span>
                  <span class="demo-tag">Walking</span>
                </div>
              </div>
            </div>
            <div class="device-img-card">
              <img src="assets/images/alzheimers-wearable.jpg" alt="Alzheimer's Patient Safety Wearable">
              <div class="device-img-badge">Patient Safety Wearable</div>
            </div>
          </div>

          <!-- Memory Quiz Card -->
          <div style="background:var(--bg);border-radius:28px;padding:36px;margin-top:48px;border:1px solid rgba(14,59,67,0.08);max-width:640px;">
            <span class="ey">INTERACTIVE MEMORY CHECK-IN</span>
            <h3>Try a daily memory check-in.</h3>
            <p style="font-size:1.1rem;color:var(--ink);margin:16px 0 20px;font-weight:600;">Which of these did you have for breakfast today?</p>
            <div style="display:flex;flex-direction:column;gap:12px;" id="quiz-options">
              <button class="b2 quiz-opt" style="text-align:left;justify-content:flex-start;padding:16px 24px;border-radius:16px;background:#FFF;" data-correct="true">Tea and toast</button>
              <button class="b2 quiz-opt" style="text-align:left;justify-content:flex-start;padding:16px 24px;border-radius:16px;background:#FFF;" data-correct="false">Idli and sambar</button>
              <button class="b2 quiz-opt" style="text-align:left;justify-content:flex-start;padding:16px 24px;border-radius:16px;background:#FFF;" data-correct="false">Poha</button>
            </div>
            <div id="quiz-feedback" style="margin-top:16px;font-weight:700;font-size:1.05rem;display:none;"></div>
            <div style="margin-top:14px;"><span class="demo-tag">Illustration, not real patient data</span></div>
          </div>
        </div>
      </section>

      <!-- Subview: Epilepsy -->
      <section id="sec-epilepsy">
        <div class="w">
          <div style="display:grid;grid-template-columns:1.2fr 1fr;gap:48px;align-items:center;">
            <div>
              <span class="ey" style="color:var(--epilepsy-1);">EPILEPSY CARE</span>
              <h2>Helping families stay connected during epilepsy monitoring.</h2>
              <p class="lead">The Neuro Mates epilepsy monitoring system continuously observes brain activity and connects abnormal EEG activity with immediate family alerts, emergency response and continued monitoring.</p>
              <div style="margin-top:20px;">
                <h4 style="color:var(--ink);">Continuous monitoring</h4>
                <p class="body-text">A lightweight headband with a brain-signal sensor continuously monitors the patient’s brain activity. A reference electrode sits behind the ear. The EEG view can show Alpha, Beta, Gamma, Delta and Theta waves.</p>
                <div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:12px;">
                  <span class="demo-tag">&bull; EEG monitoring</span>
                  <span class="demo-tag">&bull; Real-time alerts</span>
                  <span class="demo-tag">&bull; Lightweight design</span>
                  <span class="demo-tag">&bull; Safe and comfortable</span>
                </div>
              </div>
            </div>
            <div class="device-img-card">
              <img src="assets/images/epilepsy-headband.jpg" alt="Epilepsy Monitoring Wearable Headband">
              <div class="device-img-badge">EEG Headband Wearable</div>
            </div>
          </div>

          <!-- Strict Epilepsy Safety Wording Box -->
          <div style="background:rgba(43,181,138,0.08);border-left:4px solid var(--epilepsy-1);padding:24px 28px;border-radius:0 18px 18px 0;margin-top:40px;">
            <p style="margin:0;font-size:1.05rem;color:var(--ink);font-weight:600;">
              Neuro Mates monitors for abnormal EEG signals that may indicate a seizure. It does not diagnose, predict or prevent seizures, and detection cannot be guaranteed.
            </p>
          </div>
        </div>
      </section>

      <!-- Subview: Paralysis -->
      <section id="sec-paralysis" style="background:#FFFFFF;border-top:1px solid rgba(14,59,67,0.06);">
        <div class="w">
          <div style="display:grid;grid-template-columns:1.2fr 1fr;gap:48px;align-items:center;">
            <div>
              <span class="ey" style="color:var(--paralysis-1);">PARALYSIS REHABILITATION</span>
              <h2>Making rehabilitation more engaging.</h2>
              <p class="lead">Neuro Mates Paralysis Care uses interactive, game-based rehabilitation activities to encourage patients to perform prescribed exercises using different areas of the body.</p>
              <div style="margin-top:20px;">
                <h4 style="color:var(--ink);">Rehabilitation at your own pace</h4>
                <p class="body-text">Skin electrodes and muscle-signal sensors pick up the electrical activity of a muscle, and brain signals and facial expressions can also be used. These signals control the game, and the screen shows the patient’s repetitions and session progress.</p>
              </div>
            </div>
            <div class="device-img-card">
              <img src="assets/images/rehab-leg.jpg" alt="Interactive Leg Rehabilitation">
              <div class="device-img-badge">Leg Rehabilitation Physiotherapy</div>
            </div>
          </div>

          <!-- Rehabilitation Areas Gallery -->
          <div style="margin-top:48px;">
            <span class="ey">TARGETED EXERCISE AREAS</span>
            <h3>Exercise with different parts of the body</h3>
            <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(260px, 1fr));gap:24px;margin-top:28px;">
              <div class="device-img-card">
                <img src="assets/images/rehab-face.jpg" alt="Facial Rehabilitation">
                <div style="padding:20px;">
                  <h4 style="color:var(--ink);">Eyes / Face</h4>
                  <p class="body-text" style="font-size:0.92rem;margin-top:6px;">Facial and eye-based activities where applicable.</p>
                </div>
              </div>
              <div class="device-img-card">
                <img src="assets/images/rehab-hand.jpg" alt="Hand & Finger Rehabilitation">
                <div style="padding:20px;">
                  <h4 style="color:var(--ink);">Hands</h4>
                  <p class="body-text" style="font-size:0.92rem;margin-top:6px;">Interactive hand and finger exercises.</p>
                </div>
              </div>
              <div class="device-img-card">
                <img src="assets/images/rehab-leg.jpg" alt="Leg Movement Rehabilitation">
                <div style="padding:20px;">
                  <h4 style="color:var(--ink);">Legs &amp; Joints</h4>
                  <p class="body-text" style="font-size:0.92rem;margin-top:6px;">Movement-based leg and joint exercises.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="cta"></section>
    </div>

    <!-- ========================================== -->
    <!-- VIEW: TECHNOLOGY (#technology...)          -->
    <!-- ========================================== -->
    <div class="page-view" id="view-technology">
      <header class="hero">
        <div class="w">
          <span class="ey">TECHNOLOGY</span>
          <h1>Connecting sensing, <em>intelligence and care</em>.</h1>
          <p class="lead">Neuro Mates combines hardware, IoT connectivity, AI and machine learning with a connected software platform to support neurological monitoring and rehabilitation.</p>
          <div class="subnav-pills">
            <button class="subnav-pill active" onclick="location.hash='#technology'">Overview</button>
            <button class="subnav-pill" onclick="location.hash='#connected-devices'">Connected Devices</button>
            <button class="subnav-pill" onclick="location.hash='#ai-machine-learning'">AI &amp; Machine Learning</button>
            <button class="subnav-pill" onclick="location.hash='#monitoring-analytics'">Monitoring &amp; Analytics</button>
            <button class="subnav-pill" onclick="location.hash='#connected-care-platform'">Care Platform</button>
          </div>
        </div>
      </header>

      <!-- Four Layers Architecture -->
      <section style="background:#FFFFFF;border-top:1px solid rgba(14,59,67,0.06);">
        <div class="w">
          <span class="ey">ARCHITECTURE</span>
          <h2>The Four Layers of Neuro Mates</h2>
          <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(250px, 1fr));gap:24px;margin-top:36px;">
            <div style="background:var(--bg);border-radius:20px;padding:26px;border-left:4px solid #6EC1F0;">
              <span class="demo-tag" style="color:#6EC1F0;">Layer 1</span>
              <h3 style="margin:10px 0 6px;">Sensing</h3>
              <p class="body-text">GPS, movement sensors, EEG and other disease-specific sensing technologies.</p>
            </div>
            <div style="background:var(--bg);border-radius:20px;padding:26px;border-left:4px solid #7C6CFF;">
              <span class="demo-tag" style="color:#7C6CFF;">Layer 2</span>
              <h3 style="margin:10px 0 6px;">Connectivity</h3>
              <p class="body-text">IoT-based communication between devices and the platform.</p>
            </div>
            <div style="background:var(--bg);border-radius:20px;padding:26px;border-left:4px solid #2BB58A;">
              <span class="demo-tag" style="color:#2BB58A;">Layer 3</span>
              <h3 style="margin:10px 0 6px;">Intelligence</h3>
              <p class="body-text">AI and machine learning for patient-specific monitoring and analysis.</p>
            </div>
            <div style="background:var(--bg);border-radius:20px;padding:26px;border-left:4px solid #F5A623;">
              <span class="demo-tag" style="color:#F5A623;">Layer 4</span>
              <h3 style="margin:10px 0 6px;">Care Platform</h3>
              <p class="body-text">The connecting layer between disease-specific devices, patient information, care interactions and role-based access.</p>
            </div>
          </div>

          <div style="background:var(--dark-teal-grad);border-radius:28px;padding:40px;margin-top:48px;color:#FFFFFF;text-align:center;">
            <h3 style="color:#FFFFFF;font-size:1.8rem;">Hardware sensing is only one layer.</h3>
            <p style="color:rgba(255,255,255,0.85);max-width:54ch;margin:16px auto 0;font-size:1.1rem;">
              The Neuro Mates Platform receives and organises relevant information and makes the appropriate information available to the correct role: Patient, Caretaker, Doctor or Admin.
            </p>
          </div>
        </div>
      </section>

      <!-- Connected Hardware Gallery -->
      <section id="sec-devices-gallery">
        <div class="w">
          <span class="ey">CONNECTED HARDWARE</span>
          <h2>Disease-specific devices, one platform.</h2>
          <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));gap:32px;margin-top:36px;">
            <div class="device-img-card">
              <img src="assets/images/alzheimers-wearable.jpg" alt="Location tracker">
              <div style="padding:24px;">
                <span class="demo-tag" style="color:var(--alzheimers-1);">Alzheimer’s</span>
                <h4 style="margin:10px 0 6px;">Location tracker</h4>
                <p class="body-text" style="font-size:0.95rem;">Continuous patient location tracking and safe-zone monitoring.</p>
              </div>
            </div>
            <div class="device-img-card">
              <img src="assets/images/parkinsons-wearable.jpg" alt="Wearable motion sensor">
              <div style="padding:24px;">
                <span class="demo-tag" style="color:var(--parkinsons-1);">Parkinson’s</span>
                <h4 style="margin:10px 0 6px;">Wearable motion sensor</h4>
                <p class="body-text" style="font-size:0.95rem;">Movement data for tremor and fall monitoring.</p>
              </div>
            </div>
            <div class="device-img-card">
              <img src="assets/images/epilepsy-headband.jpg" alt="Brain-signal headband">
              <div style="padding:24px;">
                <span class="demo-tag" style="color:var(--epilepsy-1);">Epilepsy</span>
                <h4 style="margin:10px 0 6px;">Brain-signal (EEG) headband</h4>
                <p class="body-text" style="font-size:0.95rem;">Continuous brain-activity monitoring; a heart-rate sensor provides additional data.</p>
              </div>
            </div>
            <div class="device-img-card">
              <img src="assets/images/rehab-platform.jpg" alt="Muscle-signal sensor">
              <div style="padding:24px;">
                <span class="demo-tag" style="color:var(--paralysis-1);">Rehabilitation</span>
                <h4 style="margin:10px 0 6px;">Muscle-signal sensors</h4>
                <p class="body-text" style="font-size:0.95rem;">Interactive rehabilitation activities where applicable.</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="cta"></section>
    </div>

    <!-- ========================================== -->
    <!-- VIEW: INSIGHTS (#insights, #research...)   -->
    <!-- ========================================== -->
    <div class="page-view" id="view-insights">
      <header class="hero">
        <div class="w">
          <span class="ey">INSIGHTS</span>
          <h1>Research, technology and perspectives on <em>neurological care</em>.</h1>
          <p class="lead">Explore the research and ideas informing Neuro Mates and the broader development of connected neurological care.</p>
        </div>
      </header>

      <section style="background:#FFFFFF;border-top:1px solid rgba(14,59,67,0.06);">
        <div class="w">
          <!-- Editorial Index List (with right arrows) -->
          <div style="display:flex;flex-direction:column;gap:16px;">
            <a href="#research" class="device-img-card" style="padding:24px 32px;display:flex;align-items:center;justify-content:space-between;text-decoration:none;">
              <div>
                <h3 style="color:var(--ink);margin-bottom:4px;">Research</h3>
                <p class="body-text" style="margin:0;">Neurological monitoring and rehabilitation research.</p>
              </div>
              <span style="font-size:1.6rem;color:var(--te);">&rarr;</span>
            </a>
            <div class="device-img-card" style="padding:24px 32px;display:flex;align-items:center;justify-content:space-between;">
              <div>
                <h3 style="color:var(--ink);margin-bottom:4px;">Articles</h3>
                <p class="body-text" style="margin:0;">Technology and neurological healthcare topics. <em style="font-size:0.9rem;color:var(--mu);">(Articles will appear here.)</em></p>
              </div>
              <span style="font-size:1.6rem;color:var(--mu);">&rarr;</span>
            </div>
            <div class="device-img-card" style="padding:24px 32px;display:flex;align-items:center;justify-content:space-between;">
              <div>
                <h3 style="color:var(--ink);margin-bottom:4px;">Case Studies</h3>
                <p class="body-text" style="margin:0;">Real-world applications and project learnings. <em style="font-size:0.9rem;color:var(--mu);">(Case studies will appear here.)</em></p>
              </div>
              <span style="font-size:1.6rem;color:var(--mu);">&rarr;</span>
            </div>
            <div class="device-img-card" style="padding:24px 32px;display:flex;align-items:center;justify-content:space-between;">
              <div>
                <h3 style="color:var(--ink);margin-bottom:4px;">Resources</h3>
                <p class="body-text" style="margin:0;">Reports, references and educational material. <em style="font-size:0.9rem;color:var(--mu);">(Resources will appear here.)</em></p>
              </div>
              <span style="font-size:1.6rem;color:var(--mu);">&rarr;</span>
            </div>
          </div>

          <!-- Research References Sub-section -->
          <div id="sec-research-refs" style="margin-top:64px;">
            <span class="ey">SCIENTIFIC FOUNDATION</span>
            <h2>Research</h2>
            <p class="lead">Neurological monitoring and rehabilitation research.</p>
            <div style="display:flex;flex-direction:column;gap:14px;margin-top:28px;">
              <a href="#" class="b2" style="justify-content:flex-start;padding:16px 24px;border-radius:16px;text-align:left;background:var(--bg);" target="_blank" rel="noopener">
                &bull; Determining Falls Risk in People with Parkinson’s Disease Using Wearable Sensors &mdash; Sensors, 2025 &rarr;
              </a>
              <a href="#" class="b2" style="justify-content:flex-start;padding:16px 24px;border-radius:16px;text-align:left;background:var(--bg);" target="_blank" rel="noopener">
                &bull; EEG-Based Epileptic Seizure Detection via Machine/Deep Learning Approaches &mdash; 2022 &rarr;
              </a>
              <a href="#" class="b2" style="justify-content:flex-start;padding:16px 24px;border-radius:16px;text-align:left;background:var(--bg);" target="_blank" rel="noopener">
                &bull; Effects of Reminiscence Therapy on Cognition, Depression and Quality of Life in Elderly People with Alzheimer’s Disease: A Systematic Review of Randomized Controlled Trials &mdash; PubMed &rarr;
              </a>
              <a href="#" class="b2" style="justify-content:flex-start;padding:16px 24px;border-radius:16px;text-align:left;background:var(--bg);" target="_blank" rel="noopener">
                &bull; A scoping review on remote patient monitoring technologies &mdash; Discover Artificial Intelligence, Springer Nature &rarr;
              </a>
              <a href="#" class="b2" style="justify-content:flex-start;padding:16px 24px;border-radius:16px;text-align:left;background:var(--bg);" target="_blank" rel="noopener">
                &bull; IoT-Enabled healthcare ecosystems: innovations in remote monitoring, patient outcomes, and digital transformation &mdash; PubMed &rarr;
              </a>
            </div>
            <!-- Research Disclaimer -->
            <div style="background:rgba(14,59,67,0.05);padding:20px 24px;border-radius:16px;margin-top:28px;">
              <p style="margin:0;font-size:0.95rem;color:var(--mu);line-height:1.6;">
                <strong>Research disclaimer:</strong> Research references are provided to show broader scientific and technological context relevant to neurological monitoring, rehabilitation and remote healthcare. They are not research authored or clinically validated by Neuro Mates.
              </p>
            </div>
          </div>
        </div>
      </section>

      <section class="cta"></section>
    </div>

    <!-- ========================================== -->
    <!-- VIEW: ABOUT US (#about, #vision-mission...) -->
    <!-- ========================================== -->
    <div class="page-view" id="view-about">
      <header class="hero">
        <div class="w">
          <span class="ey">ABOUT US</span>
          <h1>Building technology around the realities of <em>neurological care</em>.</h1>
          <p class="lead">Neuro Mates is building connected care systems designed around the needs of people living with neurological conditions, their families and the healthcare professionals involved in their care.</p>
          <div class="subnav-pills">
            <button class="subnav-pill active" onclick="location.hash='#about'">About Us</button>
            <button class="subnav-pill" onclick="location.hash='#vision-mission'">Vision &amp; Mission</button>
            <button class="subnav-pill" onclick="location.hash='#our-approach'">Our Approach</button>
            <button class="subnav-pill" onclick="location.hash='#impact'">Impact</button>
          </div>
        </div>
      </header>

      <section style="background:#FFFFFF;border-top:1px solid rgba(14,59,67,0.06);">
        <div class="w">
          <div style="display:grid;grid-template-columns:1.2fr 1fr;gap:48px;align-items:center;">
            <div>
              <span class="ey">OUR STORY</span>
              <h2>Our story</h2>
              <p class="body-text" style="font-size:1.15rem;line-height:1.7;">
                Neuro Mates began with a simple question: how can technology help patients and families manage the challenges that continue between clinical visits? The project is motivated by challenges around continuous care, monitoring limitations, caretaker dependency, falls, seizures, missed medication, getting lost and rehabilitation.
              </p>
              <h3 style="margin-top:28px;color:var(--ink);">Connected care beyond the clinic.</h3>
              <p class="body-text">Neuro Mates is developing a connected care concept that brings disease-specific monitoring, rehabilitation, reminders and communication into one ecosystem.</p>
            </div>
            <div class="device-img-card">
              <img src="assets/images/alzheimers-wearable.jpg" alt="Patient and family care in the community">
              <div class="device-img-badge">Family &bull; Patient &bull; Community</div>
            </div>
          </div>

          <!-- Vision & Mission -->
          <div id="sec-vision" style="background:var(--dark-teal-grad);border-radius:32px;padding:clamp(36px, 6vw, 64px);color:#FFFFFF;margin-top:64px;">
            <div style="max-width:640px;">
              <span class="ey" style="color:var(--aq);">VISION &amp; MISSION</span>
              <h3 style="color:#FFFFFF;font-size:2rem;margin-bottom:14px;">A future where neurological care stays connected.</h3>
              <p style="color:rgba(255,255,255,0.9);font-size:1.15rem;line-height:1.7;">
                <strong>Vision:</strong> Our vision is to make continuous neurological care more accessible, connected and personalised by bringing patients, families, healthcare professionals and technology into one care ecosystem.
              </p>
              <p style="color:rgba(255,255,255,0.9);font-size:1.15rem;line-height:1.7;margin-top:18px;">
                <strong>Mission:</strong> To develop practical technology that supports neurological patients beyond the clinic through intelligent monitoring, personalised rehabilitation, connected devices and meaningful communication between patients, caretakers and doctors.
              </p>
            </div>
          </div>

          <!-- Our Approach -->
          <div id="sec-approach" style="margin-top:64px;">
            <span class="ey">OUR PHILOSOPHY</span>
            <h2>Technology should support people, not complicate their care.</h2>
            <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(240px, 1fr));gap:24px;margin-top:32px;">
              <div style="background:var(--bg);border-radius:20px;padding:26px;border:1px solid rgba(14,59,67,0.08);">
                <h4 style="color:var(--te);margin-bottom:8px;">Patient-centred</h4>
                <p class="body-text">Designed around everyday patient needs.</p>
              </div>
              <div style="background:var(--bg);border-radius:20px;padding:26px;border:1px solid rgba(14,59,67,0.08);">
                <h4 style="color:var(--te);margin-bottom:8px;">Connected</h4>
                <p class="body-text">Bringing patients, caretakers and doctors into one ecosystem.</p>
              </div>
              <div style="background:var(--bg);border-radius:20px;padding:26px;border:1px solid rgba(14,59,67,0.08);">
                <h4 style="color:var(--te);margin-bottom:8px;">Personalised</h4>
                <p class="body-text">Adapting care support to the condition and patient.</p>
              </div>
              <div style="background:var(--bg);border-radius:20px;padding:26px;border:1px solid rgba(14,59,67,0.08);">
                <h4 style="color:var(--te);margin-bottom:8px;">Responsible</h4>
                <p class="body-text">Considering privacy, reliability, safety and the limitations of AI and connected devices.</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="cta"></section>
    </div>

    <!-- ========================================== -->
    <!-- VIEW: CONTACT US (#contact)                -->
    <!-- ========================================== -->
    <div class="page-view" id="view-contact">
      <header class="hero">
        <div class="w" style="text-align:center;">
          <span class="ey">GET IN TOUCH</span>
          <h1 style="margin:0 auto;">Let’s talk about <em>connected neurological care</em>.</h1>
          <p class="lead" style="margin:20px auto 0;">Interested in Neuro Mates, our products, healthcare collaboration or a product demonstration? Get in touch with our team.</p>
        </div>
      </header>

      <section style="padding-top:0;">
        <div class="w">
          <div class="form-card">
            <form id="contact-form" novalidate>
              <!-- Honeypot -->
              <input type="text" name="website_hp" style="display:none;" tabindex="-1" autocomplete="off">

              <div class="form-group">
                <label for="c-name">Full Name *</label>
                <input class="form-input" id="c-name" type="text" required placeholder="Dr. / Mr. / Ms.">
              </div>

              <div class="form-group">
                <label for="c-email">Email Address *</label>
                <input class="form-input" id="c-email" type="email" required placeholder="name@organisation.com">
              </div>

              <div class="form-group">
                <label for="c-phone">Phone Number *</label>
                <input class="form-input" id="c-phone" type="tel" required placeholder="+91 ...">
              </div>

              <div class="form-group">
                <label for="c-org">Organisation / Hospital</label>
                <input class="form-input" id="c-org" type="text" placeholder="Clinic, Hospital, or Research Institute">
              </div>

              <div class="form-group">
                <label>I am interested in</label>
                <div class="chips-group" id="c-chips">
                  <span class="chip-item selected">Parkinson’s Care</span>
                  <span class="chip-item">Alzheimer’s Care</span>
                  <span class="chip-item">Epilepsy Care</span>
                  <span class="chip-item">Paralysis Care</span>
                  <span class="chip-item">Healthcare Partnership</span>
                  <span class="chip-item">Product Demonstration</span>
                  <span class="chip-item">Other</span>
                </div>
              </div>

              <div class="form-group">
                <label for="c-msg">Message *</label>
                <textarea class="form-textarea" id="c-msg" rows="4" required placeholder="How can we assist you? (Please do not include personal medical details.)"></textarea>
              </div>

              <button class="btn" type="submit" id="c-submit" style="width:100%;margin-top:12px;">Send enquiry &rarr;</button>
              <div id="c-feedback" style="margin-top:16px;text-align:center;font-weight:700;display:none;"></div>
            </form>
          </div>
        </div>
      </section>

      <section class="cta"></section>
    </div>

    <!-- ========================================== -->
    <!-- VIEW: REGISTER FOR DEMO (#register-demo)   -->
    <!-- ========================================== -->
    <div class="page-view" id="view-register-demo">
      <header class="hero" style="background:var(--dark-teal-grad);color:#FFFFFF;text-align:center;">
        <div class="w">
          <span class="ey" style="color:var(--aq);">LIVE DEMONSTRATION</span>
          <h1 style="color:#FFFFFF;margin:0 auto;">See Neuro Mates in <em>action</em>.</h1>
          <p style="color:rgba(255,255,255,0.85);font-size:1.15rem;max-width:52ch;margin:20px auto 0;line-height:1.65;">
            Request a demonstration of the Neuro Mates Platform and explore how our disease-specific products connect patients, caretakers, doctors and the operational Admin environment.
          </p>
        </div>
      </header>

      <section style="padding-top:40px;">
        <div class="w">
          <div class="form-card">
            <form id="demo-form" novalidate>
              <input type="text" name="demo_hp" style="display:none;" tabindex="-1" autocomplete="off">

              <div class="form-group">
                <label for="d-name">Name *</label>
                <input class="form-input" id="d-name" type="text" required placeholder="Full Name">
              </div>

              <div class="form-group">
                <label for="d-org">Organisation *</label>
                <input class="form-input" id="d-org" type="text" required placeholder="Hospital / Care Centre / Institute">
              </div>

              <div class="form-group">
                <label for="d-role">Role *</label>
                <input class="form-input" id="d-role" type="text" required placeholder="Physician / Caregiver / Administrator / Other">
              </div>

              <div class="form-group">
                <label for="d-email">Email *</label>
                <input class="form-input" id="d-email" type="email" required placeholder="email@address.com">
              </div>

              <div class="form-group">
                <label for="d-phone">Phone *</label>
                <input class="form-input" id="d-phone" type="tel" required placeholder="+91 ...">
              </div>

              <div class="form-group">
                <label>Product of interest</label>
                <div class="chips-group" id="d-chips-prod">
                  <span class="chip-item selected">Parkinson’s Care</span>
                  <span class="chip-item">Alzheimer’s Care</span>
                  <span class="chip-item">Epilepsy Care</span>
                  <span class="chip-item">Paralysis Care</span>
                  <span class="chip-item">Not sure yet</span>
                </div>
              </div>

              <div class="form-group">
                <label>Preferred contact method</label>
                <div class="chips-group" id="d-chips-contact">
                  <span class="chip-item selected">Email</span>
                  <span class="chip-item">Phone</span>
                  <span class="chip-item">Either</span>
                </div>
              </div>

              <div class="form-group">
                <label for="d-msg">Message</label>
                <textarea class="form-textarea" id="d-msg" rows="3" placeholder="Any specific requirements or questions?"></textarea>
              </div>

              <button class="btn" type="submit" id="d-submit" style="width:100%;margin-top:12px;">Request a demo &rarr;</button>
              <div id="d-feedback" style="margin-top:16px;text-align:center;font-weight:700;display:none;"></div>
            </form>
          </div>
        </div>
      </section>

      <section class="cta"></section>
    </div>
  </main>

  <!-- Global Footer -->
  <footer id="global-footer"></footer>

  <script src="assets/js/shared.js"></script>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      // 1. Shared Footer and CTA injection
      document.querySelectorAll('.cta').forEach(c => {
        c.innerHTML = window.NeuroShared.getCTAHTML();
      });
      const footerEl = document.getElementById('global-footer');
      if (footerEl) footerEl.innerHTML = window.NeuroShared.getFooterHTML();

      // 2. SPA View Router (Single URL hash switcher)
      const views = {
        'home': document.getElementById('view-home'),
        'products': document.getElementById('view-products'),
        'parkinsons-care': document.getElementById('view-products'),
        'alzheimers-care': document.getElementById('view-products'),
        'epilepsy-care': document.getElementById('view-products'),
        'paralysis-care': document.getElementById('view-products'),
        'technology': document.getElementById('view-technology'),
        'connected-devices': document.getElementById('view-technology'),
        'ai-machine-learning': document.getElementById('view-technology'),
        'monitoring-analytics': document.getElementById('view-technology'),
        'connected-care-platform': document.getElementById('view-technology'),
        'insights': document.getElementById('view-insights'),
        'research': document.getElementById('view-insights'),
        'articles': document.getElementById('view-insights'),
        'case-studies': document.getElementById('view-insights'),
        'resources': document.getElementById('view-insights'),
        'about': document.getElementById('view-about'),
        'vision-mission': document.getElementById('view-about'),
        'our-approach': document.getElementById('view-about'),
        'impact': document.getElementById('view-about'),
        'contact': document.getElementById('view-contact'),
        'register-demo': document.getElementById('view-register-demo')
      };

      function route() {
        const hash = (location.hash || '#home').replace('#', '').toLowerCase();
        const targetView = views[hash] || views['home'];

        // Toggle active view
        document.querySelectorAll('.page-view').forEach(v => v.classList.remove('active'));
        if (targetView) targetView.classList.add('active');

        // Scroll to specific sub-section if matched
        if (hash === 'parkinsons-care') {
          document.getElementById('sec-parkinsons')?.scrollIntoView({ behavior: 'smooth' });
        } else if (hash === 'alzheimers-care') {
          document.getElementById('sec-alzheimers')?.scrollIntoView({ behavior: 'smooth' });
        } else if (hash === 'epilepsy-care') {
          document.getElementById('sec-epilepsy')?.scrollIntoView({ behavior: 'smooth' });
        } else if (hash === 'paralysis-care') {
          document.getElementById('sec-paralysis')?.scrollIntoView({ behavior: 'smooth' });
        } else if (hash === 'connected-devices') {
          document.getElementById('sec-devices-gallery')?.scrollIntoView({ behavior: 'smooth' });
        } else if (hash === 'research') {
          document.getElementById('sec-research-refs')?.scrollIntoView({ behavior: 'smooth' });
        } else if (hash === 'vision-mission') {
          document.getElementById('sec-vision')?.scrollIntoView({ behavior: 'smooth' });
        } else if (hash === 'our-approach') {
          document.getElementById('sec-approach')?.scrollIntoView({ behavior: 'smooth' });
        } else {
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        // Update nav active link
        document.querySelectorAll('nav ul a').forEach(a => {
          const h = a.getAttribute('href');
          const isMatch = h === `#${hash}` || (hash.includes('care') && h === '#products') || (hash.includes('devices') && h === '#technology');
          a.closest('li')?.classList.toggle('active', isMatch);
        });
      }

      window.addEventListener('hashchange', route);
      route();

      // 3. Interactive Role Switcher in Home view
      const roleData = {
        patient: {
          title: 'Patient Portal',
          desc: 'Personal care environment with disease-specific monitoring/status, daily activity entry where applicable, medication reminders, appointment reminders, interactive rehabilitation and Alzheimer memory-recall activities.',
          badge: 'Patient Portal Environment',
          img: 'assets/images/page_11_Image-979344929.jpg'
        },
        caretaker: {
          title: 'Caretaker Portal',
          desc: 'Relevant emergency alerts, Alzheimer location/safety information, activity information, medication-related reminders/alerts, rehabilitation/care status and normal-state confirmations where applicable.',
          badge: 'Caretaker Alert & Safety Interface',
          img: 'assets/images/page_3_Image-2000805986.jpg'
        },
        doctor: {
          title: 'Doctor Portal',
          desc: 'Patient information, disease-specific monitoring, daily/weekly/monthly reports where available, Alzheimer activity/memory information, Parkinson movement information, Epilepsy monitoring information and Paralysis rehabilitation information.',
          badge: 'Clinical Telemetry & Reports',
          img: 'assets/images/page_12_Image-2708199956.jpg'
        },
        admin: {
          title: 'Admin Portal',
          desc: 'Platform operational environment including relevant user/patient relationships, product/device configuration, Alzheimer safe-zone configuration, operational status and communication/alert environment.',
          badge: 'System & Device Operations',
          img: 'assets/images/page_13_Image-6703682664.jpg'
        }
      };

      document.querySelectorAll('.role-tab-btn').forEach(btn => {
        btn.addEventListener('click', () => {
          document.querySelectorAll('.role-tab-btn').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          const role = btn.dataset.role;
          const data = roleData[role];
          if (data) {
            document.getElementById('role-title').textContent = data.title;
            document.getElementById('role-desc').textContent = data.desc;
            document.getElementById('role-badge').textContent = data.badge;
            document.getElementById('role-img').src = data.img;
          }
        });
      });

      // 4. Fall Simulation Interactive Demo
      const fallBtn = document.getElementById('btn-fall-sim');
      const fallStatus = document.getElementById('fall-sim-status');
      if (fallBtn && fallStatus) {
        let step = 0;
        const states = [
          'Status: 1. Normal movement monitored.',
          'Status: 2. Abnormal movement detected! (Tremor / sudden fall)',
          'Status: 3. WhatsApp alert sent to family, siren activated!',
          'Status: 4. Condition returns to normal.',
          'Status: 5. Safe confirmation sent. Normal monitoring resumed.'
        ];
        fallBtn.addEventListener('click', () => {
          step = (step + 1) % states.length;
          fallStatus.textContent = states[step];
          fallStatus.style.color = (step === 1 || step === 2) ? 'var(--co)' : 'var(--gr)';
        });
      }

      // 5. Memory Quiz Interactive Demo
      const quizOpts = document.querySelectorAll('.quiz-opt');
      const quizFeedback = document.getElementById('quiz-feedback');
      quizOpts.forEach(opt => {
        opt.addEventListener('click', () => {
          const isCorrect = opt.dataset.correct === 'true';
          quizFeedback.style.display = 'block';
          if (isCorrect) {
            quizFeedback.textContent = 'Correct!';
            quizFeedback.style.color = 'var(--gr)';
            opt.style.borderColor = 'var(--gr)';
            opt.style.background = 'rgba(43,181,138,0.1)';
          } else {
            quizFeedback.textContent = 'Not quite, try again.';
            quizFeedback.style.color = 'var(--co)';
            opt.style.borderColor = 'var(--co)';
          }
        });
      });

      // 6. Chips selection for forms
      document.querySelectorAll('.chips-group').forEach(group => {
        group.querySelectorAll('.chip-item').forEach(chip => {
          chip.addEventListener('click', () => {
            group.querySelectorAll('.chip-item').forEach(c => c.classList.remove('selected'));
            chip.classList.add('selected');
          });
        });
      });

      // 7. Contact Form Simulation
      const contactForm = document.getElementById('contact-form');
      if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
          e.preventDefault();
          const name = document.getElementById('c-name').value.trim();
          const email = document.getElementById('c-email').value.trim();
          const fb = document.getElementById('c-feedback');
          if (!name || !email) {
            fb.textContent = 'Please fill in required fields.';
            fb.style.color = 'var(--co)';
            fb.style.display = 'block';
            return;
          }
          fb.textContent = 'Sending…';
          fb.style.color = 'var(--te)';
          fb.style.display = 'block';
          setTimeout(() => {
            fb.textContent = 'Thank you. Your enquiry has been sent.';
            fb.style.color = 'var(--gr)';
            contactForm.reset();
          }, 600);
        });
      }

      // 8. Demo Request Form Simulation
      const demoForm = document.getElementById('demo-form');
      if (demoForm) {
        demoForm.addEventListener('submit', (e) => {
          e.preventDefault();
          const name = document.getElementById('d-name').value.trim();
          const email = document.getElementById('d-email').value.trim();
          const fb = document.getElementById('d-feedback');
          if (!name || !email) {
            fb.textContent = 'Please fill in required fields.';
            fb.style.color = 'var(--co)';
            fb.style.display = 'block';
            return;
          }
          fb.textContent = 'Sending…';
          fb.style.color = 'var(--te)';
          fb.style.display = 'block';
          setTimeout(() => {
            fb.textContent = 'Thank you. Your demo request has been sent.';
            fb.style.color = 'var(--gr)';
            demoForm.reset();
          }, 600);
        });
      }
    });
  </script>
</body>
</html>
'''

with open(r'D:\Neuromates(website)\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Saved unified single-URL application into D:\\Neuromates(website)\\index.html")

