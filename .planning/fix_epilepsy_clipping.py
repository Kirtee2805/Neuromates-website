for filename in ['neuromates-products.html', 'products.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix epilepsy .r clip-path
    old_rule1 = 'body[data-v=epilepsy-care] .r{opacity:1;transform:none;clip-path:inset(0 100% 0 0);transition:clip-path 1.2s var(--e)}'
    new_rule1 = 'body[data-v=epilepsy-care] .r{opacity:1;transform:none;clip-path:none;transition:opacity .6s var(--e)}'
    
    # Fix h1.wp clip-path
    old_rule2 = 'h1.wp{clip-path:inset(0 100% 0 0);transition:clip-path 1.6s var(--e)}'
    new_rule2 = 'h1.wp{clip-path:none;opacity:1;transition:opacity .6s var(--e)}'

    count1 = content.count(old_rule1)
    count2 = content.count(old_rule2)
    print(f"{filename}: found rule1 {count1} times, rule2 {count2} times")

    content = content.replace(old_rule1, new_rule1)
    content = content.replace(old_rule2, new_rule2)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

print("Replacement complete in products files!")

