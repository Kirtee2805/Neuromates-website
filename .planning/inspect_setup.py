with open('neuromates-products.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('function setup(v)')
if idx != -1:
    print(text[idx:idx+2500])

