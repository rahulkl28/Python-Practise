a = 200
b = 35
c = 31

if b  > a:
    print("b >> a")
elif a == b:
    print("a == b")
else:
    print("a >> b")

#And / or operator

if a > b and c > a:
    print("true")

if not a > b:
    print("a is not greater than b")


#nested if

if a > b:
    print("re")
    if b > c:
        print("tr")


#While loops

i = 1
# while i < 6:
#     print(i)
#     if i == 4:
#       break
#     i += 1

while i < 6:
    i += 1
    if (i == 5):
        continue
    print(i)


# For loops

x = ["apple","banana", "cherry"]
for i in x:
    print(i)
    if i == "banana":
        break

for x in range(6,20,3):
    if x == 15: break
    print(x)


#Nested loops

a = ["red", "big", "cherry"]
b = ["apple", "banana", "cherry"]

for x in a:
    for y in b:
        print(x, y)


#Functions

# calling a func

def my_func(fname):
    print(fname + " surname")
my_func("Sam")


# Keyword Arguments

def my_function(fname,lname):
  print( fname + "last name is " + lname)

my_function(fname = "Sam ", lname = "Refsnes")


# Arbitrary Arguments, *args

def my_fun(*kid):
    print(kid[1])
my_fun("aman", "tom")


#Arbitrary Keyword Arguments, **kwargs

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


#Return Values

def my_function(x):
    return 5*x
print(my_function(3))
print(my_function(5))
print(my_function(9))


i = 2
j = 4

i = i + j
j = i - j
i = i - j
print(i)
print(j)

#Recursion

# def recursive(k):
#     if(k > 0):
#         result = k + recursive(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result

# recursive(6)