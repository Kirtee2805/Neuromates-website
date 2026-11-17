import os

files_to_fix = [
    'neuromates-products.html',
    'products.html',
    'Products _ Neuro Mates.html'
]

old_pattern = '.b1{left:0;top:8%;animation-delay:.1s,.1s}.b2{right:0;top:0;width:33%;animation-delay:.25s,-1.5s}.b3{left:18%;bottom:0;animation-delay:.4s,-3s}.b4{right:2%;bottom:14%;width:32%;animation-delay:.55s,-4.5s}'
new_replacement = '.bub.b1{left:0;top:8%;animation-delay:.1s,.1s}.bub.b2{right:0;top:0;width:33%;animation-delay:.25s,-1.5s}.bub.b3{left:18%;bottom:0;animation-delay:.4s,-3s}.bub.b4{right:2%;bottom:14%;width:32%;animation-delay:.55s,-4.5s}\n.bt .b2{width:auto!important;position:static!important}'

for fn in files_to_fix:
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()

    if old_pattern in content:
        content = content.replace(old_pattern, new_replacement)
        print(f"Replaced scoped .bub.b1-.b4 in {fn}")
    else:
        print(f"Old pattern not found in {fn}, searching variant...")
        # Check if spaces exist
        import re
        content = re.sub(
            r'\.b1\s*\{\s*left:\s*0;\s*top:\s*8%[^\}]*\}\s*\.b2\s*\{\s*right:\s*0;\s*top:\s*0;\s*width:\s*33%[^\}]*\}\s*\.b3\s*\{\s*left:\s*18%[^\}]*\}\s*\.b4\s*\{\s*right:\s*2%[^\}]*\}',
            new_replacement,
            content
        )

    # Also make sure .bt .b2 has width: auto
    if '.bt .b2' not in content:
        content = content.replace('</style>', '\n.bt .b2{width:auto!important;position:static!important}\n</style>', 1)

    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {fn}")

print("Fix completed!")
