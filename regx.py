import re
x = "To do the best"

y = re.search("[best$]", x)

if y:
    print("exist")
else:
    print("not exist")


z = re.findall(".t", x)
print(z)


a = re.split("\s", x)
print(a)


b = re.sub("\s", "ooo", x, 1)
print(b)



#Match Object

c = re.search("ai", x)
print(c)                      #return - none



#Search for an upper case "S" character in the beginning of a word, and print its position:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

#The string property returns the search string:

print(x.string)

#Search for an upper case "S" character in the beginning of a word, and print the word:

print(x.group())










