f1 = open("外科学1.txt", "r", encoding="utf-8")
f1_lines = f1.readlines()
f1.close()

if_write = 0
txt = ""

for line in f1_lines:
    if line[0] == "第" and "章" in line:
        if_write = 1
    elif line.startswith("三、试"):
        if_write = 0
        txt += "\n"

    if if_write:
        txt += line

with open("纲要.txt", "w", encoding="utf-8") as f:
    f.write(txt)
