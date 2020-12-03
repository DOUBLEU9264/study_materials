with open('临床麻醉学习题集.txt', 'r', encoding='UTF-8') as f1:
    lines = f1.readlines()
    count = 0
    for l in lines:
        count += 1
        if l.count('@') == 0:
            print('第' + str(count) + '行无@')
        elif l.count('@') > 1:
            print('第' + str(count) + '行超过一个@')
            