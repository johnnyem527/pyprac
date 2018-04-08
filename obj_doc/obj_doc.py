"这是模块文档字符串"

def foo():
    "这是函数声明文档字符串"
    pass

print(foo.__doc__)


class Foo:
    "这是类声明文档字符串"
    pass

foo = Foo()
print(foo.__doc__)
