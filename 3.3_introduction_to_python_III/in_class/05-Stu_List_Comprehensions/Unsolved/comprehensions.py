names = []
for _ in range(5):
    name = input("Please enter the name of someone you know. ")
    names.append(name)

# @TODO: Use a list comprehension to create a list of lowercased names
lowercased = [name.lower() for name in names]
print(lowercased)

# @TODO: Use a list comprehension to create a list of titlecased names
# https://www.tutorialspoint.com/python/string_title.htm
titlecased = [name.title() for name in lowercased]

invitations = [
    f"Dear {name}, please come to the wedding this Saturday!" for name in titlecased]

for invitation in invitations:
    print(invitation)

d = {}
for name in titlecased:
  d[name] = d.get(name, 0) + 1


for x in d:
  print (x,':', d[x])

