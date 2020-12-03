with open('六节选择题.txt', 'r', encoding='utf-8') as f1,\
    open('choose.txt', 'w', encoding='utf-8') as f2:

    lines = f1.readlines()

    for l in lines:
        if l[0] in '123456789':
            f2.write('\n%s\n' % l)
        elif l[:2] in 'A.B.C.D.':
            f2.write('- %s' % l)
        elif l[:2] == 'E.':
            f2.write('- %s\n' % l)
        else:
            f2.write(l)