for path in [r"D:\Neuromates(website)\index.html", r"D:\Neuromates(website)\neuromates-products.html", r"D:\Neuromates(website)\assets\js\shared.js"]:
    with open(path, "r", encoding="utf-8") as f:
        t = f.read()
    import re
    logos = re.findall(r'<a[^>]*class="[^"]*l[go][^"]*"[^>]*>.*?</a>', t, re.DOTALL)
    print(path)
    for l in logos[:5]:
        print("  ", l[:120])

