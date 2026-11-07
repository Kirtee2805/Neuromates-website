import glob

root_htmls = [
    r"D:\Neuromates(website)\index.html",
    r"D:\Neuromates(website)\neuromates-home.html",
    r"D:\Neuromates(website)\neuromates-products.html",
    r"D:\Neuromates(website)\products.html",
    r"D:\Neuromates(website)\Products _ Neuro Mates.html",
    r"D:\Neuromates(website)\Neuro Mates _ Connected neurological care.html"
]

tag = '<script src="assets/js/chat-widget.js" async></script>\n</body>'

for path in root_htmls:
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()
    if "chat-widget.js" in c:
        print(f"Already has chat-widget.js: {path}")
        continue
    
    if "</body>" in c:
        c = c.replace("</body>", tag)
        with open(path, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"Added chat-widget.js to: {path}")
    else:
        print(f"No </body> in: {path}")

print("Chat widget added to all root pages!")

