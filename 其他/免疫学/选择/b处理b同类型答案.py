with open('b单选答案.txt', 'r', encoding='UTF-8') as f1, open('b处理后答案.txt', 'w', encoding='UTF-8') as f2:
    lines = f1.readlines()
    for l in lines:
        if l[0] in '123456789':
            f2.write(l.replace('\n', '  '))