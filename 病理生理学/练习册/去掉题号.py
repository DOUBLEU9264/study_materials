import time

t = time.time()
with open('名解.txt', 'r', encoding='UTF-8') as f_liuke, \
    open('名解去题号.txt', 'w', encoding='UTF-8') as f2:

    count = 0
    lines_liuke = f_liuke.readlines()
    for l in lines_liuke:
        count += 1
        splited_list = l.split('.')
        print(splited_list[0], end='\t')
        f2.write('.'.join(splited_list[1:]))
    print('\n共计耗时' + str(time.time()-t) + '秒，处理了' + str(count) + '道题。')