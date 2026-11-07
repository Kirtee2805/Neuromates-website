with open(r"D:\Neuromates(website)\index.html", "r", encoding="utf-8") as f:
    c = f.read()

start_marker = "/* 3D: devices orbiting the care platform */"
pos_start = c.find(start_marker)
pos_end = c.find("</script>", pos_start)

print("Start pos:", pos_start)
print("End pos:", pos_end)
print("Content length to replace:", pos_end - pos_start)
print("Content preview:")
print(c[pos_start:pos_start + 500])
print("...")
print(c[pos_end - 300:pos_end])

