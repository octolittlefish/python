import random as r
class Fish():
    def __init__(self):
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)
    def move(self):
        self.x-=1;
        self.y-=1;
        print("我的位置是：",self.x,self.y)
class GoldFish(Fish):
    pass
class Carp(Fish):
    pass
class Salmon(Fish):
    pass
class Shark(Fish):
    def __init__(self):
        # Fish.__init__(self)
        super().__init__()
        self.hungry = True
    def eat(self):
        if(self.hungry==True):
            print("木啊木啊，好吃！")
            self.hungry=False
        else:
            print("好撑，不能吃了")
shark = Shark()
shark.move()
shark.eat()