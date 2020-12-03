with open('b单选答案.txt', 'r', encoding='UTF-8') as f1, open('b处理后答案.txt', 'w', encoding='UTF-8') as f2:
    text = f1.read().replace(' ', '')
    t = '1'
    for i in range(1, len(text)):
        if text[i-1] == '.':
            t += text[i] + ' '
        else:
            t += text[i]
    
    f2.write(t[:-1])