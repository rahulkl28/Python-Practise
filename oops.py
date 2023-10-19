class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)



#__init__() function

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


#__str__()

class Person:
    def __init__(set, name, age):
        set.name = name
        set.age = age

    def __str__(set):
        return f"{set.name}({set.age})"

p1 = Person("John" , 54)

print(p1)


#Object Methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("hello " + self.name)

p1 = Person("Johnathan", 21)
p1.age = 40
print(p1.age)
p1.myfunc()


