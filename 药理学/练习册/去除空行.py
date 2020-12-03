with open('yaoli.txt', 'r', encoding='UTF-8') as f1, \
    open('yaoli无空行.txt', 'w', encoding='UTF-8') as f2:
    lines = f1.readlines()

    count = 0
    for l in lines:
        if l.strip() != '':
            f2.write(l.strip() + '\n')
        else:
            count += 1
            print('发现%d个空行' % count)