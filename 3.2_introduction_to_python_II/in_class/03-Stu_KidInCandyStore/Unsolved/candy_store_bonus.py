candy_list = ["Snickers", "Starburst", "Airheads", "M&Ms",
              "Skittles", "KitKat", "Lollipop", "Juicy Fruit", "Hersheys"]

for i in range(len(candy_list)):
    print(f"{[i]} {candy_list[i]}")

select_more_candy = "yes"
candy_cart = []

while select_more_candy == "yes":
    candy_input = int(
        input("Enter the number associated with the candy you want. "))
    try:
        candy_cart.append(candy_list[candy_input])
    except IndexError:
        print('You selected an invalid option.')
    select_more_candy = input(
        "Do you want more candy? Enter 'yes' to select some more candy. You know you want to.")

if len(candy_cart) > 0:
    print("You selected the following candies:")
    for i in range(len(candy_cart)):
        print(f"{candy_cart[i]}")
else:
    print("You didn't select any candies.")
