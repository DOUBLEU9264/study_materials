with open('a.txt', 'r', encoding='utf-8') as f1, \
    open('b.txt', 'w', encoding='utf-8') as f2:

    lines = f1.readlines()
    i = 0
    for l in lines:
        i += 1
        l = l.strip()
        if l != '':
            f2.write('%d.%s\n' % (i, l))
print('Done.')