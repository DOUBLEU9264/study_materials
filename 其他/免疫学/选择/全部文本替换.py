for i in range(1, 20):
    with open(str(i)+'.txt', 'w', encoding='UTF-8') as f2, \
        open((str(i) + 'changed.txt'), 'r', encoding='UTF-8') as f1:
        # 替换文本
        s = '   '
        rpls_s = '  '
        text = f1.read()
        f2.write(text.replace(s, rpls_s))
        '''

        # 处理格式
        lines = f1.readlines()
        for i in range(len(lines)-1):
            if lines[i+1][:2] in 'B.C.D.E.F.':
                f2.write(lines[i].replace('\n', '  '))
            else:
                f2.write(lines[i])
        f2.write(lines[-1])
        '''