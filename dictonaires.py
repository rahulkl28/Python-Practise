thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]

}

print(thisdict)
print(thisdict["brand"])
print(type(thisdict))

#Access items

x = thisdict["model"]
# x = thisdict.get("model")

x = thisdict.keys()
print(x)

x = thisdict.values()
print(x)

x = thisdict.items()
print(x)

thisdict.update({"year": 2020})
print(thisdict)



#Add  Dictionary items

thisdict.update({"color": "red"})
print(thisdict)


#Remove Dictionary items

thisdict.pop("model")

thisdict.popitem()
print(thisdict)

# thisdict.clear()

#loop dictionary

for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
  print(x)

for x, y in thisdict.items():
  print(x, y)


#copy dictionaries

mydict = thisdict.copy()

mydict = dict(thisdict)

print(mydict)

#Nested Dictionaries

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)
print(myfamily["child1"]["name"])
