# _*_ coding:utf-8 _*_

import sys

# セット
'''
test_set_1 = {'python','-','izm','.','com'}
print(test_set_1)

print('------------------------------------')

for i in test_set_1:
    print(i)
'''

# スライス [開始位置:終了位置:ステップ幅]
'''
test_list = ['http','www','python','izm','com']
print(test_list[2:4])
print(test_list[::3])
'''

# インクリメント or デクリメント
'''
test_num = 100
print(test_num)

test_num += 1
print(test_num)
'''

# コマンドライン引数の取得

args = sys.argv
print(args)
print('第１引数：'+args[1])
