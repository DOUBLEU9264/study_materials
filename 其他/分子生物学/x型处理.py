def f_ans(s):
    '''处理答案字符串'''

    s = s.replace('.', '')
    s = s.replace(' ', '')
    s1 = ''
    for i in range(len(s)-1):
        if s[i] in '1234567890' and s[i+1] in 'ABCDE':
            s1 += s[i] + '.'
        elif  s[i] in 'ABCDE' and s[i+1] in '123456789':
            s1 += s[i] + ' '
        else:
            s1 += s[i]
    s1 += s[-1]
    s1 = s1.strip()
    print(s1)
    d = {}
    for i in s1.split(' '):
        d[i.split('.')[0]] = i.split('.')[1]
    return d


def f1():
    '''保证题目在同一行'''

    with open('x型处理前.txt', 'r', encoding='UTF-8') as f1,\
        open('x型处理中.txt', 'w', encoding='UTF-8') as f2:

        lines = f1.readlines()
        f2.write(lines[0].strip())
        for l in lines[1:]:
            l = l.strip()
            if l[0] in '123456789ABCDE':
                f2.write('\n' + l)
            else:
                f2.write(l)


def f2(d):
    ''''''

    with open('x型处理后.txt', 'w', encoding='UTF-8') as f2,\
        open('x型处理中.txt', 'r', encoding='UTF-8') as f1:

        lines = f1.readlines()
        anses = ''
        for l in lines:
            l = l.strip()
            if l[0] in '123456789':
                f2.write('\n' + l + '@')
                anses = d[l.split('.')[0]]
                if anses == 'ABCD':
                    f2.write(anses)

            elif anses != 'ABCD' and l[0] in anses:
                f2.write(l[2:] + '  ')
            
                
if __name__ == '__main__':
    # main
    ans = '\
    1.ABCD2.ABD3.ABCD4.ABCD5.ABCD6.AB7.ABC8.ABC'
    f1()
    f2(f_ans(ans))