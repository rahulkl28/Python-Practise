class Person:
    def __init__(self, fname,lname):
        self.fname = fname 
        self.lname = lname

    def printfun(self):
        print(self.fname, self.lname)

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

x = Person("John", "Wick")

y = Student("James", "Bond")

y.printfun()
x.printfun()


#super() keyword

class Person:
    def __init__(set, fname, lname):
        set.fname = fname
        set.lname = lname

    def printname(set):
        print(set.fname, set.lname)

class student(Person):
    def __init__(set, fname, lname, year):
        super().__init__(fname, lname)
        set.gradyear = year

z = student("Johny", "Walker", 2014)
z.printname()
print(z.gradyear)