with open(r"D:\Neuromates(website)\technology\connected-devices.html", "r", encoding="utf-8") as f:
    t = f.read()

import html.parser
class Checker(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.errors = []
    def handle_starttag(self, tag, attrs):
        if tag not in ['img', 'br', 'hr', 'input', 'meta', 'link']:
            self.tags.append(tag)
    def handle_endtag(self, tag):
        if tag in ['img', 'br', 'hr', 'input', 'meta', 'link']:
            return
        if self.tags and self.tags[-1] == tag:
            self.tags.pop()
        else:
            self.errors.append((tag, list(self.tags[-5:])))

c = Checker()
c.feed(t)
print("Errors in connected-devices.html:", c.errors)
print("Unmatched tags count:", len(c.tags))

