# coding:utf-8

# タプル

my_list = [1,2]
print(my_list)
my_tuple = (1,2)
print(my_tuple)
other_tuple = 3,4
my_list[1] = 3
print(my_list)
try:
    my_tuple[1] = 3
except TypeError:
    print ("cannot change tuple")

# 関数から複数の値を返す
def sum_and_product(x,y):
    return (x + y),(x * y)

sp = sum_and_product(2,3)
print(sp)
s, p = sum_and_product(5, 10) # 多重割当
print(s, p)

s, p = p ,s # Python的値の交換
print(s, p)
