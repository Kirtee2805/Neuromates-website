import os

files = [
    r'D:\Neuromates(website)\index.html',
    r'D:\Neuromates(website)\neuromates-home.html',
    r'D:\Neuromates(website)\neuromates-products.html',
    r'D:\Neuromates(website)\products.html'
]

old_dropdown = '<li class="dd"><a href="insights/index.html">Insights</a><div><a href="insights/index.html">Insights Overview</a><a href="insights/research.html">Research</a><a href="insights/articles.html">Articles</a><a href="insights/case-studies.html">Case Studies</a><a href="insights/resources.html">Resources</a></div></li>'
new_dropdown = '<li class="dd"><a href="insights/index.html">Insights</a><div><a href="insights/index.html">Insights Overview</a><a href="insights/research.html">Research</a><a href="insights/resources.html">Resources</a></div></li>'

for fp in files:
    if os.path.exists(fp):
        with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        if old_dropdown in content:
            content = content.replace(old_dropdown, new_dropdown)
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated dropdown in {os.path.basename(fp)}")
        else:
            print(f"Old dropdown not found directly in {os.path.basename(fp)}")

