theset = {"apple", "banana", "cherry", "apple"}
print(theset)

#True and 1 are same in sets

print(len(theset))
print(type(theset))

#loop
for x in theset:
    print(x)


#Add items 

theset.add("orange")
print(theset)

thisset = {"pineapple", "mango", "papaya"}
theset.update(thisset)

print(theset)

#remove item

theset.remove("banana")
theset.discard("banana")

print(theset)


#Join two sets

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

set3 = set1.union(set2)
print(set3)

#print only duplicates

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)

z = x.intersection(y)
print(z)

#Not duplicates

x.symmetric_difference_update(y)
print(x)

z = x.symmetric_difference(y)
print(z)