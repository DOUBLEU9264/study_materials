import itchat, random
from itchat.content import TEXT

questions = {}
# 分行导入章节txt文件，储存为字典
with open('linma_db.txt', 'r', encoding='UTF-8') as f:
    lines = f.readlines()
    for line in lines:
        l = line.split('@')
        questions[l[0]] = l[1]
print('数据库导入完毕...\n')


def search(keywords, target_dict):
    '''关键字检索'''

    output_dict = {}
    for key, value in target_dict.items():
        for keyword in keywords.split(' '):
            if keyword not in key:
                break
        else:
            output_dict[key] = value
    if len(output_dict) > 10:
        return '检索结果超过10条了！再添加一个关键字试试吧！'
    return_str = '共检索到' + str(len(output_dict)) + '条结果！\n'
    for key, value in output_dict.items():
        return_str += key + '\n    ' + value
    return return_str


@itchat.msg_register(TEXT, isFriendChat=True, isGroupChat=False, isMpChat=True)
def auto_reply(msg):
    '''自动回复'''

    global questions
    message = msg['Text']
    if '@' in message:
        return (search(message.replace('@', ' '), questions))
    elif message == '考试网址':
        return 'http://218.7.95.52:900/smuexam/1202/default.asp'


# itchat.auto_login(enableCmdQR=2, hotReload=True)
itchat.auto_login()
itchat.run()
