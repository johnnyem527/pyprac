'''
写代码要遵循开发封闭原则，虽然在这个原则是用的面向对象开发，
但是也适用于函数式编程，简单来说，它规定已经实现的功能代码
不允许被修改，但可以被扩展，即：

封闭：已实现的功能代码块
开放：对扩展开发

函数在没有被调用之前其内部代码不会被执行。
'''

'''
1. 把@w1下面的方法作为参数传给w1方法
2. 将执行完的w1函数在重新赋值给原函数的函数名

'''
# 为什么装饰器不能这样写，是因为这样写的话，
# 即便不调用f1方法，也会执行3个print方法
# 执行流程是
# 1. 先把f1作为参数传给w1
# 2. 3个print, 然后返回f1
# 3. 然后把返回的f1函数赋给原来的f1函数
# 实际上f1函数没有变化，所以需要一个包装函数，
# 包装一下f1函数，并把这个包装好的函数赋值给原来的f1
# def w1(func):
#     print(1)
#     print(2)
#     print(3)
#     return func
#
# @w1
# def f1(name, age):
#     print(name, age)

# f1('nihao', 11)


def w2(func):

    def inner(name, age, gender):
        # 验证1
        print(1)
        # 验证2
        print(2)
        # 验证3
        print(3)
        print(name)
        print(age)
        print(gender)
        func(name, age)
        # return func(name, age)
    # 这里返回的已经不是以前的f2函数了
    # 而是新包装的f2函数，即inner函数
    return inner

# 加上装饰器之后f2已经不是f2了，而是inner
@w2
def f2(name, age):
    print(name, age)

# f2('是不是', 123, 'male')

'''
装饰器也带多个参数
'''
def decrator(*dargs, **dkargs):
    def wrapper(func):
        def _wrapper(*args, **kargs):
            print("decrator param:", dargs, dkargs)
            print("function param:", args, kargs)
            return func(*args, **kargs)
        return _wrapper
    return wrapper

@decrator(1, a=2)
def foo(x, y=0):
    print("foo", x, y)

#
# if __name__ == '__main__':
#     foo(3, 4)

#################################
#  函数带多个参数，装饰器能转换参数类型
def validate(**vkargs):
    def decorator(func):
        def wrapper(**kargs):
            for key in vkargs:
                # 根据vkargs中的参数的类型对kargs的参数进行类型转换
                kargs[key] = vkargs[key](kargs[key])
            return func(**kargs)
        return wrapper
    return decorator

@validate(x=int, y=float, z=float)
def move(x, y, z):
    print("move %d (%0.2f, %0.2f)"%(x, y, z))

if __name__ == '__main__':
    move(x="1", y="0.2", z="0.3")

##################################
##多个装饰器的调用顺序是自下往上，但是运行时的执行顺序是自上往下！！！
##################################