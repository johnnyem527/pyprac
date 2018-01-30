class SuperBaseClass:
    def hi(self):
        print("OK")

class ClassA(SuperBaseClass):
    pass
    def hi(self):
        print("Hello A!")

    def another(self):
        print("In Class A.")

class ClassB:
    def hi(self):
        print("Hello B!")

class ClassC(ClassB, ClassA):
    pass

c = ClassC()
c.hi()
c.another()