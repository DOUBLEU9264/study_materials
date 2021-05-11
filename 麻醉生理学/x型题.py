f1 = open("before", "r", encoding="utf-8")  # 打开题目文件
lines_f1 = f1.readlines()
f1.close()

f2 = open("after", "a", encoding="utf-8")  # 打开待写入文件

ans_list = lines_f1[-1].strip()  # 获取答案字符串
lines_f1 = lines_f1[:-1]

alphabet = ["A", "B", "C", "D", "E"]

# 处理答案
ans_dict = {}
for e in ans_list.split(" "):
    cache_list = e.split("、")
    ans_dict[cache_list[0]] = cache_list[1]

# 处理题目
for line_f1 in lines_f1:
    line_f1 = line_f1.strip()
    every = line_f1.split("@")
    qus_index = line_f1.split("、", 1)[0]
    f2.write(every[0] + "@" +
             every[alphabet.index(ans_dict[qus_index])+1] + "\n")
    print(every[0] + "@" + every[alphabet.index(ans_dict[qus_index])+1])

f2.write("\n")
f2.close()
