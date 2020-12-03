with open('病理x.txt', 'r', encoding='UTF-8') as f1, \
    open('x处理中.txt', 'w', encoding='UTF-8') as f2:
    lines_1 = f1.readlines()
    lines_2 = []

    for l in lines_1:
        l = l.strip()
        if l != '':
            if len(l) == 1 and l in 'ABCDE':
                pass
            elif '答案解析' in l:
                pass
            elif '得分' in l:
                lines_2.append(l)
            elif '正确答案' in l:
                lines_2.append(l.split(' 我的答案')[0] + '\n')
            elif l[0] in '123456789':
                lines_2.append(l + '.')
            elif l[:2] in 'A、B、C、D、E、':
                lines_2.append(l.replace('、', '.'))
            else:
                lines_2.append(l + '\n')

    
    f2.writelines(lines_2)
    
with open('x处理中.txt', 'r', encoding='UTF-8') as f2, \
    open('x处理后.txt', 'w', encoding='UTF-8') as f3:

    lines = f2.readlines()
    for l in lines:
        if '得分' not in l:
            f3.write(l)

    '''
    # 做成含有@的题库
    d = {}
    c = 1
    for l in lines_1:
        l = l.strip()

        if l[0] in '123456789':
            f3.write(l + '@')
            print(l)
            c += 1
        elif l[0] in 'ABCDE':
            d[l[0]] = l[2:]
        elif '正确答案' in l:
            f3.write(d[l[-1]] + '\n')
            d = {}
    '''