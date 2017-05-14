import random

secret = random.randint(1, 8)  # 生成1-8的int数值 包括1和8
print(secret)
guess = 0
times = 0
while guess != secret and times < 3:
    temp = input("猜一下我想哪个数字")  # input返回字符串类型 赋值给temp
    if temp.isdigit():
        guess = int(temp)  # temp转化为int型 赋值给guess
        if guess == secret:
            print("你是我心里的蛔虫吗？！")
            print("猜中了也没有奖励")
        else:
            if guess > secret:
                print("哥,大了大了")
            else:
                print("嘿,小了！小了!")
    else:
        print("请输入数字类型的值")
    times += 1
print("游戏结束,不玩了")


