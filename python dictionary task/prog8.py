string = "Python is great and Java is also great"
newstr = string.split()

new_str = ""
dict = {}



for char in newstr:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1

myList2 = list(dict.keys())

for i in myList2:
    new_str += i + " "

print(new_str)

