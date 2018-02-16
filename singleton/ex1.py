# class Singleton(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
# class Apple(Singleton):
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
# apple1 = Apple('apple')
# print(apple1)
# apple2 = Apple('birne')
# print(apple1)
# print(apple1 == apple2)

# class Singleton(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
# class Pig(Singleton):
#     a =1
#
# pig1 = Pig()
# pig2 = Pig()
# print(pig1 != pig2)

def singleton(cls, *args, **kwargs):
    __instance = {}

    def getinstance():
        if cls not in __instance:
            __instance[cls] = cls(*args, **kwargs)
        return __instance[cls]

    return getinstance

@singleton
class Duck(object):
    a = 1

duck1 = Duck()
duck2 = Duck()

print(duck1 == duck2)