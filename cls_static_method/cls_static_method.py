def get_no_of_instance(cls):
    return cls.no_of_instance

class Foo(object):
    no_of_instance = 0

    def __init__(self):
        Foo.no_of_instance += 1

foo1 = Foo()
foo2 = Foo()
print(foo1.no_of_instance)
print(get_no_of_instance(Foo))

def foo(*args):
    print("para: ", args)

foo('apple', 'birne', 'peach')

class Pig(object):
    pigs = []


pig1 = Pig()
pig1.pigs.append(1)
print(Pig.pigs)
pig2 = Pig()
pig2.pigs.append(2)
print(Pig.pigs)
print(pig1.pigs)

print(dir(str))

print(getattr(str, 'split'))


testmap = globals()
print(testmap['foo'])

print('my favor: {}'.format(['Emma', 'Chloe']))
