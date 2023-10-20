List = [53,2,4,76,25,98,13,57]

n = len(List)


#prog1

for i in List:
    temp = List[0]
    List[0] = List[n - 1]
    List[n - 1] = temp
    print(List)

#prog2

# print(n)

# print(len(List))
    
count = 0

for i in List:
    count = count + 1
    print(count)







