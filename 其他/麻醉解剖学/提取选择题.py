with open('选择题.txt', 'r', encoding='utf-8') as f1,\
    open('选择答案.txt', 'r', encoding='utf-8') as f2,\
    open('选择out.txt', 'w', encoding='utf-8') as f3:

    lines = f1.readlines()
    lines_ans = f2.readlines()

    for i in range(len(lines)-1):
        f3.write('%s@%s\n' %(lines[i].strip(), lines_ans[i].strip()))