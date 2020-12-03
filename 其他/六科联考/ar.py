import itchat, time
from itchat.content import TEXT

# 定义题目字典
questions = {}



def choose_db():
    '''导入数据'''

    global questions
    db = 'liulian.txt'
    try:
        # 分行导入题库txt文件，储存为字典
        with open(db, 'r', encoding='UTF-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print('文件不存在！请核对后重试。')
        exit()
    for line in lines:
        l = line.split('@')
        questions[l[0]] = l[1]
    print('\n数据库导入完毕...\n\n')


def search(keywords, target_dict):
    '''关键字检索'''

    count_finded = 0
    return_str = ''
    for key, value in target_dict.items():
        for keyword in keywords.split(' '):
            if keyword not in key:
                break
        else:
            if count_finded > 9:
                return '\n  检索结果超过10条了！再添加一个关键词试试吧！\n'
            else:
                count_finded += 1
                return_str += '\n  %d.%s\n    %s' %(count_finded, key, value)

    # 格式化返回字符串
    return_str = '\n  共检索到%d条结果！\n%s' %(count_finded, return_str)
    return return_str


# main
print('\n欢迎使用此查题程序！')
time.sleep(1)
print('\n请在“->”符号后输入关键词，')
time.sleep(1)
print('（熟悉微信版本的朋友请注意，软件版不需要使用@字符）')
time.sleep(1)
print('\n关键词之间以 空格键 分隔，且关键词数目无上限，\n')
time.sleep(1)
print('例如输入“细胞 区别于”，最后按回车键结束。')
time.sleep(1)
print('\n任何时候在“->”后输入“exit”以退出程序。')
time.sleep(1)
print('\n*郑重声明*：本程序仅供学习交流，请勿用于非法用途并于下载后24小时内删除。')
time.sleep(2)
choose_db()
while 1:
    key1 = input('->')
    if key1 == 'exit':
        break
    print(search(key1, questions))