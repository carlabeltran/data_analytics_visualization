user_plays = "y"
starting_number = 0

while user_plays == "y":
    user_number = int(input("How many numbers?"))

    for number in range(starting_number, user_number + starting_number):
        print(number)

    starting_number = user_number + starting_number
    user_plays = input(
        "Do you want to play again? Enter 'y' to play again. Enter 'n' to exit the game.")
