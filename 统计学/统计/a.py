# 处理题目
def process_question(q, a):
    array = q.split("\t")
    title = array[0]
    array = array[1:]
    index = ["A", "B", "C", "D", "E"].index(a)
    return title + "\t" + array[index]


# 合并题目和答案
def merge(q_list, a_list, f):
    for i in range(len(a_list)):
        l = process_question(q_list[i], a_list[i])
        f.write(l + "\n")


# main
f = open("选择.txt", "r", encoding="utf-8")
f_out = open("选择_out.txt", "w", encoding="utf-8")

lines = f.readlines()
f.close()

ansList = lines[-1].strip().split(" ")
lines = [i.strip() for i in lines[:-1] if i.strip() != ""]

# 检查答案与题目长度是否相等
if len(ansList) == len(lines):
    print("题目与答案长度相等")
else:
    print("题目与答案长度不相等")

for i, j in enumerate(ansList):
    if j not in "ABCDE":
        print("第%d个答案%s存在问题" % (i+1, j))

for i, j in enumerate(lines):
    if j.count("\t") != 5:
        print("第%d个题目%s存在问题" % (i+1, j[:10]+"..."))

merge(lines, ansList, f_out)

f_out.close()
print("Done.")
