import json


f1 = open("选择题答案.txt", "r", encoding="utf-8")
lines = f1.readlines()
f1.close()

章节 = ""
题型 = ""
txt = ""
cache = ""
array = []


def add_to_list():
    global cache, array
    if cache == "":
        return
    array.append("%s|%s|%s\n" % (章节, 题型, cache.strip().replace("\n", "@")))
    cache = ""


for line in lines:
    if (line[0] == "第" and "章" in line):
        add_to_list()
        章节 = line.strip()
        continue
    elif "A型题" in line:
        add_to_list()
        题型 = "A型题"
        continue
    elif "B型题" in line:
        add_to_list()
        题型 = "B型题"
        continue
    elif "X型题" in line:
        add_to_list()
        题型 = "X型题"
        continue

    if line[0] == "(" or line[0] in "123456789":
        add_to_list()

    cache += line

with open("选择题答案案.txt", "w", encoding="utf-8") as f:
    f.writelines(array)
