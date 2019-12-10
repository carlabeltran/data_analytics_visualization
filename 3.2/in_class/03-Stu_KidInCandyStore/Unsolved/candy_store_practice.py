candy_list = ["Snickers", "Starburst", "Airheads", "M&Ms",
              "Skittles", "KitKat", "Lollipop", "Juicy Fruit", "Hersheys"]

for i in range(len(candy_list)):
    print(f"{[i]} {candy_list[i]}")

allowance = 5
candy_cart = []

while allowance > 0:
    candy_input = int(
        input("Enter the number associated with the candy you want. "))
    candy_cart.append(candy_list[candy_input])
    allowance = allowance - 1

print("You selected the following candies:")
for i in range(len(candy_cart)):
    print(f"{candy_cart[i]}")
