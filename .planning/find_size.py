with open('neuromates-products.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('function size(')
if idx != -1:
    print(html[idx-100:idx+400])
else:
    idx2 = html.find('size=')
    print("size= found at:", idx2)
    print(html[idx2-50:idx2+200])

