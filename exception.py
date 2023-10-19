try:
    print(x)
except:
    print("An exception occured")
else:                  #Always run if the try case run   
    print("wooooooo")
finally:
    print("The try/except is finished")



# This can be useful to close objects and clean up resources

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")



#  Raise an exception

# x = -2
# if x < 0:
#     raise Exception("Sorry, no numbers below zero")


y = "hello"

if not type(y) is int:
    raise TypeError("only integers are allowed")

