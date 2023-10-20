test_dict = {
    'gfg': [1, 3, 4], 
    'is': [7, 6],
    'best': [4, 5]
    }

list = []

for key,value in test_dict.items():
    list1 = [key,value]
    list.append(list1)
print(list)