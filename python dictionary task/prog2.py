dict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}

listkey = list(dict.keys())
listval = list(dict.values())

for j in range(len(listkey)- 1):
    for i in range(len(listval)- 1):
        if(listkey[i] > listkey[i + 1]):
            temp = listkey[i]
            listkey[i] = listkey[i + 1]
            listkey[i + 1] = temp

sortdict = {}
for i in listval:
    index = listkey[listval.index(i)]
    sortdict[index] = i

print(sortdict)