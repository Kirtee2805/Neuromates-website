with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find("const T = THREE, canvas = $('#gl');")
print(text[idx:idx+2500])
