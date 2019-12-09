from enum import Enum


class People(object):
    def __init__(self, name, score, password):  # 类似构造函数
        self.name = name
        self.score = score
        self.__password = password  # 私有属性，外部无法访问（隐藏为_People__password）

    def print_score(self):
        print("姓名：%s     成绩：%s" % (self.name, self.score))

    def get_password(self):  # 获取私有属性
        return self.__password

    def set_password(self, password):
        self.__password = password

    def run(self):
        print('人在跑步..')


class Student(People):
    def run(self):  # 多态
        print('学生跑步..')

    def go_to_school(self):
        print('去上学')


class Tacher(object):  # 类属性，通过类名.类属性访问
    count = 0

    def __init__(self, name):
        self.name = name
        Tacher.count += 1


class Scientists(object):
    __slots__ = ('name', 'age')  # 当前类实例允许绑定的属性名称，继承的子类不受限制


# king = People('tom', 20, 'L123456')
# king.print_score()
# king.set_password('LILLA')
# print(king.get_password())
# print(king.__dict__)            # 打印对象全部属性
# print(dir(king))                # 打印对象的所有属性和方法
# print(hasattr(king, 'name'))    # 获取、修改、判断是否存在某个属性getattr()、setattr()、hasattr()
# print(king.name, king.score)
#
# jack = Student('jack', 30, '5555')
# print(jack.__dict__)
# jack.run()              # 多态，继承后重写
# jack.go_to_school()
#
# s1 = Scientists()
# s1.name = '测试'
# s1.score = 1


# @property装饰器就是负责把一个方法变成属性调用的：    @weight.setter把方法变成属性修改
class Dog(object):
    def __init__(self):
        self._weight = 0

    @property
    def weight(self):  # 函数名和属性名一致
        return self._weight  # 使用的时候使用：self._属性名

    @weight.setter
    def weight(self, value):
        if not isinstance(value, int):
            raise ValueError('value no a int')
        elif value < 0 or value > 200:
            raise ValueError('value should between 0-200')
        self._weight = value  # 使用的时候使用：self._属性名


# hashiqi = Dog()
# print(hashiqi.weight)
# hashiqi.weight = 30
# print(hashiqi.weight)
# hashiqi.weight = '水'    # 报value no a int
# hashiqi.weight = 300     # 报value should between 0-200


class Animal(object):
    def eat(self):
        print('动物都会吃东西..')


class Runable(object):
    def run(self):
        print('我有跑的属性..')


class Cat(Animal, Runable):  # 多继承
    pass


# coffeeCat = Cat()
# coffeeCat.eat()
# coffeeCat.run()


class Bird(object):
    def __init__(self, name):
        self.name = name
        print('父类构造函数==')

    def singing(self):
        print('鸟会唱歌==')


class Bugu(Bird):
    def __init__(self, name, color):
        super(Bugu, self).__init__(name)  # super 调用构造函数
        self.color = color

    def singing(self):
        super(Bugu, self).singing()  # super 调用实例方法
        print('Bugu会唱歌')


# bugu = Bugu('bubu', 'skyblue')
# print(bugu.name, bugu.color)
# bugu.singing()


# 类的一些定制类
# def __str__(self):             打印实例的输出内容
# def __iter__(self)：
# def __next__ (self)：          使实例可迭代(能用for in)
# def __getitem__(self, n):      在上面可迭代的基础上，可以像数组一样使用：实例()[0]获取数据
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017590712115904
# def __getattr__(self, attr):   当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
#   if attr == 'score':
#         return 1
#   raise AttributeError('object has no attribute \'%s\'' % attr)

# def __call__(self)             该方法可以直接对实例进行调用，即instance()
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        print(path)
        return Chain('%s/%s' % (self._path, path))

    def __call__(self, path):  # 实例对象直接调用 s()
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


# username = 'michael'
# print(Chain('http://192.168.2.222:8080').status.user.timeline)  # http://192.168.2.222:8080/status/user/timeline
# print(Chain('http://192.168.2.222:8080').users(username).repose)  # 动态参数username:http://192.168.2.222:8080/status/user/timeline

# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
# callable(Chain)  # True
# callable(max)  # True
# callable('ssss')  # True


# 枚举类 - 可以枚举不能实例化，枚举类内有一个__members__包含所有属性
# 方式1：Enum构造器
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)

# 方式2：使用继承
class Week(Enum):
    Mon = 0
    Tue = 1
    Wed = 2
    Thr = 3
    Fri = 4
    Sat = 5
    San = 6


print(Week)  # <enum 'Week'>
print(Week.Mon)  # Week.Mon
print(Week.Mon.name)  # Mon
print(Week.Mon.value)  # 0
