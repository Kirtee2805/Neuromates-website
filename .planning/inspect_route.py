with open('neuromates-products.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Look for 'function route()' in text
idx = text.find('function route()')
if idx != -1:
    print("--- ROUTE FUNCTION ---")
    print(text[idx:idx+1500])

# Look for epilepsy handling
idx2 = text.find("cur=='epilepsy-care'")
if idx2 != -1:
    print("\n--- EPILEPSY CUR CHECK ---")
    print(text[idx2-200:idx2+800])

