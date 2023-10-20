List = [53,2,4,76,25,98,13,57]

n = len(List)

for j in range(len(List)):
    for i in range(len(List)-1):
        if(List[i] > List[i+1]):
            temp = List[i]
            List[i] = List[i + 1]
            List[i + 1] = temp

print(List[0])
print(List[1])



# List.sort()
# print(List[0])
# print(List[1])



#prog8

print(List[0])