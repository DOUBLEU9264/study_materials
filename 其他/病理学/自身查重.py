import time

def clean(text):
    '''处理文本以便于比较'''

    # 去掉题号
    text = text.split('.')[1]
    # 去掉答案
    text = text.split('@')[0]
    # 去掉中文括号
    text = text.split('（')[0]
    # 去掉所有空格
    text = text.replace(' ', '')
    # 去掉所有逗号
    text = text.replace('，', '')
    # 去掉所有句号
    text = text.replace('。', '')
    # 英文转换为小写
    text = text.lower()

    return text


t = time.time()
with open('a1_db.txt', 'r', encoding='UTF-8') as f_liuke, \
    open('a1去重后.txt', 'w', encoding='UTF-8') as f2:

    # 分行提取六联题目，储存为列表lines_liuke
    lines_liuke = f_liuke.readlines()

    count = 0
    for num_1st, line_1st in enumerate(lines_liuke):
        for num_2nd, line_2nd in enumerate(lines_liuke):
            if clean(line_1st) == clean(line_2nd) and num_1st < num_2nd:
                count += 1
                output = '第' + str(num_1st + 1) + '行与第' + str(num_2nd + 1) + '行重复'
                print(output)
                break
        else:
            f2.write(line_1st)



print('\n共计耗时' + str(time.time()-t) + '秒，有' + str(count) + '道重复。')
