import re

# 1. Read user-provided file
with open(r'C:\Users\Hp\.gemini\antigravity\brain\97e9f06c-a990-4fae-9687-3f72ccbf640d\.user_uploaded\media_1794933374184_d0ed0c5a.html', 'r', encoding='utf-8') as f:
    user_content = f.read()

# Extract the style block
style_match = re.search(r'<style>(.*?)</style>', user_content, re.DOTALL)
if not style_match:
    raise ValueError("Could not find style in user content")
user_style = style_match.group(1).strip()

# Extract header HTML
header_match = re.search(r'(<header class="p-hero">.*?</header>)', user_content, re.DOTALL)
if not header_match:
    raise ValueError("Could not find header in user content")
user_header = header_match.group(1).strip()

print(f"Extracted user style: {len(user_style)} chars")
print(f"Extracted user header: {len(user_header)} chars")

target_files = [
    'neuromates-products.html',
    'products.html',
    'Products _ Neuro Mates.html'
]

for filename in target_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add the style before </style> or before </head>
    # Check if user_style already added
    if '.p-hero' not in content:
        # insert user_style into the existing <style> tag or create one before </head>
        if '</style>' in content:
            content = content.replace('</style>', f"\n/* USER PROVIDED HERO STYLES */\n{user_style}\n</style>", 1)
        else:
            content = content.replace('</head>', f"<style>\n{user_style}\n</style>\n</head>", 1)
    else:
        # replace existing .p-hero styles if any
        pass

    # Replace the overview header
    # Current overview header pattern
    # It is inside <div class="pv on" id="v-overview"> ... <section class="bg stk z">
    overview_header_pattern = r'(<div\s+class="pv[^"]*"\s+id="v-overview">\s*)<header[^>]*>.*?</header>(\s*<section)'
    match = re.search(overview_header_pattern, content, re.DOTALL)
    if match:
        content = content[:match.start()] + match.group(1) + user_header + match.group(2) + content[match.end():]
        print(f"Successfully replaced overview header in {filename}")
    else:
        # Try finding <header class="ph">...</header> right after id="v-overview">
        idx = content.find('id="v-overview"')
        if idx != -1:
            end_header = content.find('</header>', idx)
            start_header = content.find('<header', idx)
            if start_header != -1 and end_header != -1 and start_header < end_header:
                content = content[:start_header] + user_header + content[end_header + len('</header>'):]
                print(f"Replaced header by index search in {filename}")
            else:
                print(f"Could not find header tags after v-overview in {filename}")
        else:
            print(f"Could not find v-overview in {filename}")

    # Add hash alias support to router in JavaScript so both #parkinsons and #parkinsons-care work
    if 'const HASH_ALIASES' not in content:
        alias_code = """const HASH_ALIASES={'parkinsons':'parkinsons-care','alzheimers':'alzheimers-care','epilepsy':'epilepsy-care','paralysis':'paralysis-care','parkinsons-care':'parkinsons-care','alzheimers-care':'alzheimers-care','epilepsy-care':'epilepsy-care','paralysis-care':'paralysis-care','overview':'overview'};
function route(){let v=location.hash.slice(1);if(HASH_ALIASES[v])v=HASH_ALIASES[v];if(!VS.includes(v)){v=cur&&!location.hash?'overview':'overview';if(location.hash&&$('#'+location.hash.slice(1)))return}"""
        content = re.sub(r'function route\(\)\{let v=location\.hash\.slice\(1\);if\(!VS\.includes\(v\)\)\{v=cur&&!location\.hash\?\'overview\':\'overview\';if\(location\.hash&&#\'\+location\.hash\.slice\(1\)\)\)return\}',
                         alias_code, content)
        # Also handle standard regex if above string didn't exact-match
        if 'const HASH_ALIASES' not in content:
            old_route_pat = r'function route\(\)\s*\{\s*let v=location\.hash\.slice\(1\);'
            content = re.sub(old_route_pat,
                             r"const HASH_ALIASES={'parkinsons':'parkinsons-care','alzheimers':'alzheimers-care','epilepsy':'epilepsy-care','paralysis':'paralysis-care'}; function route(){let v=location.hash.slice(1);if(HASH_ALIASES[v])v=HASH_ALIASES[v];",
                             content)
        print(f"Updated router in {filename}")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {filename}")

print("Done applying user hero!")
