with open('病理选择621.txt', 'r', encoding='UTF-8') as f1,\
    open('bingli_db.txt', 'w', encoding='UTF-8') as f2:

    lines = f1.readlines()
    count = 1
    ans_dict = {}

    for l in lines:
        l = l.strip()
        if l == '':
            pass
        elif l[:2] not in 'A.B.C.D.E.正确':
            print(l)
            f2.write('\n' + l + '@')
            ans_dict = {}
        elif l[:2] in 'A.B.C.D.E.':
            ans_dict[l[0]] = l[2:]
        elif l[:2] == '正确':
            if l.split(':')[1] != 'ABCDE':
                for i in l.split(':')[1]:
                    f2.write(ans_dict[i] + '  ')
            else:
                f2.write('ABCDE')
        