# 把类作为第一个参数传入装饰器
def singleton(cls, *args, **kwargs):
    # 构建类 - 对象， 这样的键值对
    instances = {}

    def getinstance():
        # 如果该类-对象 键值不存在于字典里，那么在字典里加入该键值对
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    # 返回wrapper函数名
    return getinstance

@singleton
class MyClass:
    a =1

if __name__ == '__main__':
    my_class1 = MyClass()
    my_class2 = MyClass()
    print(my_class2 == my_class1)