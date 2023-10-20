# Add two list into dictionary

# test_keys = ["Rash", "Kil", "Varsha"]
# test_values = [1, 4, 5]

# dict ={}

# for i in test_keys:
#     for j in test_values:
#         dict[i] = j 
#         test_values.remove(j)
#         break
# print(dict)


# old_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56, 'E': 12, 'F': 69, 'G': 67, 'H': 23}


# remove duplicate dictionary from list

# test_list = [{"Akash" : 1}, {"Kil" : 2}, {"Akshat" : 3},
#              {"Kil" : 2}, {"Akshat" : 3}]
 
# list1 =[]


# for i in test_list: 
#     if i not in list1:
#         list1.append(i)
# print(list1)




# print frequency of repeated no. in a list

# my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

# mydict = {}

# for i in my_list:
#     if i not in mydict.keys():
#         mydict[i] = 1
        
#     else:
#         mydict[i]+=1
# print(mydict)
        


# my_dict ={"Java":100, "Python":112, "C":11}


# for i in my_dict.keys():
#     print(my_dict)




# Find depth of a dictionary

# dic = {1:'Geek', 2: {3: {4: {}}}}

# count = 0


# for i in str(dic):
#     if i == "{":
#         count += 1
# print(count)




# Swap Keys and Values in Dictionary

old_dict = {'A': 67, 'B': 23, 'C': 45, 'E': 12, 'F': 69, 'G': 67, 'H': 23}

newdict = {}

for i,j in old_dict.items():
    
        if j in newdict:
            newdict[j].append(i)
        else:
            newdict[j] =[i]
print(newdict)