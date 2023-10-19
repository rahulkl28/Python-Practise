import random

print("Hello, world")
print(random.randrange(1,10))

#if-else condition
a = 23
b = 3
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")


x = 5
z = 11

#convert from int to complex:
a = complex(x)

#covert from int to float:
b = float(z)

# print(a)
# print(b)
# print(type(a))
# print(type(b))

y = "Drop"
print(range(x))
print(type(x))
print(str(x))
print(x,y)

#unpacked variable
"""fruits = ["apple", "mango","pineapple"]
x, y, z = fruits
print(x)
print(y)
print(z)
print(x,y,z)"""


#global keyword

# def myFunc():
#     global x
#     x = "moon"

# myFunc()
# print(x[3])
# print("to the " + x)

txt = "  my name, is"
cd = "james"
d = txt + " " + cd
print(d)

print(txt[1:6])
print(txt[:6])
print(txt[5:])
print(txt[-4:-1])
print(txt.upper())
print(txt.strip())
print(txt.replace("n", "g"))
print(txt.split(","))

if "name" in txt:
    print("yes, it is present")

print("is" in txt)
for x in "banana":
    print(x)
    

#format strings
age = 21
state = 34
tx = "My name is John, I am {1} and state {0}"
print(tx.format(age, state)) 




#boolean
print(10>9)
print(10 == 9)
print(10<9)


print(bool(False))
print(bool(None))


class myclass():
    def _len_(self):
        return True

myobj = myclass()
print(bool(myobj))

x = 20.0
print(isinstance(x, int))

print(10 / 5)