x = "Hello World!"

print(len(x))



class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


class Boat(Car):
    def move(self):
        print("Sail!")


class Plane(Car):
    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")



for x in (car1, boat1, plane1):
    x.move()


#GLobal Scope

x = 300

def myfunc():
    # global x 
    x = 150
    print(x)


myfunc()

print(x)