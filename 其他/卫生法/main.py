f1 = f = open("1.txt", "w", encoding="utf-8")


def write_array(array):
    ans = array[0].split("(")[-1][:-1]
    f1.write(array[0] + "@")
    for c in ans:
        f1.write(array[["A", "B", "C", "D", "E"].index(c) + 1] + "  ")
    f1.write("\n")


f = open("卫生法.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()
array = []

for line in lines:
    line = line.strip()

    if line == "":
        write_array(array)
        array = []
    else:
        array.append(line)

f1.close()
print("Done.")
