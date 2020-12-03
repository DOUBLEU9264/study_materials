list_1 = ['B.', 'C.', 'D.', 'E.']

with open('cache.txt', 'r', encoding='UTF-8') as f1,\
    open('cache处理后.txt', 'w', encoding='UTF-8') as f2:

    lines = f1.readlines()
    for l in lines:
        l = l.strip()
        if l == '':
            continue
        for i in list_1:
            if i in l:
                l = l.replace(i, '\n'+i)
        f2.write(l + '\n')
        