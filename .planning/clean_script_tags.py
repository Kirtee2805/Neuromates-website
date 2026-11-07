import os

tech_dir = r'D:\Neuromates(website)\technology'
for fn in os.listdir(tech_dir):
    if fn.endswith('.html'):
        fp = os.path.join(tech_dir, fn)
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()
        if '<script src="../assets/js/tokens.css"></script>' in content:
            content = content.replace('<script src="../assets/js/tokens.css"></script>\n', '')
            content = content.replace('<script src="../assets/js/tokens.css"></script>', '')
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Cleaned up script tag in {fn}")

