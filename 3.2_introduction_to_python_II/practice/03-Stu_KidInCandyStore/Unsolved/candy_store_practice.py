candies = ["Snickers", "M&Ms", "Reeses", "Milky Way", "Starbursts", "Skittles", "JuicyFruit", "Lollipop", "Twizzlers", "Cotton Candy"]

candies_list_length = len(candies)

for i in range(candies_list_length):
  print(f"{[i]} {candies[i]}")

allowance = 5
candy_cart = []

for x in range(allowance):
  candy_number = int(input('Enter the number associated with the candy you want: '))
  try:
   candy_cart.append(candies[candy_number])
  except IndexError:
    print("Sorry, we don't have that candy. Please select a different option.")

print("Candies purchased:")
for candy in candy_cart:
  print(f"{candy}")