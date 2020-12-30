import re

with open('诊断学选择题.txt', 'r', encoding='utf-8') as f1, \
    open('aaaa.txt', 'w', encoding='utf-8') as f2:

    lines = f1.readlines()
    b = ''
    for l in lines:
        if a := re.findall(r'（[A-E]+）', l):
            print(b)
            l = l.replace(a[0], '')
            f2.write('\n答案：%s\n\n%s' % (b, l))
            b = a[0]
        else:
            f2.write(l)
    f2.write('\n答案：%s' % b)