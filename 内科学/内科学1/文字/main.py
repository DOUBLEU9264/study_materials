f1 = open("问答题.txt", "r", encoding="utf-8")
f2 = open("问答题有序号.txt", "w", encoding="utf-8")

lines = f1.readlines()
f1.close()

i = 0
for line in lines:
    if line[0] == "@":
        i += 1
        line = str(i) + "." + line[1:]

    f2.write(line)

f2.close()
