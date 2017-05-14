# class MyDecriptor:
#     def __get__(self, instance, owner):
#         print("getting...",self,instance,owner)
#     def __set__(self, instance, value):
#         print("setting...",self,instance,value)
#     def __delete__(self, instance):
#         print("deleting...",self,instance)
#
# class Test:
#     x = MyDecriptor()
#
# test = Test()
# test.x
# test.x="X-man"
# del  test.x
# print(123)

class Celsius:
    def __init__(self,value = 26.0):
        self.value = float(value)
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value=float(value)
class Fahrenheit:
    def __get__(self, instance, owner):
        return instance.cel * 1.8 +32
    def __set__(self, instance, value):
        instance.cel=(float(value)-32)/1.8

class Temperature:
    cel = Celsius()
    fah = Fahrenheit()

temp =Temperature()
print("初始摄氏温度是: ")
print(temp.cel)
temp.cel = 30
print("摄氏温度设置为")
print(temp.cel)
print("对应华氏温度是: ")
print(temp.fah)
