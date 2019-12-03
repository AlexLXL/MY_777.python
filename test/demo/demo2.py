# 前端 - push后加、pop后减、shift前加、unshift前减
# 前端写法if(){} else if(){} finally{}

# 数组（list列表）- append后加、pop删特定位置、insert加特定位置
nameList = ['alex', 'game', 'tom']
print(nameList)
nameList.append('后加')
print(nameList)
nameList.insert(0, '0加')
print(nameList)
nameList.pop(-1)
print(nameList)

# 不可改变的数组（tuple元组）
nameTuple = (1, 2, 3)
nameTuple2 = (1,)  # 区别括号和元组

# 对象（dict字典）- 比js严谨，键值加单引号，添加使用tomDict['sex'] = '男'
tomDict = {'name': 'tom', 'age': 18}
print(tomDict)
tomDict['sex'] = '男'
print(tomDict)
print('name' in tomDict)  # name属性在不在tomDict对象里面（前端也可以使用，但前端会把原型链也搜索，前端不搜索原型链可以使用hasOwnProperty）

# 不重复的key，创建需使用list
onlySet = set([1, 2, 3, 4, 1, 2, 5])
print("\n", onlySet)
onlySet.add(7)  # 添加
onlySet.remove(1)  # 删除
print(onlySet)

# if判断
salary = input('\n输入工资：')
salary = int(salary)
if salary > 5000:
    print('你的工资大于5000')
elif salary >= 3000:
    print('你的工资有3000以上了')
else:
    print('继续加油')

# 前端for in 遍历的是对象，用来拿下标 for(var i in obj){ console.log(obj[i]) }
# 前端while巡检写法，while(i < 500){ i++ }

# for in 巡检遍历数组
print()
sum = 0
ageList = [18, 22, 33, 60, 78]
for i in ageList:
    sum += i  # 自增运算已经废弃
print(sum)

# while循环
weight = 140
while weight < 150:
    if weight == 145:
        break
    weight += 1
print(weight)

# 不可变类型：数字、字符串、元组
# 可变类型：数组（list）、对象（dict）
# 可变不可变，是指堆内存是否可以被改变
