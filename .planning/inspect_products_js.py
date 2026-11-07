import re

with open('neuromates-products.html', 'r', encoding='utf-8') as f:
    text = f.read()

print('Length:', len(text))
views = re.findall(r'id="(v-[^"]+)"', text)
print('Views found:', views)

# Find scripts
scripts = re.findall(r'<script\b[^>]*>(.*?)</script>', text, re.DOTALL)
print(f'Found {len(scripts)} scripts')
for i, s in enumerate(scripts):
    print(f'Script {i} length: {len(s)}')
    # Check if there is route / hash handling
    if 'hash' in s or 'view' in s.lower() or 'epilepsy' in s.lower():
        print(f'Script {i} contains routing keywords')
        # Print snippet of how views are switched
        lines = [l for l in s.split('\n') if any(k in l for k in ['hash', 'v-', 'show', 'display', 'epilepsy'])]
        for l in lines[:15]:
            print('   ', l.strip()[:100])

