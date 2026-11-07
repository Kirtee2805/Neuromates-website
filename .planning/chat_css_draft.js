/* Neuro Mates AI Frontend Chat Widget Styles */
const chatWidgetCSS = `
  /* Chat Launcher Floating Button */
  #neuro-chat-launcher {
    position: fixed;
    bottom: 24px;
    right: 24px;
    width: 62px;
    height: 62px;
    border-radius: 50%;
    background: linear-gradient(135deg, #0B7A7C 0%, #0E3B43 100%);
    box-shadow: 0 10px 30px rgba(11, 122, 124, 0.4), 0 4px 12px rgba(14, 59, 67, 0.25);
    border: 2px solid rgba(255, 255, 255, 0.35);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    z-index: 99999;
    transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.3s ease;
    color: #FFFFFF;
    outline: none;
  }
  #neuro-chat-launcher:hover {
    transform: scale(1.08) translateY(-2px);
    box-shadow: 0 16px 36px rgba(11, 122, 124, 0.5), 0 6px 16px rgba(14, 59, 67, 0.3);
  }
  #neuro-chat-launcher svg {
    width: 28px;
    height: 28px;
    fill: currentColor;
    transition: transform 0.3s ease;
  }
  #neuro-chat-launcher.open svg {
    transform: rotate(90deg) scale(0.9);
  }
  .neuro-chat-badge {
    position: absolute;
    top: -2px;
    right: -2px;
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background: #FF5A5F;
    color: #FFFFFF;
    font: 700 11px system-ui, sans-serif;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 2px 6px rgba(255, 90, 95, 0.5);
    border: 2px solid #FFFFFF;
    animation: chatBadgePulse 2.4s infinite;
  }
  @keyframes chatBadgePulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.2); }
  }

  /* Chat Window Container */
  #neuro-chat-window {
    position: fixed;
    bottom: 96px;
    right: 24px;
    width: 380px;
    max-width: calc(100vw - 32px);
    height: 580px;
    max-height: calc(100vh - 120px);
    background: #FFFFFF;
    border-radius: 28px;
    box-shadow: 0 24px 70px rgba(14, 59, 67, 0.22), 0 8px 24px rgba(14, 59, 67, 0.12);
    border: 1px solid rgba(14, 59, 67, 0.1);
    display: flex;
    flex-direction: column;
    overflow: hidden;
    z-index: 99999;
    opacity: 0;
    pointer-events: none;
    transform: translateY(20px) scale(0.96);
    transform-origin: bottom right;
    transition: opacity 0.35s cubic-bezier(0.16, 1, 0.3, 1), transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
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
    width: 40px;
    height: 40px;
    border-radius: 12px;
    background: #FFFFFF;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 3px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
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
    font-size: 0.96rem;
    font-weight: 700;
    color: #FFFFFF;
    letter-spacing: -0.01em;
  }
  .neuro-chat-status {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 0.74rem;
    color: #A3E3DE;
    margin-top: 2px;
    font-weight: 500;
  }
  .neuro-chat-status-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #5BE7C4;
    box-shadow: 0 0 8px #5BE7C4;
    display: inline-block;
  }
  .neuro-chat-close-btn {
    background: rgba(255, 255, 255, 0.15);
    border: none;
    color: #FFFFFF;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    transition: background 0.2s;
  }
  .neuro-chat-close-btn:hover {
    background: rgba(255, 255, 255, 0.3);
  }

  /* Chat Messages Scroll Container */
  .neuro-chat-body {
    flex: 1;
    overflow-y: auto;
    -webkit-overflow-scrolling: touch;
    padding: 18px 16px;
    display: flex;
    flex-direction: column;
    gap: 12px;
    background: #F8F9FA;
  }

  /* Chat Message Bubbles */
  .neuro-chat-msg {
    display: flex;
    gap: 10px;
    max-width: 86%;
    animation: chatMsgAppear 0.3s ease-out forwards;
  }
  @keyframes chatMsgAppear {
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
    width: 30px;
    height: 30px;
    border-radius: 50%;
    background: #FFFFFF;
    box-shadow: 0 2px 8px rgba(14, 59, 67, 0.12);
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 3px;
    flex-shrink: 0;
  }
  .neuro-chat-avatar img {
    width: 100%;
    height: 100%;
    object-fit: contain;
  }
  .neuro-chat-bubble {
    padding: 12px 16px;
    border-radius: 18px;
    font-size: 0.9rem;
    line-height: 1.45;
  }
  .neuro-chat-msg.bot .neuro-chat-bubble {
    background: #FFFFFF;
    color: #0E3B43;
    border-bottom-left-radius: 4px;
    box-shadow: 0 2px 10px rgba(14, 59, 67, 0.06);
    border: 1px solid rgba(14, 59, 67, 0.07);
  }
  .neuro-chat-msg.user .neuro-chat-bubble {
    background: linear-gradient(135deg, #0B7A7C 0%, #0E3B43 100%);
    color: #FFFFFF;
    border-bottom-right-radius: 4px;
    box-shadow: 0 4px 12px rgba(11, 122, 124, 0.25);
  }
  .neuro-chat-time {
    font-size: 0.68rem;
    color: #8C9EA1;
    margin-top: 4px;
    display: block;
    text-align: right;
  }

  /* Quick Suggestion Chips */
  .neuro-chat-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 4px;
  }
  .neuro-chat-chip {
    background: #FFFFFF;
    color: #0B7A7C;
    border: 1px solid rgba(11, 122, 124, 0.25);
    border-radius: 99px;
    padding: 6px 12px;
    font-size: 0.78rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
    box-shadow: 0 2px 6px rgba(14, 59, 67, 0.04);
  }
  .neuro-chat-chip:hover {
    background: #0B7A7C;
    color: #FFFFFF;
    border-color: #0B7A7C;
    transform: translateY(-1px);
    box-shadow: 0 4px 10px rgba(11, 122, 124, 0.2);
  }

  /* Action Buttons inside Bot Message */
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

  /* Chat Footer & Input */
  .neuro-chat-footer {
    padding: 12px 14px;
    background: #FFFFFF;
    border-top: 1px solid rgba(14, 59, 67, 0.08);
  }
  .neuro-chat-form {
    display: flex;
    gap: 8px;
    align-items: center;
  }
  .neuro-chat-input {
    flex: 1;
    border: 1px solid rgba(14, 59, 67, 0.16);
    border-radius: 99px;
    padding: 10px 16px;
    font-size: 16px; /* 16px prevents iOS Safari auto-zoom! */
    outline: none;
    color: #0E3B43;
    transition: border-color 0.2s, box-shadow 0.2s;
  }
  .neuro-chat-input:focus {
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

  /* Mobile Responsive for iPhone and Android */
  @media (max-width: 480px) {
    #neuro-chat-launcher {
      bottom: 16px;
      right: 16px;
      width: 56px;
      height: 56px;
    }
    #neuro-chat-window {
      bottom: 82px;
      right: 12px;
      left: 12px;
      width: auto;
      max-width: none;
      height: 520px;
      max-height: calc(100vh - 100px);
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

