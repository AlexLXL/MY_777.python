# print
# assert断言，例: assert n != 0, 'n is zero!'   关闭断言：python -O xxxx.py
# logging
# pycharm debug - F7步入 F8步过 alt+F9执行到下一个断点
import unittest


def foo(s):
    s += 1
    return s


def bar(i):
    i = i + 1
    foo(i)
    return True


def main(t):
    bar(t)
    foo(10)


main(1)


# 单元测试
# import unittest           # 导入单元测试模块
# from mydict import Dict
#
# class TestDict(unittest.TestCase):
#
#     def test_init(self):
#         d = Dict(a=1, b='test')
#         self.assertEqual(d.a, 1)              # 断言是否相等
#         self.assertEqual(d.b, 'test')
#         self.assertTrue(isinstance(d, dict))  # 断言是否为True
#
#     def test_keyerror(self):
#         d = Dict()
#         with self.assertRaises(KeyError):     # 下面的代码是否抛出KeyError异常
#             value = d['empty']
#
#       def setUp(self):                            # 打开数据库(进行单元测试前的操作)
#           print('setUp...')
#
#       def tearDown(self):                         # 关闭数据库(进行单元测试后的操作)
#           print('tearDown...')
#
# if __name__ == '__main__':
#     unittest.main()
