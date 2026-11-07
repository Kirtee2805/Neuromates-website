with open('neuromates-products.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('function wave(')
if idx != -1:
    print(html[idx:idx+600])

