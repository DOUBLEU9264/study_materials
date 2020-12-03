import time

t = time.time()
with open('bingyuan.txt', 'r', encoding='UTF-8') as f_liuke, \
    open('bingyuan无题号.txt', 'w', encoding='UTF-8') as f2:

    count = 0
    lines_liuke = f_liuke.readlines()
    for l in lines_liuke:
        count += 1
        splited_list = l.split('.')
        print(splited_list[0], end='\t')
        for i in splited_list[1:]:
            f2.write(i)
    print('\n共计耗时' + str(time.time()-t) + '秒，处理了' + str(count) + '道题。')