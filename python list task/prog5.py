List = [53,2,4,76,25,98,13,57]

n = len(List)

# prog5

i = 0
j = n - 1

while(i < j):
    temp = List[i]
    List[i] = List[j]
    List[j] = temp
    i+=1
    j-=1


print(List)

# List.reverse()