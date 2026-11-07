import glob, re

files = [
    r"D:\Neuromates(website)\neuromates-products.html",
    r"D:\Neuromates(website)\Products _ Neuro Mates.html",
    r"D:\Neuromates(website)\products.html",
    r"D:\Neuromates(website)\index.html",
    r"D:\Neuromates(website)\neuromates-home.html",
    r"D:\Neuromates(website)\Neuro Mates _ Connected neurological care.html"
]

for f in files:
    with open(f, "r", encoding="utf-8") as fp:
        c = fp.read()

    # Fix logo links pointing to claude
    c = c.replace('href="https://claude.ai/artifact/B8BZvrw4J21xwsmHS9aegH" target="_blank" rel="noopener"', 'href="index.html" aria-label="Neuro Mates Home"')
    c = c.replace("href='https://claude.ai/artifact/B8BZvrw4J21xwsmHS9aegH' target='_blank' rel='noopener'", 'href="index.html" aria-label="Neuro Mates Home"')
    c = c.replace('href="https://claude.ai/artifact/B8BZvrw4J21xwsmHS9aegH"', 'href="index.html"')

    # Fix product card links pointing to claude
    c = c.replace('href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#overview" target="_blank" rel="noopener"', 'href="neuromates-products.html#overview"')
    c = c.replace('href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#parkinsons-care" target="_blank" rel="noopener"', 'href="neuromates-products.html#parkinsons-care"')
    c = c.replace('href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#alzheimers-care" target="_blank" rel="noopener"', 'href="neuromates-products.html#alzheimers-care"')
    c = c.replace('href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#epilepsy-care" target="_blank" rel="noopener"', 'href="neuromates-products.html#epilepsy-care"')
    c = c.replace('href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#paralysis-care" target="_blank" rel="noopener"', 'href="neuromates-products.html#paralysis-care"')

    c = c.replace('href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#overview"', 'href="neuromates-products.html#overview"')
    c = c.replace('href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#parkinsons-care"', 'href="neuromates-products.html#parkinsons-care"')
    c = c.replace('href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#alzheimers-care"', 'href="neuromates-products.html#alzheimers-care"')
    c = c.replace('href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#epilepsy-care"', 'href="neuromates-products.html#epilepsy-care"')
    c = c.replace('href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#paralysis-care"', 'href="neuromates-products.html#paralysis-care"')

    # Fix home page logo href="#" to href="index.html"
    c = re.sub(r'<a class="lg" href="#">', '<a class="lg" href="index.html" aria-label="Neuro Mates Home">', c)

    with open(f, "w", encoding="utf-8") as fp:
        fp.write(c)
    print(f"Purged claude links from: {f}")

print("All claude.ai links successfully replaced with internal routes!")

