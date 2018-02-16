from types import MethodType

class Duck(object):
    def __init__(self, name, func1=None, func2=None):
        self.name = name
        if func1 is not None and func2 is not None:
            self.fly = MethodType(func1, self)
            self.quack = MethodType(func2, self)

    def fly(self):
        print("I can fly")

    def quack(self):
        print("I can quack")

    def __str__(self):
        return self.name

def cannofly(self):
    print("I can not fly")

def quacklikebird(self):
    print("I can quack like a bird")

class CanFly(object):
    @staticmethod
    def canfly(self):
        print("I can fly")

class CanNoFly(object):
    @staticmethod
    def cannofly(self):
        print("I can not fly")

class QuackLikeBird(object):
    @staticmethod
    def quacklikebird(self):
        print("I can quack like a bird")

class QuackLikeDog(object):
    @staticmethod
    def quacklikedog(self):
        print("I can quack like a dog")

if __name__ == '__main__':
    donald = Duck('Donald', CanNoFly.cannofly, QuackLikeBird.quacklikebird)
    print(donald)
    donald.quack()
    donald.fly()
    # donald.quack()
