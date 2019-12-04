import functools
import time
from functools import reduce


# 高阶函数（函数参数传入函数）     map、reduce
def fn(x):
    return x + 1


def add_fn(x, y):  # x是累加器，一开始是前两个元素
    return x * 10 + y


def is_odd(n):
    return n % 2 == 1


# 返回一个迭代器   # 第二个参数传的是Iterable（即迭代器也可以）     # 返回迭代器
iteratorList = map(fn, [1, 2])  # 前端的使用[1，2].map(fn),map会自动遍历数组传进fn函数中
print(list(iteratorList))  # 将迭代器转为list数组
iteratorList = map(str, [1, 2])  # 转换成str
print(list(iteratorList))
# 返回一个迭代器   # 第二个参数传的是Iterable（即迭代器也可以）     # 返回迭代器
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))  # 前端使用[1, 3, 5, 7].filter((item, index) =>{return item>5})
# 返回add_fn函数的return
print(reduce(add_fn, [1, 3, 5, 7, 9]))  # 前端使用[1, 3, 5, 7, 9].reduce((add, item, index) =>{return add})


# 排序sorted(数组、 执行的函数、 逆序)
sortList = sorted([7, 4, -76, 9, -18, 32, 1, 44], key=abs, reverse=True)  # 前端用法arr.sort((ａ，ｂ) =>　{　return a - b　})
print(sortList)


def by_score(t):  # 按年龄排序，加负号表示高到低
    return -t[1]


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L, key=by_score)
print(L2)


# 解决闭包的两种方式
# 引入堆变量
def createCounter():
    fs = [0]

    def counter():
        fs[0] += 1
        return fs[0]

    return counter


# 使用nonlocal:上一级函数中的局部变量，多用于函数嵌套   global：全局
def createCounter():
    num = 0

    def counter():
        nonlocal num
        num += 1
        return num

    return counter


# 匿名函数
anonymous_functions = lambda x, y: x if x > y else y  # lambda匿名函数 + 三元运算
print(anonymous_functions(102, 101))


# 装饰器 - 在代码运行期间动态增加功能的方式,接受一个函数作为参数，并返回一个函数
def log(func):
    @functools.wraps(func)      # wrapper.__name__ = func.__name__，详见108行
    def wrapper(*args, **kwargs):
        print('函数名：' + func.__name__)
        func(*args, **kwargs)
    return wrapper


def log2(text):             # 装饰器传参数
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('装饰器传参数:' + text)
            func(*args, **kwargs)
        return wrapper
    return decorator


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.time()
        fn(*args, **kwargs)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, end - start))
        return fn(*args, **kwargs)
    return wrapper


@log
def getTime():
    print('2019/12/4')


@log2('你好')
def getTime2():
    print('2019-12-04')


getTime()   # 执行函数时，等效log(getTime),并执行返回的函数
getTime2()  # 执行函数时，等效log2('你好')(getTime2),并执行返回的函数
print(getTime.__name__)     # 如果不加@functools.wraps(func) 会变成wrapper
# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)      # time.sleep()睡觉、time.time()获取时间
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

