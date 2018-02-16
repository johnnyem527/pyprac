# for immutable objects
a = 1
def foo(a):
    a = a + 1

foo(a)
print(a)

# for mutable objects
b = []
def foo_1(b):
    b.append(1)

foo_1(b)
print(b)

class Test(object):
    pass

print(type(Test))

test = type('test', (), {'name':'Johnny'})
print(test)
print(test().name)

print(object.__class__.__class__)

