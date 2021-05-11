f1 = open("before", "r", encoding="utf-8")  # 打开题目文件
lines_f1 = f1.readlines()
f1.close()

f2 = open("after_1", "a", encoding="utf-8")  # 打开待写入文件

ans_list = lines_f1[-1].strip()  # 获取答案字符串
lines_f1 = lines_f1[:-1]

alphabet = ["A", "B", "C", "D", "E"]

# 处理答案
ans_dict = {}
for e in ans_list.split(" "):
    cache_list = e.split(".")
    ans_dict[cache_list[0]] = cache_list[1]

# 处理题目
for line_f1 in lines_f1:
    line_f1 = line_f1.strip()  # 去掉题目前后空白
    every = line_f1.split("@")  # 以@符分隔
    题目 = every[0]  # 获取题目
    选项 = every[1:]  # 获取全部选项
    题号 = line_f1.split("、", 1)[0]
    此题答案 = ans_dict[题号]
    答案字符串 = ""
    if 此题答案 == "ABCDE":
        答案字符串 = 此题答案
    else:
        for i in 此题答案:
            答案字符串 += 选项[alphabet.index(i)] + " "
    f2.write(题目 + "@" + 答案字符串 + "\n")
    print(题目 + "@" + 答案字符串)

f2.write("\n")
f2.close()
