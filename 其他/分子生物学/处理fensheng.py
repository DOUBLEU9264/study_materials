with open('fensheng.txt', 'r', encoding='UTF-8') as f1, \
    open('fensheng处理后.txt', 'w', encoding='UTF-8') as f2:

    lines_1 = f1.readlines()
    lines = []

    for l in lines_1:
        lines.append(l.strip() + '\n')

    for i in range(len(lines)-1):
        if lines[i+1][0] in 'BCDE':
            f2.write(lines[i].replace('\n', '  '))
        else:
            f2.write(lines[i])
    
    f2.write(lines[-1])