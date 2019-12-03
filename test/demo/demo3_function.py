# -*- coding: utf-8 -*-
import math

# 函数/方法 - 前端定义方式function name(){}  es6语法()=>{}

print(abs(-20))  # 绝对值   前端:Math.abs()
print(hex(65535))  # 转16进制
print()


def my_function(a=1):  # 定义函数
    if not isinstance(a, (int, float)):  # 判断函数参数类型
        raise TypeError('The type of the parameter is not a column')
    if a > 5:
        print('输入的数值大于5')
    else:
        print('输入的数值小于5')
    return 3, 4  # 返回多个值，默认以元组tuple形式


def add_end(i=None):
    if i is None:
        i = []
    i.append('END')
    return i


def quadratic(a, b, c):  # math.sqrt()开方
    return (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a), (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)


def run_arguments(a, b, *arguments):
    print(arguments)


def keyword_arguments(a, b, **kw):
    print(kw)


def name_arguments(name, *args, age):
    print(name, args, age)


my_function()  # 默认参数必须指向不变对象！
x, y = my_function(10)
print(x, y)

# 测试:
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

run_arguments(1, 2, 3, 4, 5)  # *arguments可变参数，多余参数解析为元组
keyword_arguments(5, 5, name='alex')  # **kw关键字参数，多余参数解析为对象
name_arguments('alex', age=18)  # 命名关键字参数，就是可变形参后面的参数必须使用命名的方式传参


def product(*args):
    if args:
        acl = 1
        for i in args:
            acl *= i
        return acl
    else:
        raise TypeError('write by ss')


# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()       # 传空的时候应该报异常raise TypeError('write by ss')
        print('测试失败!')
    except TypeError:   # 抛异常
        print('测试成功!')

