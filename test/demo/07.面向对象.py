class People(object):
    def __init__(self, name, score, password):
        self.name = name
        self.score = score
        self.__password = password  # 私有属性，外部无法访问（隐藏为_People__password）

    def print_score(self):
        print("姓名：%s     成绩：%s" % (self.name, self.score))

    def get_password(self): # 获取私有属性
        return self.__password

    def set_password(self, password):
        self.__password = password

    def run(self):
        print('人在跑步..')


class Student(People):
    def run(self):      # 多态
        print('学生跑步..')

    def go_to_school(self):
        print('去上学')


class Tacher(object):   # 类属性，通过类名.类属性访问
    count = 0

    def __init__(self, name):
        self.name = name
        Tacher.count += 1


class Scientists(object):
    __slots__ = ('name', 'age')     # 当前类实例允许绑定的属性名称，继承的子类不受限制


king = People('tom', 20, 'L123456')
king.print_score()
king.set_password('LILLA')
print(king.get_password())
print(king.__dict__)            # 打印对象全部属性
print(dir(king))                # 打印对象的所有属性和方法
print(hasattr(king, 'name'))    # 获取、修改、判断是否存在某个属性getattr()、setattr()、hasattr()
print(king.name, king.score)

jack = Student('jack', 30, '5555')
print(jack.__dict__)
jack.run()              # 多态，继承后重写
jack.go_to_school()

s1 = Scientists()
s1.name = '测试'
# s1.score = 1
