List = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

myList = []
List.sort()
        
for i in range(len(List)-1):
    if(List[i] == List[i + 1]):
        myList.append(List[i])
    else:
        i+=1
    mySet = set(myList)
    UniList = list(mySet)
print(UniList)

        
       
