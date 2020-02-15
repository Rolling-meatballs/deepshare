import os

with open('db.txt', mode='r', encoding='utf-8') as read_f, \
        open('db.txt.swap', 'w', encoding='utf-8') as write_f:
    s = set()
    for line in read_f:
        if line not in s:
            s.add(line)
            write_f.write(line)

os.remove('db.txt')
os.rename('db.txt.swap', 'db.txt')