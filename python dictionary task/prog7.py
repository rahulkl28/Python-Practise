string = "geeksforgeeeks"

list = []
dict = {}


for char in string:
    if char in dict:
        dict[char]+=1

    else:
        dict[char]=1
    

for char,count in dict.items():
    if count>1:
        list.append(char)
print(list)