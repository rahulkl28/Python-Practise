lst = [ {"name": "Rahul", "age": 20}, 
        {"name": "Navjot", "age": 25},
        {"name": "Ajay", "age": 19}
    ]


for j in range(len(lst) - 1):
    for i in range(0,len(lst) - 1):
        if(lst[i]["age"] > lst[i + 1]["age"]):
             temp = lst[i]
             lst[i] = lst[i + 1]
             lst[i + 1] = temp

print(lst)


for j in range(len(lst) - 1):
    for i in range(0,len(lst) - 1):
        if(lst[i]["name"] > lst[i + 1]["name"]):
             temp = lst[i]
             lst[i] = lst[i + 1]
             lst[i + 1] = temp
print(lst)

