# 答案之间两个半角空格
with open('b处理后答案.txt', 'r', encoding='UTF-8') as f_ans:
    answer = f_ans.read()
ans_list = answer.split('  ')
ans_dict = {}
for ans in ans_list:
    ans_dict[ans.split('.')[0]] = ans.split('.')[1]

with open('a单选.txt', 'r', encoding='UTF-8') as f1, open('a处理后单选.txt', 'w', encoding='UTF-8') as f2:
    lines = f1.readlines()
    for i in range(0, len(lines), 2):
        if lines[i].strip() == '':
            f2.write(lines[i])
            f2.write(lines[i+1].replace('\n', '@\n'))
            continue
        f2.write(lines[i].replace('\n', '@'))
        choose = lines[i+1].replace('\n', '').strip().split('  ')
        choose_dict = {}
        for cho in choose:
            choose_dict[cho.split('.')[0]] = cho.split('.')[1]
        f2.write(choose_dict[ans_dict[lines[i].split('.')[0]]] + '\n')
        print(i / 2 + 1)
