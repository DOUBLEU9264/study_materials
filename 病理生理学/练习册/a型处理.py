def f_ans(s):
    s = s.replace('.', '')
    s = s.replace(' ', '')
    s = s.replace(',', '')
    s = s.upper()
    s = s.replace('A', '.A ')
    s = s.replace('B', '.B ')
    s = s.replace('C', '.C ')
    s = s.replace('D', '.D ')
    s = s.replace('E', '.E ')
    s = s.strip()
    return s


def f1():
    # 预处理去除无用空行
    with open('a型处理前.txt', 'r', encoding='UTF-8') as f1,\
        open('a型处理中.txt', 'w', encoding='UTF-8') as f2:

        lines = f1.readlines()
        for l in lines:
            l = l.strip()
            if l[0] in '123456789ABCDE':
                f2.write('\n' + l)
            else:
                f2.write(l)


def f2(ans):
    with open('a型处理后.txt', 'w', encoding='UTF-8') as f4,\
        open('a型处理中.txt', 'r', encoding='UTF-8') as f3:
        
        index = 0
        
        ans_list = ans.split(' ')
        lines = f3.readlines()
        for l in lines:
            if l[0] in '123456789':
                index = int(l.split('.')[0]) - 1
                f4.write(l.replace('\n', '@'))
            elif l[0] == ans_list[index].split('.')[1]:
                if ans_list[index].split('.')[0] == str(index+1):
                    f4.write(l[2:])
                else:
                    print(index)


# main
# 答案字符串
ans = '1.C 2.B 3.D 4.C 5.E6.D 7.A 8.E 9.A 10.C11 .B 12.D13.D14.C15.B 16.B 17.B18.D19.C 20.E 21.A 22.B 23.C 24.C 25.E26.A 27.D 28.B'

f1()
f2(f_ans(ans))