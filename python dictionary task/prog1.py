dict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}

thelist = list(dict.values())
listkey = list(dict.keys())

for j in range(len(thelist)- 1):
    for i in range(len(thelist)-1):
        if(thelist[i]> thelist[i + 1]):
            temp = thelist[i]
            thelist[i] = thelist[i + 1]
            thelist[i + 1] = temp




sorted_dict = {}
for i in thelist:
    index = listkey[thelist.index(i)]
    sorted_dict[index] = i

print(sorted_dict)

