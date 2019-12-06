import pickle

print('hello Python!')

count = 1024 * 768
print('\n1024 * 768 = ', count, sep="")  # 逗号拼接打印  # seq是间隔符，默认是空格

print('''\nline1                          
line2''')  # 打印多行也可用\n换行

# name = input('\n请输入content:')         # input输入     # 动态语言，不用像java那样int num = 1这样静态定义
# print(name)

print('%.4f' % (10 / 3))  # 保留4个浮点数
print(9 / 3)  # 结果是浮点数3.0
print(11 // 3)  # 结果是向下取整
print(True and False)   # 布尔类型大写 and、or、not（与、或、非）

print(len("alex"))  # len()获取字符串、数组长度
print(' alex  '.strip())    # strip()去除前后特定字符串(传参)，默认空格 ## 等效前端的trim（）
print('AxCC'.lower())       # 小写
print("整数%d，浮点数%f，字符串%s" % (100, 3.14, '测试string'))  # 格式化字符串 - 整数%d，浮点数%f，字符串%s，十六进制帧数%x，如果不知道数据具体类型，可以统一使用%s


