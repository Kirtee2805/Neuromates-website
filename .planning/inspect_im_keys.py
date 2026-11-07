with open('neuromates-products.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
im_match = re.search(r'const\s+IM\s*=\s*\{([^}]+)\}', text)
if im_match:
    keys = re.findall(r'"([^"]+)":\s*"data:image', im_match.group(1))
    print("Keys in IM with base64 data:", keys)
else:
    print("Could not match const IM = {...} easily, checking raw mentions:")
    for k in ['p_prod', 'p_person', 'p_detail', 'a_dash', 'e_prod', 'e_person', 'e_detail', 'pa_face', 'pa_leg']:
        print(f"Key {k} present:", f'"{k}"' in text)

