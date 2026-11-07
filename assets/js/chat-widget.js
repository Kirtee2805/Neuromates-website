/**
 * NEURO MATES — Official Healthcare AI Chat Widget (Frontend UI)
 * Built as a pure, decoupled frontend UI ready for custom RAG backend integration.
 * Features official Neuro Mates brain logo launcher, pre-messages, suggestion chips,
 * and 100% mobile/iPhone responsiveness.
 */

(function () {
  'use strict';

  // Prevent multiple initializations
  if (window.NeuroChatInitialized) return;
  window.NeuroChatInitialized = true;

  // Determine root path prefix based on directory depth
  const path = window.location.pathname.replace(/\\/g, '/');
  const isSubdir = path.includes('/technology/') || path.includes('/insights/') || path.includes('/about/') || path.includes('/products/');
  const root = isSubdir ? '../' : './';
  const logoUrl = `${root}assets/images/logo.png`;
  const logoIconUrl = `${root}assets/images/logo-icon.png`;

  // Global RAG API Hook for custom backend connection
  // User can define: window.NeuroChatAPI = async function(userMessage) { return "RAG response..."; }
  if (typeof window.NeuroChatAPI === 'undefined') {
    window.NeuroChatAPI = null;
  }

  // Inject CSS Styles
  const styleEl = document.createElement('style');
  styleEl.id = 'neuro-chat-widget-styles';
  styleEl.textContent = `
    /* Chat Launcher Floating Button with Official Neuro Mates Logo */
    #neuro-chat-launcher {
      position: fixed;
      bottom: 24px;
      right: 24px;
      width: 64px;
      height: 64px;
      border-radius: 50%;
      background: #FFFFFF;
      box-shadow: 0 10px 30px rgba(11, 122, 124, 0.35), 0 4px 14px rgba(14, 59, 67, 0.2);
      border: 2.5px solid #0B7A7C;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      z-index: 99999;
      transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.3s ease, border-color 0.2s ease;
      outline: none;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }
    #neuro-chat-launcher:hover {
      transform: scale(1.08) translateY(-2px);
      box-shadow: 0 16px 36px rgba(11, 122, 124, 0.45), 0 6px 18px rgba(14, 59, 67, 0.25);
      border-color: #0E3B43;
    }
    #neuro-chat-launcher .icon-launcher-logo {
      width: 40px;
      height: 40px;
      object-fit: contain;
      border-radius: 50%;
      transition: transform 0.3s ease, opacity 0.2s ease;
      pointer-events: none;
    }
    #neuro-chat-launcher.open .icon-launcher-logo {
      display: none;
    }
    #neuro-chat-launcher .icon-launcher-close {
      display: none;
      width: 26px;
      height: 26px;
      fill: #0B7A7C;
      transition: transform 0.3s ease;
    }
    #neuro-chat-launcher.open .icon-launcher-close {
      display: block;
      transform: rotate(90deg);
    }
    .neuro-chat-badge {
      position: absolute;
      top: -3px;
      right: -3px;
      width: 20px;
      height: 20px;
      border-radius: 50%;
      background: #FF5A5F;
      color: #FFFFFF;
      font: 700 11px system-ui, -apple-system, sans-serif;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 2px 6px rgba(255, 90, 95, 0.5);
      border: 2px solid #FFFFFF;
      animation: chatBadgePulse 2.4s infinite;
    }
    @keyframes chatBadgePulse {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.18); }
    }

    /* Chat Window Container */
    #neuro-chat-window {
      position: fixed;
      bottom: 98px;
      right: 24px;
      width: 384px;
      max-width: calc(100vw - 32px);
      height: 580px;
      max-height: calc(100vh - 120px);
      background: #FFFFFF;
      border-radius: 28px;
      box-shadow: 0 24px 70px rgba(14, 59, 67, 0.22), 0 8px 24px rgba(14, 59, 67, 0.12);
      border: 1px solid rgba(14, 59, 67, 0.12);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      z-index: 99999;
      opacity: 0;
      pointer-events: none;
      transform: translateY(20px) scale(0.96);
      transform-origin: bottom right;
      transition: opacity 0.32s cubic-bezier(0.16, 1, 0.3, 1), transform 0.32s cubic-bezier(0.16, 1, 0.3, 1);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    #neuro-chat-window.open {
      opacity: 1;
      pointer-events: auto;
      transform: translateY(0) scale(1);
    }

    /* Chat Header */
    .neuro-chat-header {
      background: linear-gradient(135deg, #0E3B43 0%, #0B7A7C 100%);
      color: #FFFFFF;
      padding: 16px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
      position: relative;
    }
    .neuro-chat-header-brand {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .neuro-chat-logo-wrap {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 4px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.16);
      flex-shrink: 0;
    }
    .neuro-chat-logo-wrap img {
      width: 100%;
      height: auto;
      max-height: 100%;
      object-fit: contain;
    }
    .neuro-chat-title-group h3 {
      margin: 0;
      font-size: 1.02rem;
      font-weight: 700;
      letter-spacing: -0.01em;
      color: #FFFFFF;
    }
    .neuro-chat-status {
      display: flex;
      align-items: center;
      gap: 6px;
      margin-top: 3px;
      font-size: 0.74rem;
      opacity: 0.92;
      color: #C2ECE8;
    }
    .neuro-chat-status-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #5BE7C4;
      box-shadow: 0 0 8px #5BE7C4;
      animation: chatOnlinePulse 2s infinite;
    }
    @keyframes chatOnlinePulse {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.6; transform: scale(0.9); }
    }
    .neuro-chat-close-btn {
      background: rgba(255, 255, 255, 0.12);
      border: none;
      color: #FFFFFF;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 1.25rem;
      line-height: 1;
      transition: background 0.2s;
      outline: none;
    }
    .neuro-chat-close-btn:hover {
      background: rgba(255, 255, 255, 0.25);
    }

    /* Chat Messages Body */
    .neuro-chat-body {
      flex: 1;
      padding: 16px 14px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 14px;
      background: #F8FAF9;
      scroll-behavior: smooth;
      -webkit-overflow-scrolling: touch;
    }
    .neuro-chat-msg {
      display: flex;
      gap: 10px;
      max-width: 88%;
      animation: chatMsgFadeIn 0.28s ease-out;
    }
    @keyframes chatMsgFadeIn {
      from { opacity: 0; transform: translateY(8px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .neuro-chat-msg.bot {
      align-self: flex-start;
    }
    .neuro-chat-msg.user {
      align-self: flex-end;
      flex-direction: row-reverse;
    }
    .neuro-chat-avatar {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      background: #FFFFFF;
      border: 1px solid rgba(11, 122, 124, 0.2);
      box-shadow: 0 2px 6px rgba(14, 59, 67, 0.08);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      padding: 2px;
    }
    .neuro-chat-avatar img {
      width: 85%;
      height: 85%;
      object-fit: contain;
    }
    .neuro-chat-bubble {
      padding: 11px 15px;
      border-radius: 18px;
      font-size: 0.88rem;
      line-height: 1.45;
      word-break: break-word;
    }
    .neuro-chat-msg.bot .neuro-chat-bubble {
      background: #FFFFFF;
      color: #0E3B43;
      border-bottom-left-radius: 4px;
      box-shadow: 0 3px 12px rgba(14, 59, 67, 0.06);
      border: 1px solid rgba(14, 59, 67, 0.06);
    }
    .neuro-chat-msg.user .neuro-chat-bubble {
      background: #0B7A7C;
      color: #FFFFFF;
      border-bottom-right-radius: 4px;
      box-shadow: 0 3px 12px rgba(11, 122, 124, 0.25);
    }
    .neuro-chat-time {
      font-size: 0.68rem;
      color: #8C9EA1;
      margin-top: 4px;
      display: block;
    }
    .neuro-chat-msg.user .neuro-chat-time {
      text-align: right;
    }

    /* Suggestion Chips */
    .neuro-chat-chips {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 8px;
    }
    .neuro-chat-chip {
      background: #FFFFFF;
      color: #0B7A7C;
      border: 1px solid rgba(11, 122, 124, 0.3);
      border-radius: 99px;
      padding: 6px 12px;
      font-size: 0.77rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
      box-shadow: 0 2px 6px rgba(14, 59, 67, 0.04);
      -webkit-tap-highlight-color: transparent;
    }
    .neuro-chat-chip:hover,
    .neuro-chat-chip:active {
      background: #0B7A7C;
      color: #FFFFFF;
      border-color: #0B7A7C;
      transform: translateY(-1px);
      box-shadow: 0 4px 10px rgba(11, 122, 124, 0.2);
    }

    /* Action Link Button inside Bot Message */
    .neuro-chat-btn-link {
      display: inline-block;
      margin-top: 8px;
      padding: 6px 14px;
      background: #0B7A7C;
      color: #FFFFFF !important;
      font-size: 0.8rem;
      font-weight: 700;
      border-radius: 8px;
      text-decoration: none;
      transition: background 0.2s;
    }
    .neuro-chat-btn-link:hover {
      background: #0E3B43;
    }

    /* Typing Indicator */
    .neuro-chat-typing {
      display: flex;
      align-items: center;
      gap: 4px;
      padding: 10px 14px;
      background: #FFFFFF;
      border-radius: 16px;
      border-bottom-left-radius: 4px;
      box-shadow: 0 2px 8px rgba(14, 59, 67, 0.06);
      width: fit-content;
    }
    .neuro-chat-typing span {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: #0B7A7C;
      opacity: 0.4;
      animation: typingBounce 1.4s infinite ease-in-out;
    }
    .neuro-chat-typing span:nth-child(2) { animation-delay: 0.2s; }
    .neuro-chat-typing span:nth-child(3) { animation-delay: 0.4s; }
    @keyframes typingBounce {
      0%, 60%, 100% { transform: translateY(0); opacity: 0.4; }
      30% { transform: translateY(-4px); opacity: 1; }
    }

    /* Chat Footer & Input (16px prevents iOS auto-zoom) */
    .neuro-chat-footer {
      padding: 12px 14px;
      background: #FFFFFF;
      border-top: 1px solid rgba(14, 59, 67, 0.08);
      padding-bottom: max(12px, env(safe-area-inset-bottom));
    }
    .neuro-chat-form {
      display: flex;
      gap: 8px;
      align-items: center;
    }
    .neuro-chat-input {
      flex: 1;
      border: 1px solid rgba(14, 59, 67, 0.18);
      border-radius: 99px;
      padding: 10px 16px;
      font-size: 16px; /* 16px prevents iOS Safari auto-zoom! */
      outline: none;
      color: #0E3B43;
      transition: border-color 0.2s, box-shadow 0.2s;
      background: #FAFAFC;
    }
    .neuro-chat-input:focus {
      background: #FFFFFF;
      border-color: #0B7A7C;
      box-shadow: 0 0 0 3px rgba(11, 122, 124, 0.15);
    }
    .neuro-chat-send {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: #0B7A7C;
      border: none;
      color: #FFFFFF;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: background 0.2s, transform 0.2s;
      flex-shrink: 0;
      outline: none;
    }
    .neuro-chat-send:hover {
      background: #0E3B43;
      transform: scale(1.05);
    }
    .neuro-chat-disclaimer {
      font-size: 0.68rem;
      color: #8C9EA1;
      text-align: center;
      margin-top: 6px;
    }

    /* Mobile / iPhone Optimization */
    @media (max-width: 480px) {
      #neuro-chat-launcher {
        bottom: 18px;
        right: 18px;
        width: 58px;
        height: 58px;
      }
      #neuro-chat-launcher .icon-launcher-logo {
        width: 36px;
        height: 36px;
      }
      #neuro-chat-window {
        bottom: 84px;
        right: 12px;
        left: 12px;
        width: auto;
        max-width: none;
        height: 520px;
        max-height: calc(100vh - 105px);
        border-radius: 22px;
      }
      .neuro-chat-header {
        padding: 14px 16px;
      }
      .neuro-chat-body {
        padding: 14px 12px;
      }
    }
  `;
  document.head.appendChild(styleEl);

  // Helper to format current time
  function formatTime() {
    const d = new Date();
    let h = d.getHours();
    let m = d.getMinutes();
    const ampm = h >= 12 ? 'PM' : 'AM';
    h = h % 12 || 12;
    m = m < 10 ? '0' + m : m;
    return `${h}:${m} ${ampm}`;
  }

  // Frontend Knowledge Base Fallbacks (Used if custom RAG backend is not yet hooked)
  const fallbackKnowledge = {
    parkinsons: {
      text: "<b>Parkinson’s Care:</b> Our system utilizes a lightweight wearable motion sensor worn on the back of the hand. It provides continuous tremor monitoring and immediate fall detection, sending real-time automated alerts to designated family members and caregivers via WhatsApp and phone.",
      link: `${root}neuromates-products.html#parkinsons-care`,
      linkText: "View Parkinson’s Details →"
    },
    alzheimers: {
      text: "<b>Alzheimer’s Care:</b> Features an arm-worn location tracker paired with a configurable <b>1 km safe-zone geofence</b>. If the patient moves beyond the safe boundary, automated alerts and calls are dispatched immediately. The system also logs daily activities to generate personalized memory recall quizzes.",
      link: `${root}neuromates-products.html#alzheimers-care`,
      linkText: "Explore Alzheimer’s Care →"
    },
    epilepsy: {
      text: "<b>Epilepsy Care:</b> Our epilepsy monitoring wearable is an ergonomic headband equipped with continuous brain-activity (EEG) and heart-rate sensing. It actively observes brain activity for <em>abnormal EEG signals that may indicate a seizure</em>, keeping caregivers informed without delay.",
      link: `${root}neuromates-products.html#epilepsy-care`,
      linkText: "View Epilepsy Wearable →"
    },
    paralysis: {
      text: "<b>Paralysis Rehabilitation:</b> Designed for motor recovery, Neuro Mates pairs non-invasive <b>BioAmp EMG muscle sensors</b> and facial-expression tracking with interactive, game-based rehabilitation exercises for facial, hand and leg motor function.",
      link: `${root}neuromates-products.html#paralysis-care`,
      linkText: "View Rehabilitation System →"
    },
    platform: {
      text: "<b>Connected Care Platform:</b> Neuro Mates connects 4 synchronized portals around the central cloud platform: <b>Patient</b> (vitals & activities), <b>Caretaker</b> (alerts & safety), <b>Doctor</b> (clinical telemetry & trends), and <b>Admin</b> (fleet & safe-zone management).",
      link: `${root}technology/connected-care-platform.html`,
      linkText: "Explore Ecosystem Architecture →"
    },
    demo: {
      text: "<b>Book a Live Demonstration:</b> We would be delighted to showcase how the Neuro Mates care ecosystem functions. You can request a live demonstration for your hospital, clinic, or family.",
      link: `${root}register-demo.html`,
      linkText: "Register for a Demo →"
    },
    default: {
      text: "Neuro Mates is an AI and IoT connected care ecosystem supporting <b>Parkinson’s, Alzheimer’s, Epilepsy, and Paralysis</b>. We bridge the gap between clinical appointments through continuous monitoring, smart alerts, and role-based care portals.",
      link: `${root}neuromates-products.html#overview`,
      linkText: "Explore Products →"
    }
  };

  // Build DOM Structure
  function initChatDOM() {
    // 1. Launcher Button with Official Neuro Mates Logo
    const launcher = document.createElement('button');
    launcher.id = 'neuro-chat-launcher';
    launcher.setAttribute('aria-label', 'Open Neuro Mates Care Chat');
    launcher.innerHTML = `
      <img src="${logoIconUrl}" class="icon-launcher-logo" alt="Neuro Mates Logo">
      <svg class="icon-launcher-close" viewBox="0 0 24 24"><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg>
      <span class="neuro-chat-badge">1</span>
    `;

    // 2. Chat Window
    const win = document.createElement('div');
    win.id = 'neuro-chat-window';
    win.setAttribute('role', 'dialog');
    win.setAttribute('aria-label', 'Neuro Mates Virtual Care Assistant');
    win.innerHTML = `
      <div class="neuro-chat-header">
        <div class="neuro-chat-header-brand">
          <div class="neuro-chat-logo-wrap">
            <img src="${logoUrl}" alt="Neuro Mates Logo">
          </div>
          <div class="neuro-chat-title-group">
            <h3>Neuro Mates Assistant</h3>
            <div class="neuro-chat-status">
              <span class="neuro-chat-status-dot"></span>
              <span>Online &bull; Healthcare AI</span>
            </div>
          </div>
        </div>
        <button class="neuro-chat-close-btn" id="neuro-chat-close" aria-label="Close Chat">&times;</button>
      </div>

      <div class="neuro-chat-body" id="neuro-chat-messages">
        <!-- Pre-Messages from Bot -->
        <div class="neuro-chat-msg bot">
          <div class="neuro-chat-avatar">
            <img src="${logoIconUrl}" alt="Neuro Mates">
          </div>
          <div>
            <div class="neuro-chat-bubble">
              Hello! Welcome to <b>Neuro Mates</b> — Connected Care Platform. 👋
            </div>
            <span class="neuro-chat-time">${formatTime()}</span>
          </div>
        </div>

        <div class="neuro-chat-msg bot">
          <div class="neuro-chat-avatar">
            <img src="${logoIconUrl}" alt="Neuro Mates">
          </div>
          <div>
            <div class="neuro-chat-bubble">
              I'm the Neuro Mates AI Care Assistant UI. How can I help you today? You can choose a quick topic below or type any question:
              <div class="neuro-chat-chips">
                <button type="button" class="neuro-chat-chip" data-topic="parkinsons">Parkinson’s Wearable</button>
                <button type="button" class="neuro-chat-chip" data-topic="alzheimers">Alzheimer’s Safe-Zone</button>
                <button type="button" class="neuro-chat-chip" data-topic="epilepsy">Epilepsy EEG Headband</button>
                <button type="button" class="neuro-chat-chip" data-topic="paralysis">Paralysis Rehabilitation</button>
                <button type="button" class="neuro-chat-chip" data-topic="platform">Connected Care Platform</button>
                <button type="button" class="neuro-chat-chip" data-topic="demo">Book a Live Demo →</button>
              </div>
            </div>
            <span class="neuro-chat-time">${formatTime()}</span>
          </div>
        </div>
      </div>

      <div class="neuro-chat-footer">
        <form class="neuro-chat-form" id="neuro-chat-form">
          <input type="text" class="neuro-chat-input" id="neuro-chat-input" placeholder="Ask about our care ecosystem..." autocomplete="off">
          <button type="submit" class="neuro-chat-send" aria-label="Send Message">
            <svg viewBox="0 0 24 24" width="18" height="18" fill="#FFFFFF"><path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/></svg>
          </button>
        </form>
        <div class="neuro-chat-disclaimer">
          Frontend RAG UI &bull; Neuro Mates Connected Care
        </div>
      </div>
    `;

    document.body.appendChild(launcher);
    document.body.appendChild(win);

    // Event Bindings
    const msgContainer = document.getElementById('neuro-chat-messages');
    const form = document.getElementById('neuro-chat-form');
    const input = document.getElementById('neuro-chat-input');
    const closeBtn = document.getElementById('neuro-chat-close');
    const badge = launcher.querySelector('.neuro-chat-badge');

    function toggleChat() {
      const isOpen = win.classList.toggle('open');
      launcher.classList.toggle('open', isOpen);
      if (badge && isOpen) {
        badge.style.display = 'none';
      }
      if (isOpen) {
        setTimeout(() => input.focus(), 300);
      }
    }

    launcher.addEventListener('click', toggleChat);
    closeBtn.addEventListener('click', toggleChat);

    // Append User Message to UI
    function appendUserMessage(text) {
      const msg = document.createElement('div');
      msg.className = 'neuro-chat-msg user';
      msg.innerHTML = `
        <div>
          <div class="neuro-chat-bubble">${escapeHTML(text)}</div>
          <span class="neuro-chat-time">${formatTime()}</span>
        </div>
      `;
      msgContainer.appendChild(msg);
      msgContainer.scrollTop = msgContainer.scrollHeight;
    }

    // Append Bot Message to UI
    function appendBotMessage(htmlContent, linkUrl, linkText) {
      const msg = document.createElement('div');
      msg.className = 'neuro-chat-msg bot';
      let linkHtml = '';
      if (linkUrl && linkText) {
        linkHtml = `<div><a href="${linkUrl}" class="neuro-chat-btn-link">${escapeHTML(linkText)}</a></div>`;
      }
      msg.innerHTML = `
        <div class="neuro-chat-avatar">
          <img src="${logoIconUrl}" alt="Neuro Mates">
        </div>
        <div>
          <div class="neuro-chat-bubble">
            ${htmlContent}
            ${linkHtml}
          </div>
          <span class="neuro-chat-time">${formatTime()}</span>
        </div>
      `;
      msgContainer.appendChild(msg);
      msgContainer.scrollTop = msgContainer.scrollHeight;
    }

    // Append Typing Indicator
    function showTypingIndicator() {
      const typing = document.createElement('div');
      typing.id = 'neuro-chat-typing-indicator';
      typing.className = 'neuro-chat-msg bot';
      typing.innerHTML = `
        <div class="neuro-chat-avatar">
          <img src="${logoIconUrl}" alt="Neuro Mates">
        </div>
        <div class="neuro-chat-typing">
          <span></span><span></span><span></span>
        </div>
      `;
      msgContainer.appendChild(typing);
      msgContainer.scrollTop = msgContainer.scrollHeight;
      return typing;
    }

    function removeTypingIndicator() {
      const typing = document.getElementById('neuro-chat-typing-indicator');
      if (typing) typing.remove();
    }

    // Dispatches message to RAG or fallback engine
    async function handleUserSubmission(queryText, topicKey) {
      if (!queryText && !topicKey) return;

      if (topicKey) {
        // Quick Chip clicked
        const data = fallbackKnowledge[topicKey] || fallbackKnowledge.default;
        appendUserMessage(queryText);
        const typing = showTypingIndicator();
        setTimeout(() => {
          removeTypingIndicator();
          appendBotMessage(data.text, data.link, data.linkText);
        }, 500);
        return;
      }

      // User typed query
      appendUserMessage(queryText);
      const typing = showTypingIndicator();

      // Check if external RAG hook is connected
      if (typeof window.NeuroChatAPI === 'function') {
        try {
          const ragResult = await window.NeuroChatAPI(queryText);
          removeTypingIndicator();
          if (typeof ragResult === 'string') {
            appendBotMessage(ragResult);
          } else if (ragResult && ragResult.text) {
            appendBotMessage(ragResult.text, ragResult.link, ragResult.linkText);
          } else {
            appendBotMessage("Response received from connected RAG pipeline.");
          }
          return;
        } catch (err) {
          console.warn("[NeuroChat] Error executing external RAG API:", err);
          removeTypingIndicator();
          appendBotMessage("<em>RAG Pipeline notice: Awaiting connection response. Falling back to local intelligence...</em>");
        }
      }

      // Default UI Fallback Search
      setTimeout(() => {
        removeTypingIndicator();
        const lower = queryText.toLowerCase();
        let matched = fallbackKnowledge.default;

        if (lower.includes('parkinson') || lower.includes('tremor') || lower.includes('fall')) {
          matched = fallbackKnowledge.parkinsons;
        } else if (lower.includes('alzheimer') || lower.includes('safe') || lower.includes('geofence') || lower.includes('gps') || lower.includes('memory') || lower.includes('lost')) {
          matched = fallbackKnowledge.alzheimers;
        } else if (lower.includes('epilepsy') || lower.includes('seizure') || lower.includes('eeg') || lower.includes('brain')) {
          matched = fallbackKnowledge.epilepsy;
        } else if (lower.includes('paralysis') || lower.includes('rehab') || lower.includes('stroke') || lower.includes('muscle') || lower.includes('game') || lower.includes('bioamp')) {
          matched = fallbackKnowledge.paralysis;
        } else if (lower.includes('platform') || lower.includes('portal') || lower.includes('doctor') || lower.includes('patient') || lower.includes('admin') || lower.includes('caretaker')) {
          matched = fallbackKnowledge.platform;
        } else if (lower.includes('demo') || lower.includes('register') || lower.includes('book') || lower.includes('trial')) {
          matched = fallbackKnowledge.demo;
        }

        appendBotMessage(matched.text, matched.link, matched.linkText);
      }, 650);
    }

    // Form Submit
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const val = input.value.trim();
      if (!val) return;
      input.value = '';
      handleUserSubmission(val, null);
    });

    // Chips Delegate
    msgContainer.addEventListener('click', (e) => {
      const chip = e.target.closest('.neuro-chat-chip');
      if (chip) {
        const topic = chip.getAttribute('data-topic');
        const text = chip.textContent.trim();
        handleUserSubmission(text, topic);
      }
    });

    // Escape HTML helper
    function escapeHTML(str) {
      return str.replace(/[&<>'"]/g,
        tag => ({
          '&': '&amp;',
          '<': '&lt;',
          '>': '&gt;',
          "'": '&#39;',
          '"': '&quot;'
        }[tag] || tag)
      );
    }
  }

  // Initialize on DOM Ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initChatDOM);
  } else {
    initChatDOM();
  }
})();

window.NeuroChatAPI = async function (userMessage) {
  try {

    const response = await fetch('https://neuromates-rag.onrender.com/api/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },

      body: JSON.stringify({ question: userMessage })
    });

    if (!response.ok) {
      throw new Error(`Server returned status: ${response.status}`);
    }

    const data = await response.json();


    return data.answer || data.reply || "Sorry, I couldn't process an answer.";

  } catch (error) {
    console.error("NeuroMates RAG Connection Error:", error);
    return "Sorry, I am having trouble connecting to my brain right now. Please try again shortly!";
  }
};
