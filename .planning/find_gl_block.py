with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = 602272 # where Rn = new T.WebGLRenderer was found
start_of_block = text.rfind('/* ', 0, pos)
if start_of_block == -1:
    start_of_block = text.rfind('//', 0, pos)
print("Block starts around:", text[pos-300:pos+50])
