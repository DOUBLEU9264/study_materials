import time

def clean(text):
    '''处理文本以便于比较'''

    # 去掉所有空格
    text = text.replace(' ', '')
    # 去掉所有逗号
    text = text.replace('，', '')
    # 去掉所有句号
    text = text.replace('。', '')
    # 去掉答案
    text = text.split('@')[0]
    # 去掉中文括号
    text = text.split('（')[0]
    # 英文转换为小写
    text = text.lower()

    return text

t = time.time()
with open('bingli_db.txt', 'r', encoding='UTF-8') as f_lihua, \
    open('liuke_db.txt', 'r', encoding='UTF-8') as f_liuke:
    #open('六联去重后.txt', 'w', encoding='UTF-8') as f3:

    # 提取两科题目，储存为两个列表
    lines_lihua = f_lihua.readlines()
    lines_liuke = f_liuke.readlines()

    count_chong = 0
    count_liuke = 0
    for line_liuke in lines_liuke:
        count_liuke += 1
        count_lihua = 0
        for line_lihua in lines_lihua:
            count_lihua += 1
            if clean(line_liuke) == clean(line_lihua):
                count_chong += 1
                output = '六科第' + str(count_liuke) + '题与理化第' + str(count_lihua) + '题重复'
                print(output)
                break
        #else:
        #    f3.write(line_liuke)

    print('\n共计耗时' + str(time.time()-t) + '秒，有' + str(count_chong) + '道重复。')
