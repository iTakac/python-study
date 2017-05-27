# coding:utf-8

from collections import defaultdict

# defaultdictクラス
document = {}
word_counts = defaultdict(int)
for word in document:
    word_counts[word] += 1

list = {2 : [1]}
dd_list = defaultdict(list)
print(dd_list[2])
