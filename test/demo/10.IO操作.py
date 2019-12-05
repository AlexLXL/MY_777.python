import os
# f = open('./test.txt', 'r')
# print(f.read())
# f.close()

# 上面简写成 with as
# 执行open() 返回实例对象并执行实例中的__enter__，__enter__返回值赋值给f，执行下面的代码，最后执行实例的__exit__
# errors='ignore' 遇到非法字符时忽略
with open('./test.txt', 'r', encoding='UTF-8', errors='ignore') as f:
    content = f.read()      # 读完
    # size = f.read(256)      # 256字节
    # lines = f.readlines()   # 读完，按行返回list
    # line = f.readline()     # 一行
    print(content)
    # print(size)
    # print(line)
    # print(lines)

with open('./test1.txt', 'w') as f:     # w-删除文件重新写入
    f.write('KO')

with open('./test1.txt', 'a') as f:     # a-追加内容
    f.write('KO')


print('\n',os.name)         # 操作系统类型：posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.environ)           # 操作系统环境变量os.environ.get('PATH')
print(os.path.abspath('.')) # 当前目录路径
print(os.path.join('\\user\\lang', 'testdir'))              # 拼接目录  linux：part-1/part-2     window：part-1\part-2
print(os.path.split('/Users/michael/testdir/file.txt'))     # 拆分路径(/Users/michael/testdir, file.txt)
print(os.path.splitext('/path/to/file.txt'))                # 拆分文件后缀名
# os.mkdir('./testdir1')    # 新建目录
# os.rmdir('./testdir1')    # 删除目录
# os.rename('test1.txt', 'test1.py')    # 重命名文件
os.remove('test1.py')                   # 删除文件
