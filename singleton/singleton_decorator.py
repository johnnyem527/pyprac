def singleton(cls, *args, **kwargs):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return getinstance

@singleton
class MyClass:
    a =1

if __name__ == '__main__':
    my_class1 = MyClass()
    my_class2 = MyClass()
    print(my_class2 == my_class1)