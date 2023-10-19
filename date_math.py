import datetime
import math

x = datetime.datetime.now()
print(x)

X = datetime.datetime(2015, 3, 4)
print(x.strftime("%B"))
print(X.strftime("%A"))


#MATH

y = min(9, 3, 5)
z = max(4, 2, 8)
i = math.sqrt(64)
a = abs(-23.4)
b = math.ceil(-12.3)
c = math.floor(-12.3)

j = pow(4,5)

print(j)

print(c)
print(b)
print(i)
print(a)
print(z)
print(y)