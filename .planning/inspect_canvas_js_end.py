with open(r"D:\Neuromates(website)\about\index.html", "r", encoding="utf-8") as f:
    t = f.read()

pos2 = t.find("const cvs = document.getElementById('relationship-canvas');")
end_pos = t.find("</script>", pos2)
print("Canvas JS length:", end_pos - pos2)
print(t[end_pos - 400:end_pos])

