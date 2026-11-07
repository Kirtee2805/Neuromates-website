import re

targets = [
    r"D:\Neuromates(website)\neuromates-products.html",
    r"D:\Neuromates(website)\products.html",
    r"D:\Neuromates(website)\Products _ Neuro Mates.html"
]

pattern = re.compile(
    r'<div class="cardx r"><h3>Personalised memories</h3><p>.*?</section>',
    re.DOTALL
)

revert_block = """<div class="cardx r"><h3>Personalised memories</h3><p>Family members can upload photographs of loved ones, friends or relatives. The system can use these photographs to create personalised memory questions.</p><div class="ppl" aria-hidden="true"><i></i><i></i><i></i></div></div></div></section>"""

for target in targets:
    with open(target, "r", encoding="utf-8") as f:
        content = f.read()

    m = pattern.search(content)
    if m:
        content = content[:m.start()] + revert_block + content[m.end():]
        print(f"Reverted Personalised memories block cleanly in {target}")
    else:
        print(f"Pattern not found in {target}")

    with open(target, "w", encoding="utf-8") as f:
        f.write(content)

print("Finished reverting Personalised memories in all product pages.")

