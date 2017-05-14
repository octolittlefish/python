# print("let\'s go")
# print(r"let's go")
# print(r"c:\now")  # 加r输出原始字符串 r"c:\now"=="c:\\now"打印出来就是c:\now
# print("""i love you,
# all the time""")  # 输出多行语句
#
# print(2e10)  # 输出2的10次方
# c = str(5e19)
# print(c)  # 输出5e+19
# a = b = c = d = 10
# a += 1
# b -= 3
# c *= 10
# d /= 8
# print(d)  # 输出1.25
# print(3 ** 5)  # 输出3的五次方
#
# x, y = 4, 5
# small = x if x < y else y
# print(small)
# assert 3 > 4 # 断言 如果判断为FALSE 则抛出异常AssertionError

# favourite = 'FishC'
# for i in favourite:
#     print(i, end=" ")
# print('\n')

# member = ['小甲鱼', '小布丁', '黑夜']
# for i in member:
#     print(i, len(i))

# for i in range(2, 9):  # 2-8
#     print(i)
# for i in range(5):  # 0-4
#     print(i)
# for i in range(1, 10, 2):  # 1-10 以2增加
#     print(i)

# for i in range(10):
#     if i % 2 != 0:
#         print(i)
#         continue
#     i += 2
#     print(i)

# member = ['小甲鱼', '小布丁', '黑夜']
# print(member)
#
# mix = [1, '小甲鱼', '3.14', member]
# print(mix)
# mix.append('葫芦娃')
# print(mix)
# mix.extend(['1', '2'])
# print(mix)
# mix.insert(0, 'first')
# print(mix)
#
# mix.remove('first')  # 去除元素
# print(mix)
# del member[1]
# print(mix)
# mix.pop()
# mix.pop(0)
# print(mix)
#
# list1 = mix[0:2]
# print(list1)
# list2 = mix[:]  # 不改变mix，改变的是mix的拷贝

# list1 = [123]
# list2 = [234]
# print(list1 < list2)
# list1 = [300, 45]
# list2 = [234, 123]
# print(list1 > list2)
# list3 = list1 + list2
# print(list3)
# list3 *= 2
# print(list3)
# print(45 in list3)
# print(list3.count(45))
# print(list3.index(123))
# print(list3.index(123, 4, 8))  # 4-8中找 不包括8
# list3.reverse()  # 把list3反转
# print(list3)
# list3.sort()  # 从小到大排序
# print(list3)
# list3.sort(reverse=True)
# print(list3)

# tuple1 = (1, "2", 3, 4, 5, 6, 7)
# print(tuple1[0])
# print(tuple1[5:])
# print(tuple1[:3])
# tuple2 = tuple1[:]
# tuple3 = (1,)
# tuple4 = ()  # 创建新元组
# tuple5 = tuple2 * 8
# tuple6 = ('1', '2', '3', '4')
# tuple6 = tuple6[:2] + ('5',) + tuple6[2:]  # 内容为1，2，3，4，5的元组
# print('1' in tuple6)
# del tuple6  # 删除元组
#
# list1 = [1, 2, 3]
# print(1 in list1)

# str1 = 'i love you'
# print(str1[2:])
# print(str1[:2] + "really " + str1[2:])  # str1并未改变
# str1 = str1[:2] + "really " + str1[2:]  # str1改变
# str2 = 'xiao xie'
# print(str2.capitalize())  # 首字母大写
# str2 = 'DAXIExiaoxie'
# print(str2.swapcase())  # 大小写翻转
# print(str2.casefold())  # 全部转小写
# print(str2.count('xi'))  # 检查xi出现次数
# print(str2.endswith("xie"))  # 检验是否以xie结束
# str3 = 'i\tlove\tyou'
# print(str3.expandtabs(2))  # 把\t转为空格 并设置空格为2个字符
# print(str2.find("i"))  # 寻找xi出现的位置，并返回下标，不存在则返回-1
# str4 = 'aaaabbbbaaa'
# print(str4.translate(str.maketrans('a', 'b')))

# 格式化
# print("{0} love {1}.{2}".format("I", "fishC", "com"))
# print("{a} love {b}.{c}".format(a="I", b="fishC", c="com"))
# print("{{0}}".format("不打印"))  # {0}不能解释为顺序替换了，不替换
# print('{0:.1f}{1}'.format(27.551, 'GB'))
# print('%c' % 97)  # 显示ascll码对应的元素
# print('%c %c %c' % (97, 98, 99))
# print('%d + %d = %d' % (97, 98, 97 + 98))
# print('%o' % 10)  # 显示ascll码对应的元素 十进制数字10转为8进制数字
# print('%#o' % 10)  # 显示ascll码对应的元素 十进制数字10转为8进制数字并有0o前缀
# print('%10.2f' % 2.111)
# print('%-10.2f' % 2.111)
# print('%e' % 2222222222222)  # 科学计数法

# 序列
# b = 'i love fishC.com'
# b = list(b)  # b成为一个字符列表
# print(b)
# c = (1, 1, 2, 3, 5, 8, 13, 21, 34)
# c = list(c)
# print(c)
# print(len(c))
# print(max(c))
# numbers = [1, 2, 3, 4, 5, 5, 45, 12, 2, 5]
# print(max(numbers))
# chars = '123456789'
# print(min(chars))
# print(sum(c))
# print(sorted(c))  # 这句话改变了c
# print(c)
#
# # print(reversed(c)) # 返回一个迭代器 这个函数不会改变c
# print(list(reversed(c)))
# print(c)
# print(list(enumerate(numbers)))  # 枚举numbers
#
# a = [1, 2, 3, 4, 5, 6, 7]
# b = [2, 3, 4, 5]
# print(list(zip(a, b)))

# def MyFirstFunction():
#     print('my first function')
#     print('i am nervous')
#
#
# MyFirstFunction()


# def addit(a, b):
#     'a,b是形参'
#     # 他只是一个形式，表示占一个位置
#     print(a + b)
#
# addit(1, 2)
# print(addit.__doc__)  # 函数的介绍
# print(print.__doc__)  # print函数的介绍

# def addtwo(a, b):
#     return a + b
#
# print(addtwo(1, 2))

# def saysome(name, words):
#     print(name + "->" + words)
#
#
# saysome(words="让编程改变世界！", name="小甲鱼")  # 自动匹配

# def saysome(name='小甲鱼', words='吃饭'):  # 默认值
#     print(name + "->" + words)
#
#
# saysome()
# saysome("fish")
# saysome("fish", "breath")

# def test(*params):
#     print("参数的长度是:", len(params))
#     print("第二个参数是", params[1])
#
#
# test(1, 2, 5, 4, 2, 5, "55564")

# def test(*params, exp=8):
#     print('参数的长度是：', len(params), exp)
#     print('第二个参数是:', params[1])
#
#
# test(1, '小甲鱼', 3.14, 5, 6, 7, exp=9)

# def back():
#     return 1, 2, 3
#
#
# print(back())

# count=5
# def myfun():
#     count=10
#     print(count)
#
# myfun()
# print(count)

# count = 5
#
# def myfun1():
#     global count
#     count = 10
#     print(count)
#
# myfun1()
# print(count)

# def fun1():
#     print('fun1()')
#
#     def fun2():
#         print('fun2()')
#     fun2()
#
# fun1()


# def funx(x):
#     def funy(y):
#         return x*y
#     return funy
#
# i=funx(8)
# print(i(5))
#
# print(funx(8)(5))

# def fun1():
#     x=5
#     def fun2():
#         nonlocal x
#         x*=x
#         return x
#     return fun2()
# print(fun1())

# def fun1():
#     x=[5]
#     def fun2():
#         x[0]*=x[0]
#         return x
#     return fun2()
# print(fun1())

# lambda表达式表达匿名函数
# g = lambda x: 2 * x + 1
# print(g(5))

# x=filter(None,[1,0,False,True])
# print(list(x))

# def odd(x):
#     return x % 2   # 奇数返回1，偶数返回0
#
#
# temp = range(10)
# show = filter(odd, temp)  # 过滤掉0
# print(list(show))

# print(list(filter(lambda x: x % 2, range(10))))

# print(list(map(lambda x:x*2,range(10))))

# 递归

# def recursion(x):
#     if x == 1:
#         return 1
#     else:
#         return x*recursion(x-1)
#
# print(recursion(5))

# 迭代
# def fab(n):
#     n1 = 1
#     n2 = 1
#     n3 = 1
#     if n < 1:
#         print('输入有误')
#         return -1
#     while (n - 2) > 0:
#         n3 = n2 + n1
#         n1 = n2
#         n2 = n3
#         n -= 1
#     return n3
#
#
# print(fab(20))

# 递归
# def fib(n):
#     if n < 1:
#         print('输入有误')
#         return -1
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
#
# print(fib(20))

# 汉诺塔
# def hanoi(n, x, y, z):
#     if n == 1:
#         print(x, '-->', z)
#     else:
#         hanoi(n - 1, x, z, y)  # 前n-1个移动到y上
#         print(x, '-->', z)  # 最后一个移动到z上
#         hanoi(n - 1, y, x, z)  # 前n-1个移动到z上
#
#
# hanoi(6, "x", "y", "z")

# 字典
# dict1 = {'lining': '一切皆有可能', 'nike': 'just do it', 'adidas': 'impossible is nothing'}
# print(dict1['lining'])
#
# dict2 = dict((('a', 20), ('b', 15)))
# print(dict2['a'])
#
# dict3 = dict(a='ww',b='dd')
# print(dict3['a'])
# dict3['a']=5
# print(dict3['a'])
# dict3['c']=6
# print(dict3['c'])

# dict1 = {}
# dict1.fromkeys((1, 2, 3))  # value=none
# print(dict1.fromkeys((1, 2, 3), '帅哥'))
# print(dict1.fromkeys((1, 3), '美女'))  # 新建字典
# dict1=dict1.fromkeys(range(20),'handsome')
# print(dict1.keys())
# for each in dict1.keys():
#     print(each)
# for each in dict1.values():
#     print(each)
# for each in dict1.items():
#     print(each)
# print(dict1[1])
# print(19 in dict1)
# b=dict1.copy() #复制
# print(b)
# print(dict1)
# dict1.clear()
# print(dict1)

# a = {1: '2', "我": '3', 3: '4'}
# a.pop("我") # 去掉key为'我'的一项
# print(a)
# a.popitem() # 去掉第一项
# print(a)
# a.setdefault('white')  # 添加新项,value为none
# print(a)
# a.setdefault('black', 5)  # 添加新项
# print(a)
# a['white'] = 6  # 给a赋值
# print(a)
# b = {'white': 666}
# a.update(b)  # 用b来更新a
# print(a)

# 集合 没有顺序,不能保持原来顺序
# num1 = {1, 2, 3, 4, 5, 4, 0}
# print(num1)
#
# set1 = set([1, 2, 3, 4, 5, 5])
# set1.add(6)
# set1.remove(2)
# print(set1)
#
# num1 = list(set(num1))
# print(num1)
#
# num1 = frozenset([1, 2, 3, 4, 5, 6])  # 不可改变的set

# 文件
# f = open('G:\\sad.txt', 'r', encoding='utf-8')
# print(f)
# print(f.read())
# f.seek(9, 0) #  指针从正向数第十个字符开始
# print(f.readline())
# f.seek(0, 0)
# for eachline in f:
#     print(eachline)

# f = open('G:\\sad.txt', 'a', encoding='utf-8')
# f.write("入骨相思知不知")


# def writeFile(boy, girl, count):
#     file_name_boy = 'boy_' + str(count) + '.txt'
#     file_name_girl = 'girl_' + str(count) + '.txt'
#
#     boy_file = open(".\\res\\" + file_name_boy, 'w')
#     girl_file = open(".\\res\\" + file_name_girl, 'w')
#
#     boy_file.writelines(boy)
#     girl_file.writelines(girl)
#
#     boy_file.close()
#     girl_file.close()
#
#
# def splitFile(name):
#     f = open(name)
#
#     boy = []
#     girl = []
#     count = 1
#
#     for each_line in f:
#         if each_line[:6] != '======':
#             (role, line_spoken) = each_line.split(':', 1)
#             if role == '小甲鱼':
#                 boy.append(line_spoken)
#             if role == '小客服':
#                 girl.append(line_spoken)
#         else:
#             writeFile(boy, girl, count)
#             boy = []
#             girl = []
#             count += 1
#     writeFile(boy, girl, count)
#     f.close()
#
#
# splitFile('record.txt')



# import os
# os.getcwd()
# os.chdir('E:\\')
# os.listdir('E:\\')
# os.mkdir('E:\\C')
# os.makedirs('E:\\C\\sad\\sada')
# os.remove('E:a.txt')  #删除单个文件
# os.rmdir('E:\\C\\sad\\sada')   #删除单个目录
# os.removedirs('E:\\C')  #删除多个目录 遇到非空目录则抛出异常
# os.system('cmd')










