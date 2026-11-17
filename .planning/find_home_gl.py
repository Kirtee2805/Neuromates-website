with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = "/* 3D: Anatomical Interactive 3D Human Brain with Neural Synapses & Visitor Interaction */"
idx = text.find(start_marker)
if idx == -1:
    idx = text.find("const T = THREE, canvas = $('#gl');")
    if idx != -1:
        idx = text.rfind('/*', 0, idx)

end_marker = "</script>"
end_idx = text.find(end_marker, idx)

print(f"Old script block: start={idx}, end={end_idx}, length={end_idx - idx}")
print("Tail of old script:", text[end_idx-100:end_idx])
