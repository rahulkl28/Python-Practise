thislist = ["apple", "cake", "sweet"]
thislist[1:3] = ["cheery", "watermelon"]
thistuple = ("kiwi", "orange")


# thislist[2] = "cherry"
print(thislist)

print(len(thislist))
print(type(thislist))
print(thislist[-2:])

thislist.append("orange")
thislist.insert(1, "water")

thislist.extend(thistuple)

thislist.remove("apple")
thislist.pop(2)

# del thislist
# thislist.clear()

print(thislist)

#Loop lists

for x in thislist:
    print(x)

#Index Numbers

for x in range(len(thislist)):
    print(thislist[x])

#While loop
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)


#list() constructor

list1 = list((1,2,3))
print(list1)

if "apple" in thislist:
    print("Yes, it is present")



#sort list

thislist.sort()

#sort descending
thislist.sort(reverse = True)

#reverse order
thislist.reverse()

print(thislist)


#Copy List
mylist = thislist.copy()

#mylist = list(thislist)

print(mylist)



#Join two lsits

lista = [1,2,3]
listb = ["a", "b", "c"]
listc = lista + listb

print(listc)

for x in listb:
  lista.append(x)
print(lista)

listb.extend(lista)
print(listb)






