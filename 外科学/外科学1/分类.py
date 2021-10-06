f1 = open("外科学1.txt", "r", encoding="utf-8")
f1_lines = f1.readlines()
f1.close()

if_write = 0
txt = ""
type = "病案分析"

for line in f1_lines:
    if (line[0] == "第" and "章" in line) or "、试题答案及分析" in line:
        txt += "\n" + line
        continue
    elif line[:2] in "(一(二(三(四(五" and type in line:
        if_write = 1
        txt += "\n"
        # continue
    elif line[:2] in "(一(二(三(四(五":
        if_write = 0

    if if_write:
        txt += line

with open(type+".txt", "w", encoding="utf-8") as f:
    f.write(txt)
