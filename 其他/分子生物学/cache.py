with open('fensheng.txt', 'r', encoding='UTF-8') as f1,\
    open('fensheng.strip.txt', 'w', encoding='UTF-8') as f2:

    lines = f1.readlines()

    for l in lines:
        f2.write(l.strip() + '\n')