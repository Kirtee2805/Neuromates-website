for path in [r"D:\Neuromates(website)\products.html", r"D:\Neuromates(website)\Products _ Neuro Mates.html"]:
    with open(path, "r", encoding="utf-8") as f:
        t = f.read()

    import html.parser
    class DocChecker(html.parser.HTMLParser):
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

    c = DocChecker()
    c.feed(t)
    print(path, "-> Errors:", c.errors, "Unmatched tags count:", len(c.tags))

