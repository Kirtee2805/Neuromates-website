import re

def update_home_links(filepath, out_paths):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # Replace Claude artifact links and placeholders with real relative URLs
    # In navbar
    old_prod_nav = r'<a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#overview"[^>]*>Products</a><div><a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#overview"[^>]*>Products Overview</a><a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#parkinsons-care"[^>]*>Parkinson’s Care</a><a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#alzheimers-care"[^>]*>Alzheimer’s Care</a><a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#epilepsy-care"[^>]*>Epilepsy Care</a><a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#paralysis-care"[^>]*>Paralysis Care</a></div>'
    new_prod_nav = r'<a href="neuromates-products.html#overview">Products</a><div><a href="neuromates-products.html#overview">Products Overview</a><a href="neuromates-products.html#parkinsons-care">Parkinson’s Care</a><a href="neuromates-products.html#alzheimers-care">Alzheimer’s Care</a><a href="neuromates-products.html#epilepsy-care">Epilepsy Care</a><a href="neuromates-products.html#paralysis-care">Paralysis Care</a></div>'
    html = re.sub(old_prod_nav, new_prod_nav, html)

    old_tech_nav = r'<li class="dd"><a href="#">Technology</a><div><a href="#">Technology Overview</a><a href="#">Connected Devices</a><a href="#">AI &amp; Machine Learning</a><a href="#">Monitoring &amp; Analytics</a><a href="#">Connected Care Platform</a></div></li>'
    new_tech_nav = r'<li class="dd"><a href="technology/index.html">Technology</a><div><a href="technology/index.html">Technology Overview</a><a href="technology/connected-devices.html">Connected Devices</a><a href="technology/ai-machine-learning.html">AI &amp; Machine Learning</a><a href="technology/monitoring-analytics.html">Monitoring &amp; Analytics</a><a href="technology/connected-care-platform.html">Connected Care Platform</a></div></li>'
    html = html.replace(old_tech_nav, new_tech_nav)

    old_ins_nav = r'<li class="dd"><a href="#">Insights</a><div><a href="#">Insights Overview</a><a href="#">Research</a><a href="#">Articles</a><a href="#">Case Studies</a><a href="#">Resources</a></div></li>'
    new_ins_nav = r'<li class="dd"><a href="insights/index.html">Insights</a><div><a href="insights/index.html">Insights Overview</a><a href="insights/research.html">Research</a><a href="insights/articles.html">Articles</a><a href="insights/case-studies.html">Case Studies</a><a href="insights/resources.html">Resources</a></div></li>'
    html = html.replace(old_ins_nav, new_ins_nav)

    old_abt_nav = r'<li class="dd"><a href="#">About Us</a><div><a href="#">About Neuro Mates</a><a href="#">Vision &amp; Mission</a><a href="#">Our Approach</a><a href="#">Impact</a></div></li>'
    new_abt_nav = r'<li class="dd"><a href="about/index.html">About Us</a><div><a href="about/index.html">About Neuro Mates</a><a href="about/vision-mission.html">Vision &amp; Mission</a><a href="about/our-approach.html">Our Approach</a><a href="about/impact.html">Impact</a></div></li>'
    html = html.replace(old_abt_nav, new_abt_nav)

    html = html.replace('<li><a href="#">Contact Us</a></li>', '<li><a href="contact.html">Contact Us</a></li>')
    html = html.replace('<li><a class="btn" href="#">Register for a Demo</a></li>', '<li><a class="btn" href="register-demo.html">Register for a Demo</a></li>')
    html = html.replace('<a class="lg" href="#">', '<a class="lg" href="index.html">')

    # Footer links
    old_fn = r'<div class="fn"><a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#overview"[^>]*>Products</a><a href="#">Technology</a><a href="#">Insights</a><a href="#">About Us</a><a href="#">Contact Us</a><a href="#">Register for a Demo</a></div>'
    new_fn = r'<div class="fn"><a href="neuromates-products.html#overview">Products</a><a href="technology/index.html">Technology</a><a href="insights/index.html">Insights</a><a href="about/index.html">About Us</a><a href="contact.html">Contact Us</a><a href="register-demo.html">Register for a Demo</a></div>'
    html = re.sub(old_fn, new_fn, html)

    # CTA button links
    html = html.replace('<a class="btn" href="#">Register for a demo →</a>', '<a class="btn" href="register-demo.html">Register for a demo →</a>')
    html = html.replace('<a class="b2" href="#">Contact us →</a>', '<a class="b2" href="contact.html">Contact us →</a>')

    for op in out_paths:
        with open(op, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Wrote updated home to {op}")

def update_product_links(filepath, out_paths):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # In navbar
    old_prod_nav = r'<a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#overview"[^>]*>Products</a><div><a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#overview"[^>]*>Products Overview</a><a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#parkinsons-care"[^>]*>Parkinson’s Care</a><a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#alzheimers-care"[^>]*>Alzheimer’s Care</a><a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#epilepsy-care"[^>]*>Epilepsy Care</a><a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#paralysis-care"[^>]*>Paralysis Care</a></div>'
    new_prod_nav = r'<a href="#overview">Products</a><div><a href="#overview">Products Overview</a><a href="#parkinsons-care">Parkinson’s Care</a><a href="#alzheimers-care">Alzheimer’s Care</a><a href="#epilepsy-care">Epilepsy Care</a><a href="#paralysis-care">Paralysis Care</a></div>'
    html = re.sub(old_prod_nav, new_prod_nav, html)

    old_tech_nav = r'<li class="dd"><a href="#">Technology</a><div><a href="#">Technology Overview</a><a href="#">Connected Devices</a><a href="#">AI &amp; Machine Learning</a><a href="#">Monitoring &amp; Analytics</a><a href="#">Connected Care Platform</a></div></li>'
    new_tech_nav = r'<li class="dd"><a href="technology/index.html">Technology</a><div><a href="technology/index.html">Technology Overview</a><a href="technology/connected-devices.html">Connected Devices</a><a href="technology/ai-machine-learning.html">AI &amp; Machine Learning</a><a href="technology/monitoring-analytics.html">Monitoring &amp; Analytics</a><a href="technology/connected-care-platform.html">Connected Care Platform</a></div></li>'
    html = html.replace(old_tech_nav, new_tech_nav)

    old_ins_nav = r'<li class="dd"><a href="#">Insights</a><div><a href="#">Insights Overview</a><a href="#">Research</a><a href="#">Articles</a><a href="#">Case Studies</a><a href="#">Resources</a></div></li>'
    new_ins_nav = r'<li class="dd"><a href="insights/index.html">Insights</a><div><a href="insights/index.html">Insights Overview</a><a href="insights/research.html">Research</a><a href="insights/articles.html">Articles</a><a href="insights/case-studies.html">Case Studies</a><a href="insights/resources.html">Resources</a></div></li>'
    html = html.replace(old_ins_nav, new_ins_nav)

    old_abt_nav = r'<li class="dd"><a href="#">About Us</a><div><a href="#">About Neuro Mates</a><a href="#">Vision &amp; Mission</a><a href="#">Our Approach</a><a href="#">Impact</a></div></li>'
    new_abt_nav = r'<li class="dd"><a href="about/index.html">About Us</a><div><a href="about/index.html">About Neuro Mates</a><a href="about/vision-mission.html">Vision &amp; Mission</a><a href="about/our-approach.html">Our Approach</a><a href="about/impact.html">Impact</a></div></li>'
    html = html.replace(old_abt_nav, new_abt_nav)

    html = html.replace('<li><a href="#">Contact Us</a></li>', '<li><a href="contact.html">Contact Us</a></li>')
    html = html.replace('<li><a class="btn" href="#">Register for a Demo</a></li>', '<li><a class="btn" href="register-demo.html">Register for a Demo</a></li>')
    html = html.replace('<a class="lg" href="#">', '<a class="lg" href="index.html">')

    # Footer links
    old_fn = r'<div class="fn"><a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#overview"[^>]*>Products</a><a href="#">Technology</a><a href="#">Insights</a><a href="#">About Us</a><a href="#">Contact Us</a><a href="#">Register for a Demo</a></div>'
    new_fn = r'<div class="fn"><a href="#overview">Products</a><a href="technology/index.html">Technology</a><a href="insights/index.html">Insights</a><a href="about/index.html">About Us</a><a href="contact.html">Contact Us</a><a href="register-demo.html">Register for a Demo</a></div>'
    html = re.sub(old_fn, new_fn, html)

    # CTA button links
    html = html.replace('<a class="btn" href="#">Register for a demo →</a>', '<a class="btn" href="register-demo.html">Register for a demo →</a>')
    html = html.replace('<a class="b2" href="#">Contact us →</a>', '<a class="b2" href="contact.html">Contact us →</a>')

    for op in out_paths:
        with open(op, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Wrote updated products to {op}")

home_src = r'D:\Neuromates(website)\Neuro Mates _ Connected neurological care.html'
home_dsts = [
    r'D:\Neuromates(website)\neuromates-home.html',
    r'D:\Neuromates(website)\index.html'
]
update_home_links(home_src, home_dsts)

prod_src = r'D:\Neuromates(website)\Products _ Neuro Mates.html'
prod_dsts = [
    r'D:\Neuromates(website)\neuromates-products.html',
    r'D:\Neuromates(website)\products.html'
]
update_product_links(prod_src, prod_dsts)

