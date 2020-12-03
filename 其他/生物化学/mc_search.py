d = {'abcdefg': '小红', 'cdefgh': '小白', 'abdert': '小绿', 'egfrmk': '小紫', 'ngroeg': '小黑', 
    'sgfgfgfg': '小橙', 'vmbvo5': '小彩', 'hudig634':'小宗', '21woo0o': '小青', '4783648': '小粉'}
questions = {}
# 分行导入章节txt文件，储存为字典
with open('shenghua_database.txt', 'r', encoding='UTF-8') as f:
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
    print('\n共检索到' + str(len(output_dict)) + '条结果！')
    return output_dict

while 1:
    keywords = input('请输入关键字，以半角空格作为分隔，按回车键提交：\n')
    od = search(keywords, questions)
    for key, value in od.items():
        print('\n' + key + '\n\t' + value)