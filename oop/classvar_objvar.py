class Person:
    count = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "姓名: " + self.name + "  年龄: " + str(self.age)


p1 = Person("张桂", 14)
p2 = Person("李慧儿", 22)

print(p1)
print(p2)

print(p1.count)
print(p2.count)
print(Person.count)
Person.count = 1
print(p1.count)
print(p2.count)
print(Person.count)
