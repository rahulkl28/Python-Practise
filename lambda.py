y = lambda a: a + 10
print(y(5))


x = lambda a, b: a * b
print(x(5,6))



def myfunc(n):
    return lambda a : a * n
mytripler = myfunc(3)
mydoupler = myfunc(12)

print(mydoupler(2))
print(mytripler(11))
