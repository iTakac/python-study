# coding:utf-8

# 関数
def double(x):
    return x * 2

print (double(2))


def apply_to_one(f):

    return f(1)

my_double = double
x = apply_to_one(my_double)

print (double)
print (x)


def my_print(message="my default message"):
    print (message)

my_print("hello")
my_print()
