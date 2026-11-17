with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = 602272
end_pos = text.find('</script>', pos)
print(f"Script length from {pos} to {end_pos}: {end_pos - pos}")
print(text[pos-100:end_pos])
