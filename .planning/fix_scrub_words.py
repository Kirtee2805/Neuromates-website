p = r"D:\Neuromates(website)\technology\ai-machine-learning.html"
with open(p, "r", encoding="utf-8") as f:
    c = f.read()

# 1. Update .scrub-word CSS
old_css = """.scrub-word {
      display: inline-block;
      color: rgba(14, 59, 67, 0.22);
      transition: color 0.15s ease-out;
    }"""

new_css = """.scrub-word {
      display: inline-block;
      margin-right: 0.28em;
      color: rgba(14, 59, 67, 0.22);
      transition: color 0.15s ease-out;
    }"""

if old_css in c:
    c = c.replace(old_css, new_css)
    print("Updated .scrub-word CSS with margin-right spacing.")

# 2. Update JS split & join with space
old_js = "scrubContainer.innerHTML = words.map(w => `<span class=\"scrub-word\">${w}</span>`).join('');"
new_js = "scrubContainer.innerHTML = words.map(w => `<span class=\"scrub-word\">${w}</span>`).join(' ');"

if old_js in c:
    c = c.replace(old_js, new_js)
    print("Updated scrubContainer.innerHTML join(' ') with proper word spaces.")
else:
    # Check if there was trailing space in template
    old_js_alt = "scrubContainer.innerHTML = words.map(w => `<span class=\"scrub-word\">${w} </span>`).join('');"
    if old_js_alt in c:
        c = c.replace(old_js_alt, new_js)
        print("Updated scrubContainer.innerHTML join(' ') with proper word spaces (alt).")

with open(p, "w", encoding="utf-8") as f:
    f.write(c)
print("Saved ai-machine-learning.html successfully.")

