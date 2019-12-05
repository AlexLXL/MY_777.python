import logging
from functools import reduce

# try:
#     result = 10 / 0
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e, '\n')
#     logging.exception(e)        # 记录错误
# finally:
#     print('\n最后执行finally~')


# 常见错误链，根据调用追溯到源头
# Traceback (most recent call last):
#   File "err.py", line 11, in <module>
#     main()
#   File "err.py", line 9, in main
#     bar('0')
#   File "err.py", line 6, in bar
#     return foo(s) * 2
#   File "err.py", line 3, in foo
#     return 10 / int(s)
# ZeroDivisionError: division by zero

def foo(divisor):
    if divisor == 0:
        raise ValueError('divisor is zero')     # 抛出错误
    return 10 / divisor


foo(0)


# 练习
def str2num(s):
    try:
        return int(s)       # int()只能转换整数，int(7.6)报错
    except ValueError:
        return float(s)     # float()转换浮点数


def calc(exp):
    ss = exp.split(' + ')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()