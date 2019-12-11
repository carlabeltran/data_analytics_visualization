# 3.2 Introduction to Python II

## 01-Stu_QuickCheckup

```bash
# Print Hello User!
print("Hello User!")


# Take in User Input
name = input("What is your name? ")


# Respond Back with User Input
print(f"Hello {name}")


# Take in the User Age
age = int(input("What is your age? "))


# Respond Back with a statement based on age
if age <= 35:
  print("Awww... you're just a baby!")
elif age > 35:
  print("Ah... A well traveled soul are ye.")
```

## 02-Ins_SimpleLoops

```bash
# A For loop moves through a given range of numbers
# If only one number is provided it will loop from 0 to that number
for x in range(10):
    print(x)

# If two numbers are provided then a For loop will loop from the first number up until it reaches the second number
for x in range(20, 30):
    print(x)

# If a list is provided, then the For loop will loop through each element within the list
words = ["Peanut", "Butter", "Jelly", "Time", "Is", "Now"]
for word in words:
    print(word)

# A While Loop will continue to loop through the code contained within it until some condition is met
x = "Yes"
while x == "Yes":
    print("Whee! Merry-Go-Rounds are great!")
    x = input("Would you like to go on the Merry-Go-Round again? ")
```

## 03-Ins_KidInCandyStore

```bash
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
```

```bash
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
```

## 04-Stu_HouseOfPies

```bash
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
```

## 05-Ins_BasicRead

```bash
# relative path to file:
file = "Resources/input.txt"

# with is the english equivalent of "assume"
with open(file, 'r') as text:
    lines = text.read()
    print(lines)
```

## 06-Ins_Modules

* Built-in python modules: <https://docs.python.org/3/py-modindex.html>
* <https://pypi.org/>

```bash
# Import the random and string Module
import random
import string

# Utilize the string module's custom method: ".ascii_letters"
print(string.ascii_letters)

# Utilize the random module's custom method randint
for x in range(10):
    print(random.randint(1, 10))
```

```bash
import antigravity
```

## 07 - Ins_ReadCSV

```bash
>>> import os
>>> os.path.join("..", "Resources", "accounting.csv")
'..\\Resources\\accounting.csv'
```

```bash
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'accounting.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)
```

## 08-Stu_ReadNetFlix

```bash
import os
import csv

csvpath = os.path.join('..', 'Resources', 'netflix_ratings.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    video = input("What video are you looking for? ")
    found_video = False
    found_video_title = ""
    found_video_rating = ""
    found_video_rating_score = 0

    # Read each row of data after the header
    for row in csvreader:
      if row[0] == video:
        found_video = True
        found_video_title = row[0]
        found_video_rating = row[1]
        found_video_rating_score = row[6]
        break

    if found_video == True:
      print(f"{found_video_title} is rated {found_video_rating} with a rating of {found_video_rating_score}")
    else:
      print(f"Sorry, {video} could not be found. Try searching another video.")
```

## 09-Ins_WriteCSV

```bash
# Dependencies
import os
import csv

# Specify the file to write to
output_path = os.path.join("..", "output", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

    # Write the second row
    csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])
```

## 10-Ins_Zip

```bash
import csv
import os

# Three Lists
indexes = [1, 2, 3, 4]
employees = ["Michael", "Dwight", "Meredith", "Kelly"]
department = ["Boss", "Sales", "Sales", "HR"]

# Zip all three lists together into tuples
roster = zip(indexes, employees, department)

# save the output file path
output_file = os.path.join("output.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Index", "Employee", "Department"])

    writer.writerows(roster)


# # to print out to terminal:
# #comment out above code and run the code below
# for employee in roster:
#     print(employee)
```

## 11-Stu_UdemyZip

```bash
import csv
import os

csvpath = os.path.join('..', 'Resources', 'web_starter.csv')
titles = []
prices = []
subscriber_count = []
number_reviews = []
course_length = []

with open(csvpath, newline='', encoding='utf8') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read each row
    for row in csvreader:
      titles.append(row[1])
      prices.append(row[4])
      subscriber_count.append(row[5])
      number_reviews.append(row[6])
      course_length.append(float(row[9].split(' ', 1)[0]))

courses = zip(titles, prices, subscriber_count, number_reviews, course_length)

# save the output file path
output_file = os.path.join("output2.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Title", "Price", "Subscriber Count", "Number of Reviews", "Course Length (hours)"])

    writer.writerows(courses)
```

## 12-Ins_Functions

```bash
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
```

