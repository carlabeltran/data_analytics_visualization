def HelloMessage():
  print("Hello!")

HelloMessage()

def printName(name):
  print("Hello, " + name)

printName("Paul")
printName("Nili")
printName("Garrett")

def listInfo(list):
  for value in list:
    print(value)
  print("The length is " + str(len(list)))

listInfo([1, 2, 3])
listInfo(["a", "b", "c", "d"])