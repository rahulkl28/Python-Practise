test_list = [
    {'Nikhil' : 17, 'Akash' : 18, 'Akshat' : 20},
    {'Nikhil' : 21, 'Akash' : 30, 'Akshat' : 10},
    {'Nikhil' : 31, 'Akash' : 12, 'Akshat' : 19}
    ]

tuple = tuple(test_list)
(green, yellow, red) = tuple

list1 = list(green.values())
list2 = list(yellow.values())
list3 = list(red.values())

x = green.keys()
lista = list(x)

listoflist = [lista , list1 , list2 , list3]
print(listoflist)

