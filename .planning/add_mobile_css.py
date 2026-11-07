with open(r'D:\Neuromates(website)\assets\css\tokens.css', 'r', encoding='utf-8') as f:
    css = f.read()

mobile_additions = '''
/* --- Mobile Responsive Enhancements (Down to 360px) --- */
@media (max-width: 480px) {
  nav#nav {
    width: calc(100% - 16px);
    height: 58px;
    padding: 0 8px 0 14px;
  }
  nav .lg img {
    height: 32px;
  }
  #mb {
    padding: 6px 14px;
    font-size: 0.72rem;
  }
  .w, .w-narrow {
    padding: 0 16px;
  }
  .breadcrumb {
    font-size: 0.74rem;
    flex-wrap: wrap;
    gap: 6px;
  }
  .bt-group {
    flex-direction: column;
    width: 100%;
    gap: 12px;
  }
  .bt-group .btn,
  .bt-group .b2 {
    width: 100%;
    text-align: center;
  }
  .cta .bt {
    flex-direction: column;
    width: 100%;
    gap: 12px;
  }
  .cta .bt .btn,
  .cta .bt .b2 {
    width: 100%;
  }
  footer .fn {
    flex-direction: column;
    gap: 12px;
  }
  footer a.top {
    width: 100%;
    justify-content: center;
  }
}
'''

if '/* --- Mobile Responsive Enhancements (Down to 360px) --- */' not in css:
    css += mobile_additions
    with open(r'D:\Neuromates(website)\assets\css\tokens.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Added mobile responsive enhancements to tokens.css")
else:
    print("Already present in tokens.css")

