import time

t = time.time()
c = 0
status = 0
with open('病理学试题库.txt', 'r', encoding='UTF-8') as f1,\
    open('bingli处理后.txt', 'w', encoding='UTF-8') as f2:

    lines = f1.readlines()
    for l in lines:
        if '一、选择题' in l:
            status = 1
        elif '二、名词解释' in l:
            status = 0
        if status:
            f2.write(l)
            c += 1
    print('写入了%d行，耗时%.2f秒。' %(c, time.time()-t))