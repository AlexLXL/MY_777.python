# 函数/方法 - 前端定义方式function name(){}  es6语法()=>{}

print(abs(-20))  # 绝对值   前端:Math.abs()
print(hex(65535))  # 转16进制


def my_function(a):     # 定义函数
    if not isinstance(a, (int, float)):     # 判断函数参数类型
        raise TypeError('The type of the parameter is not a column')
    if a > 5:
        print('输入的数值大于5')
    else:
        print('输入的数值小于5')
    return 3, 4     # 返回多个值，默认以元组tuple形式


x, y = my_function(10)
print(x, y)
