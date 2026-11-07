with open(r"D:\Neuromates(website)\neuromates-products.html", "r", encoding="utf-8") as f:
    t = f.read()

# Let's inspect the entire #v-alzheimers-care element and all its children
pos_start = t.find('<div class="pv" id="v-alzheimers-care">')
pos_end = t.find('<div class="pv" id="v-epilepsy-care">')
print(f"Alzheimer section: start={pos_start}, end={pos_end}, len={pos_end - pos_start}")
alz_html = t[pos_start:pos_end]

# Check if there are any broken tags
import html.parser
class Checker(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.errors = []
    def handle_starttag(self, tag, attrs):
        if tag not in ['img', 'br', 'hr', 'input']:
            self.tags.append(tag)
    def handle_endtag(self, tag):
        if tag in ['img', 'br', 'hr', 'input']:
            return
        if self.tags and self.tags[-1] == tag:
            self.tags.pop()
        else:
            self.errors.append((tag, list(self.tags[-5:])))

c = Checker()
c.feed(alz_html)
print("Unmatched tags count in alz_html:", len(c.tags))
print("Errors in alz_html:", c.errors[:10])
print("Remaining unclosed tags:", c.tags)

