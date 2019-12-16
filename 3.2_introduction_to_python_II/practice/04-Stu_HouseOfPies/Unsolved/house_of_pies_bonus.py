pies = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", "Blueberry", "Buko", "Burek", "Tamale",  "Steak"]
pie_order_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print("Welcme to the House of Pies! Here are our pies:")
print("")
print("")
print("----------------------------------------------------------------")

pie_string = ""

for i in range(len(pies)):
  pie_string += f"{[i + 1]} {pies[i]}, "

print(pie_string)

keep_ordering = "y"
pies_ordered = []

while keep_ordering == "y":
  order = int(input("What pie would you like to order? Enter the number of the pie: "))

  print(f"Great! We'll have that {pies[order]} right out fr you.")
  pies_ordered.append(pies[order])
  pie_order_count[order - 1] = pie_order_count[order - 1] + 1
  keep_ordering = input(f"Would you like to make another order? Enter 'y' to order more. Otherwise, enter 'n'. ")

print(f"You ordered {len(pies_ordered)} pies.")
for i in range(len(pies)):
  print(f"{pie_order_count[i]} {pies[i]}")