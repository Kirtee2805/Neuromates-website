with open('neuromates-products.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('e_prod')
while idx != -1:
    print("Found e_prod at:", idx)
    print(text[max(0, idx-50):min(len(text), idx+150)])
    idx = text.find('e_prod', idx+1)

