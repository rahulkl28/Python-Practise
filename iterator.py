List = ["apple", "pine", "cherry"]

myit = iter(List)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"

for x in mystr:
    print(x)


#__iter__()
#__next__()

class Mynum:
    def __iter__(self):
        self.i = 1
        return self
    
    def __next__(self):
        x = self.i
        self.i += 1
        return x

myclass = Mynum()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
  


#StopIteration

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 10:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)


for x in myiter:
  print(x)
