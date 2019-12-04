from collections.abc import Iterable
from collections.abc import Iterator

# 切片 - 数组、对象、字符串均可使用
nameList = [1, 2, 3, 4, 5]
print(nameList[1:3])  # 切片(左闭右开)，等效前端slice(1，3)
print(nameList[1:])
print(nameList[1:-1])

# 迭代 - 遍历
for i in [1, 2, 3]:
    print(i)
for k, v in {'name': 'alex', 'age': 18}.items():  # items()-迭代键、值，values()-迭代值，空-迭代键
    print(k, v)
isIterable = isinstance([1, 2], Iterable)  # 判断是否可迭代
print(isIterable)

for i, value in enumerate([11, 22, 33]):  # 数组遍历时增加下标(enumerate枚举)
    print(i, value)

# 数组生成式
foo = [x for x in range(5)]
print(foo)
foo = [x for x in range(1, 11)]
print(foo)
foo = [x * x for x in range(1, 11) if x % 2 == 0]
print(foo)
foo = [k + '吨' + v for k, v in {'name': 'alex', 'age': '19'}.items()]  # 字符串才能拼接，所以19加引号
print(foo)

# 生成器 - 只是一个算法，一般通过for循环调用（next(g)也可以，但很少使用）
g = (x for x in (44, 55))  # 数组生成式用在元组上
print(type(g))
for n in g:
    print(n)


def fib(num):           # 函数使用yield，每次调用会卡在yield
    x, a, b = 0, 0, 1
    while x < num:
        yield b
        a, b = b, a + b
        x = x + 1
    return 'done'


for n in fib(6):    # for循环调用是拿不到返回值得，因为数据就那么多，遍历次数也是那么多，而返回值是在StopIteration异常里面
    print(n)

g = fib(6)                          # 不能使用next(fib(6))--这样每次next的是一个新的fib函数
while True:
    try:
        print(next(g))
    except StopIteration as e:      # 获取返回值
        print(e.value)
        break


# 迭代器 - 生成器都是Iterator对象，即数组生成使生成的元组和yield的函数
#        - 表示一个数据流，可以被next()的
isinstance([], Iterator)        # False                # 判断是否是迭代器
isinstance(iter([]), Iterator)  # True                 # 数组、对象、字符串转换为迭代器

