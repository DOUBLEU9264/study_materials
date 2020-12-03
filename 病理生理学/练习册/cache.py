# 写入数据库
import sqlite3

conn = sqlite3.connect('bingsheng.db')
c = conn.cursor()
# c.execute('CREATE TABLE phrases (phrase text, explanation text)')
c.execute('CREATE TABLE choices (question text, answer text)')

# 读取txt文件
with open('病生选择.txt', 'r', encoding='utf-8') as f1:
    lines = f1.readlines()
    # qna = [(l.strip().split(':')[0], ':'.join(l.strip().split(':')[1:])) for l in lines]
    qna = [tuple(l.strip().split('@')) for l in lines]
    print(qna[:5])
    # c.executemany('INSERT INTO phrases VALUES (?, ?)', qna)
    c.executemany('INSERT INTO choices VALUES (?, ?)', qna)
    conn.commit()

# 关闭数据库
conn.close()