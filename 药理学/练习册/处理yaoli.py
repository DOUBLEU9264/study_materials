with open('yaoli.txt', 'r', encoding='UTF-8') as f1, \
    open('yaoli处理后.txt', 'w', encoding='UTF-8') as f2:
    
    lines = f1.readlines()
    for i in range(len(lines)-1):
        if len(lines[i+1].strip())>0 and lines[i+1].strip()[0] not in '123456789ABCDEFGHIJ':
            f2.write(lines[i].strip())
        else:
            f2.write(lines[i].strip() + '\n')