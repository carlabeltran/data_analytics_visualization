pies = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
        "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

print("Welcome to the House of Pies! Here are our pies:")
print("----------------------------------------------------------------")

new_string = ""
for i in range(len(pies)):
    new_string += f"{[i + 1]} {pies[i]}, "

print(new_string)
keep_ordering = "y"
number_pies_ordered = 0
pies_ordered = []

while keep_ordering == "y":
    order = int(input(
        "Enter the number associated with the pie you would like to order: "))

    print(f"Great! We'll have that {pies[order - 1]} pie right out for you.")
    number_pies_ordered = number_pies_ordered + 1
    pies_ordered.append(pies[order - 1])

    keep_ordering = input(
        "Would you like to make another order. Enter 'y' to order another pie. Otherwise, enter 'n'.")

print(f"You ordered {number_pies_ordered} pies.")

print("You ordered the following pies:")
# for pie in pies_ordered:
#     print(pie)

for pie in pies:
    print(f"{pies_ordered.count(pie)} {pie}")
