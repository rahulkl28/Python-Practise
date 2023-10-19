import json


#Parse JSON - Convert from JSON to Python

x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)

print(y)
print(y["age"])



#Convert from Python to JSON

a = {
    "name": "Sam",
    "age": "22",
    "city": "New Jersey"
}

b = json.dumps(a)

print(b)