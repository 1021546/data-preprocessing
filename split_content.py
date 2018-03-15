import string
import os
from os import listdir
from os.path import isfile, join

# =============================================================================
# 初始化變數

qa_file = 'qa_40w.txt'
q_file = 'q.txt'
a_file = 'a.txt'
content_q = ''
content_a = ''

# =============================================================================
file_r = open(qa_file, 'r', encoding = 'utf8')
for i, line in enumerate(file_r.readlines()):
    line = line[:-1]
    content_q += line.split('\t')[0]+'\n'
    content_a += line.split('\t')[1]+'\n'
    print(i)
file_r.close()

# =============================================================================

file_w = open(q_file, 'w', encoding = 'utf8')
file_w.write(content_q)
file_w.close()
file_w = open(a_file, 'w', encoding = 'utf8')
file_w.write(content_a)
file_w.close()

print('Done') 
