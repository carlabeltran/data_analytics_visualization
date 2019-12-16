run = "y"
current_number = 0

while run == "y":
    numbers_count = int(input("How many numbers? "))

    for number in range(current_number, current_number + numbers_count):
        print(number)
    current_number = current_number + numbers_count
    keep_going = input("Do you want to continue (y/n) ?")
    if keep_going == "n":
        run = "n"
    else:
        run = "y"
