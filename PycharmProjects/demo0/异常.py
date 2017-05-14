# my_list = ['小甲鱼是帅哥']
# my_list.pop()
# assert len(my_list) > 0   # AssertionError
#
# my_list = [1, 2, 3]
# a = my_list[3]  # IndexError
#
# my_dict = {'one': 1, "two": 2, 'three': 3}
# a = my_dict['four']  # KeyError

try:
    sum1 = 1 + "1"  # 一出现错误，try中的其它语句不执行，直接跳到相应的except程序段运行
    print(sum1)
    with open("不存在的.txt") as f:
        print(f.read())
except OSError as reason:
    print("文件出错了\n" + str(reason))
except TypeError as reason:
    print("类型出错\n" + str(reason))
finally:
    print("get it")  # 一定执行

try:
    a = int('123')
    print(a)
except ValueError as reason:
    print("出错了" + str(reason))
else:
    print("没错误")