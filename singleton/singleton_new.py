# -*- coding: utf-8 -*-

class Person(object):
    # __new__方法是静态方法
    # cls参数代表当前类
    def __new__(cls, name, age):
        print('__new__ called.')
        # 用父类调用__new__方法是为了避免死循环！
        # super().__new__(cls)是py3的写法
        # super(Person, cls).__new__(cls, name, age)是py2的写法
        return super().__new__(cls)

    def __init__(self, name, age):
        print('__init__ called.')
        self.name = name
        self.age = age

    def __str__(self):
        return '<Person: %s(%s)>' % (self.name, self.age)


# class Singleton(object):
#     def __new__(cls, *args, **kw):
#         '''
#         hasattr(object, name)
#         判断一个对象里面是否有name属性或者name方法，返回BOOL值，
#         有name特性返回True， 否则返回False。
#         需要注意的是name要用括号括起来
#         '''
#         if not hasattr(cls, '_instance'):
#             cls._instance = super().__new__(cls)
#         return cls._instance

class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

class MyClass(Singleton):
    a = 1
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    # test1
    # piglei = Person('piglei', 24)
    # print(piglei)
    pass
    my_class1 = MyClass('zs', 1)
    print(my_class1.__dict__)
    my_class2 = MyClass('ls', 1)
    print(my_class1.__dict__)
    print(my_class1==my_class2)




