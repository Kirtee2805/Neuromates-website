import re
import os

# 1. Revert Home page
with open(r'D:\Neuromates(website)\Neuro Mates _ Connected neurological care.html', 'r', encoding='utf-8', errors='ignore') as f:
    home_html = f.read()

# Only connect the href links in nav and footer
# In navbar
home_html = home_html.replace(
    '<a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#overview" target="_blank" rel="noopener">Products</a><div><a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#overview" target="_blank" rel="noopener">Products Overview</a><a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#parkinsons-care" target="_blank" rel="noopener">Parkinson’s Care</a><a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#alzheimers-care" target="_blank" rel="noopener">Alzheimer’s Care</a><a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#epilepsy-care" target="_blank" rel="noopener">Epilepsy Care</a><a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#paralysis-care" target="_blank" rel="noopener">Paralysis Care</a></div>',
    '<a href="neuromates-products.html#overview">Products</a><div><a href="neuromates-products.html#overview">Products Overview</a><a href="neuromates-products.html#parkinsons-care">Parkinson’s Care</a><a href="neuromates-products.html#alzheimers-care">Alzheimer’s Care</a><a href="neuromates-products.html#epilepsy-care">Epilepsy Care</a><a href="neuromates-products.html#paralysis-care">Paralysis Care</a></div>'
)

home_html = home_html.replace(
    '<li class="dd"><a href="#">Technology</a><div><a href="#">Technology Overview</a><a href="#">Connected Devices</a><a href="#">AI &amp; Machine Learning</a><a href="#">Monitoring &amp; Analytics</a><a href="#">Connected Care Platform</a></div></li>',
    '<li class="dd"><a href="technology/index.html">Technology</a><div><a href="technology/index.html">Technology Overview</a><a href="technology/connected-devices.html">Connected Devices</a><a href="technology/ai-machine-learning.html">AI &amp; Machine Learning</a><a href="technology/monitoring-analytics.html">Monitoring &amp; Analytics</a><a href="technology/connected-care-platform.html">Connected Care Platform</a></div></li>'
)

home_html = home_html.replace(
    '<li class="dd"><a href="#">Insights</a><div><a href="#">Insights Overview</a><a href="#">Research</a><a href="#">Articles</a><a href="#">Case Studies</a><a href="#">Resources</a></div></li>',
    '<li class="dd"><a href="insights/index.html">Insights</a><div><a href="insights/index.html">Insights Overview</a><a href="insights/research.html">Research</a><a href="insights/articles.html">Articles</a><a href="insights/case-studies.html">Case Studies</a><a href="insights/resources.html">Resources</a></div></li>'
)

home_html = home_html.replace(
    '<li class="dd"><a href="#">About Us</a><div><a href="#">About Neuro Mates</a><a href="#">Vision &amp; Mission</a><a href="#">Our Approach</a><a href="#">Impact</a></div></li>',
    '<li class="dd"><a href="about/index.html">About Us</a><div><a href="about/index.html">About Neuro Mates</a><a href="about/vision-mission.html">Vision &amp; Mission</a><a href="about/our-approach.html">Our Approach</a><a href="about/impact.html">Impact</a></div></li>'
)

home_html = home_html.replace('<li><a href="#">Contact Us</a></li>', '<li><a href="contact.html">Contact Us</a></li>')
home_html = home_html.replace('<li><a class="btn" href="#">Register for a Demo</a></li>', '<li><a class="btn" href="register-demo.html">Register for a Demo</a></li>')

# In footer
home_html = home_html.replace(
    '<div class="fn"><a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#overview" target="_blank" rel="noopener">Products</a><a href="#">Technology</a><a href="#">Insights</a><a href="#">About Us</a><a href="#">Contact Us</a><a href="#">Register for a Demo</a></div>',
    '<div class="fn"><a href="neuromates-products.html#overview">Products</a><a href="technology/index.html">Technology</a><a href="insights/index.html">Insights</a><a href="about/index.html">About Us</a><a href="contact.html">Contact Us</a><a href="register-demo.html">Register for a Demo</a></div>'
)

# CTA buttons
home_html = home_html.replace('<a class="btn" href="#">Register for a demo →</a>', '<a class="btn" href="register-demo.html">Register for a demo →</a>')
home_html = home_html.replace('<a class="b2" href="#">Contact us →</a>', '<a class="b2" href="contact.html">Contact us →</a>')

# Save reverted Home page to index.html and neuromates-home.html
with open(r'D:\Neuromates(website)\index.html', 'w', encoding='utf-8') as f:
    f.write(home_html)

with open(r'D:\Neuromates(website)\neuromates-home.html', 'w', encoding='utf-8') as f:
    f.write(home_html)

print("Reverted index.html and neuromates-home.html to exact original Home page with connected links.")


# 2. Revert Products page
with open(r'D:\Neuromates(website)\Products _ Neuro Mates.html', 'r', encoding='utf-8', errors='ignore') as f:
    prod_html = f.read()

# Only connect the href links in nav and footer
prod_html = prod_html.replace(
    '<a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#overview" target="_blank" rel="noopener">Products</a><div><a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#overview" target="_blank" rel="noopener">Products Overview</a><a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#parkinsons-care" target="_blank" rel="noopener">Parkinson’s Care</a><a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#alzheimers-care" target="_blank" rel="noopener">Alzheimer’s Care</a><a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#epilepsy-care" target="_blank" rel="noopener">Epilepsy Care</a><a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#paralysis-care" target="_blank" rel="noopener">Paralysis Care</a></div>',
    '<a href="#overview">Products</a><div><a href="#overview">Products Overview</a><a href="#parkinsons-care">Parkinson’s Care</a><a href="#alzheimers-care">Alzheimer’s Care</a><a href="#epilepsy-care">Epilepsy Care</a><a href="#paralysis-care">Paralysis Care</a></div>'
)

prod_html = prod_html.replace(
    '<li class="dd"><a href="#">Technology</a><div><a href="#">Technology Overview</a><a href="#">Connected Devices</a><a href="#">AI &amp; Machine Learning</a><a href="#">Monitoring &amp; Analytics</a><a href="#">Connected Care Platform</a></div></li>',
    '<li class="dd"><a href="technology/index.html">Technology</a><div><a href="technology/index.html">Technology Overview</a><a href="technology/connected-devices.html">Connected Devices</a><a href="technology/ai-machine-learning.html">AI &amp; Machine Learning</a><a href="technology/monitoring-analytics.html">Monitoring &amp; Analytics</a><a href="technology/connected-care-platform.html">Connected Care Platform</a></div></li>'
)

prod_html = prod_html.replace(
    '<li class="dd"><a href="#">Insights</a><div><a href="#">Insights Overview</a><a href="#">Research</a><a href="#">Articles</a><a href="#">Case Studies</a><a href="#">Resources</a></div></li>',
    '<li class="dd"><a href="insights/index.html">Insights</a><div><a href="insights/index.html">Insights Overview</a><a href="insights/research.html">Research</a><a href="insights/articles.html">Articles</a><a href="insights/case-studies.html">Case Studies</a><a href="insights/resources.html">Resources</a></div></li>'
)

prod_html = prod_html.replace(
    '<li class="dd"><a href="#">About Us</a><div><a href="#">About Neuro Mates</a><a href="#">Vision &amp; Mission</a><a href="#">Our Approach</a><a href="#">Impact</a></div></li>',
    '<li class="dd"><a href="about/index.html">About Us</a><div><a href="about/index.html">About Neuro Mates</a><a href="about/vision-mission.html">Vision &amp; Mission</a><a href="about/our-approach.html">Our Approach</a><a href="about/impact.html">Impact</a></div></li>'
)

prod_html = prod_html.replace('<li><a href="#">Contact Us</a></li>', '<li><a href="contact.html">Contact Us</a></li>')
prod_html = prod_html.replace('<li><a class="btn" href="#">Register for a Demo</a></li>', '<li><a class="btn" href="register-demo.html">Register for a Demo</a></li>')

# In footer
prod_html = prod_html.replace(
    '<div class="fn"><a href="https://claude.ai/artifact/MdtJbaM9foFFhCWRVKEQBS#overview" target="_blank" rel="noopener">Products</a><a href="#">Technology</a><a href="#">Insights</a><a href="#">About Us</a><a href="#">Contact Us</a><a href="#">Register for a Demo</a></div>',
    '<div class="fn"><a href="#overview">Products</a><a href="technology/index.html">Technology</a><a href="insights/index.html">Insights</a><a href="about/index.html">About Us</a><a href="contact.html">Contact Us</a><a href="register-demo.html">Register for a Demo</a></div>'
)

# CTA buttons
prod_html = prod_html.replace('<a class="btn" href="#">Register for a demo →</a>', '<a class="btn" href="register-demo.html">Register for a demo →</a>')
prod_html = prod_html.replace('<a class="b2" href="#">Contact us →</a>', '<a class="b2" href="contact.html">Contact us →</a>')

# Save reverted Products page to neuromates-products.html and products.html
with open(r'D:\Neuromates(website)\neuromates-products.html', 'w', encoding='utf-8') as f:
    f.write(prod_html)

with open(r'D:\Neuromates(website)\products.html', 'w', encoding='utf-8') as f:
    f.write(prod_html)

print("Reverted neuromates-products.html and products.html to exact original Products page with connected links.")

# Clean up spa-views.css if it exists
spa_css = r'D:\Neuromates(website)\assets\css\spa-views.css'
if os.path.exists(spa_css):
    os.remove(spa_css)
    print("Removed temporary spa-views.css")

