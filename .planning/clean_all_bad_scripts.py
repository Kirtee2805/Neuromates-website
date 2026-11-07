import glob, re

files = glob.glob('**/*.html', recursive=True)
fixed = []

for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for <script src="...tokens.css"></script>
    new_content = re.sub(r'\s*<script\s+src="[^"]*tokens\.css"[^>]*></script>', '', content)
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        fixed.append(path)

print(f"Fixed {len(fixed)} files: {fixed}")

