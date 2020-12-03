with open('a单选.txt', 'r', encoding='UTF-8') as f1, open('a处理后单选.txt', 'w', encoding='UTF-8') as f2:
    lines = f1.readlines()
    for i in range(len(lines)-1):
        if lines[i+1][0] not in '123456789A':
            f2.write(lines[i].replace('\n', '  '))
        else:
            f2.write(lines[i])