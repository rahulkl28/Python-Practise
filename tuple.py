thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple)
print(len(thistuple))
print(type(thistuple))

thetuple = tuple(("apple", "banana", "cherry"))
print(thetuple)

print(thistuple[2:5])
print(thistuple[:2])

print(thetuple[-2])

#change tuple values

y = list(thetuple)
y[1] = "pine"
y.append("coca")
thetuple = tuple(y)
print(thetuple)

#Add tuple to a tuple
y = ("orange",)
thetuple += y

print(thetuple)


#Unpacking Tuple

fruits = ("apple", "banana", "cherry")
(green, red, pink) = fruits

print(green)
print(red)
print(pink)

#using Asterisk

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)

mytuple = fruits * 2
print(mytuple)

x = thistuple.count(2)
x = thistuple.index("banana")
print(x)
