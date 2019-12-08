# Introduction to Python 1

* Installing Anaconda
  * <https://umn.bootcampcontent.com/University-of-Minnesota-Boot-Camp/UofM-STP-DATA-PT-11-2019-U-C/blob/master/00-Documents/Conda_Installation.md>
* Curling up with Python
  * <https://coding-bootcamp-dataviz-prework.readthedocs-hosted.com/en/latest/modules/curling-up-with-python/>
* Here are some things you can run (in your Anaconda terminal) to test:

```bash
conda list | grep jupyter
# Or to search a specific environment by name,
# first list all defined virtual environments:
conda env list
# Then use the name of an environment as the argument to the -n parameter:
conda list -n PythonData | grep jupyter
```

## Common Terminal Commands

```bash
pwd
ls 
ls -al
clear
cd Desktop/
cd ..
mkdir Python
touch newfile
rm newfile
rm -r Pyythion/
explorer .
cd (go home directory)
cd - (go back)
```

## 01-Ins_Terminal

```bash
`cd Desktop` will change to the desktop directory

`mkdir PythonStuff` will make a new directory/folder on the desktop.

`cd PythonStuff` will move to the newly created folder

`open .` on a Mac or `explorer .` in PC will open the current folder

`touch first_file.py` will create a file

`touch second_file.py` will create a second file

`ls` will show what in the current directory

`cd ..` will move us up a director back to Desktop
```

## To run a python program

```bash
python firstProgram.py
```

## Git/GitHub

* Generating SSH keys: <https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh>
* <https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account>
* Two git/GitHub references:
  * Git and GitHub in Plain English is a great guide to review & it’s code-free, focusing on the concepts: <https://blog.red-badger.com/2016/11/29/gitgithub-in-plain-english>
  * This is a nice guide for a workflow & cheat sheet: <https://mukulrathi.com/git-beginner-cheatsheet/*>

* Git commands

```bash
git status
git add <file>
git commit -m "added Python file"
git push origin master
```

* If you're getting the following message

```bash
$ git commit -m "added first python file"
*** Please tell me who you are.
Run
  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"
to set your account's default identity.
Omit --global to set the identity only in this repository.
```

* Run the git config commands, putting in your info where it suggests.

## Anaconda

* To see what version you have:

```bash
conda --version
```

* Create virtual environment

```bash
conda create -n PythonData python=3.6 anaconda
```

* Active environment (one of these commands)

```bash
source activate PythonData
conda activate PythonData
activate PythonData
```

* check python version

```bash
python --version
```

* deactivate environment (one of these commands.)

```bash
source deactivate
conda deactivate
deactivate
```

* To open a file (here myFile.py) for editing in VS Code from a command line:

```bash
code myFile.py
```

* To run interactive python shell

```bash
python
```

## 03-Ins_Variables

* <https://realpython.com/python-f-strings/>

```bash
# Creates a variable with a string "Frankfurter"
title = "Frankfurter"

# Creates a variable with an integer 80
years = 80

# Creates a variable with the boolean value of True
expert_status = True

# Prints a statement adding the variable
print("Nick is a professional " + title)

# Convert the integer years into a string and prints
print("He has been coding for " + str(years) + " years")

# Converts a boolean into a string and prints
print("Expert status: " + str(expert_status))

# An f-string accepts all data types without conversion
print(f"Expert status: {expert_status}")
```

## 05-Ins_Prompts

```bash
# Collects the user's input for the prompt "What is your name?"
name = input("What is your name? ")

# Collects the user's input for the prompt "How old are you?" and converts the string to an integer.
age = int(input("How old are you? "))

# Collects the user's input for the prompt "Is input truthy?" and converts it to a boolean. Note that non-zero,
#   non-empty objects are truth-y.
trueOrFalse = bool(input("Is the input truthy? "))

# Creates three print statements that to respond with the output.
print("My name is " + str(name))
print("I will be " + str(age + 1) + " next year.")
print("The input was converted to " + str(trueOrFalse))
```

## 07-Ins_Conditionals

```bash
x = 1
y = 10

# Checks if one value is equal to another
if x == 1:
    print("x is equal to 1")

# Checks if one value is NOT equal to another
if y != 1:
    print("y is not equal to 1")

# Checks if one value is less than another
if x < y:
    print("x is less than y")

# Checks if one value is greater than another
if y > x:
    print("y is greater than x")

# Checks if a value is less than or equal to another
if x >= 1:
    print("x is greater than or equal to 1")

# Checks for two conditions to be met using "and"
if x == 1 and y == 10:
    print("Both values returned true")

# Checks if either of two conditions is met
if x < 45 or y < 5:
    print("One or more of the statements were true")

# Nested if statements
if x < 10:
    if y < 5:
        print("x is less than 10 and y is less than 5")
    elif y == 5:
        print("x is less than 10 and y is equal to 5")
    else:
        print("x is less than 10 and y is greater than 5")
```

## Lists

* <https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list>

```bash
$ python
Python 3.6.9 |Anaconda, Inc.| (default, Jul 30 2019, 14:00:49) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> myList = ["apples", 6, "bananas", 12]
>>> myList
['apples', 6, 'bananas', 12]
>>> print(myList)
['apples', 6, 'bananas', 12]
>>> myList.append("limes")
>>> myList[3]
12
>>> myList[0]
'apples'
>>> myList[-1]
'limes'
>>> len(myList)
5
>>> print(myList.index("bananas"))
2
>>> myList
['apples', 6, 'bananas', 12, 'limes']
>>> myList.remove("limes")
>>> myList
['apples', 6, 'bananas', 12]
>>> myList.pop(0)
'apples'
>>> myList
[6, 'bananas', 12]
>>> myList.append("guavas")
>>> myList
[6, 'bananas', 12, 'guavas']
>>> myList.append("bananas")
>>> myList.remove("bananas")
>>> myList
[6, 12, 'guavas', 'bananas']
>>> myList[0] = 7
>>> myList
[7, 12, 'guavas', 'bananas']
>>> myTuple = ("apples", "bananas", "carrots")
>>> myTuple
('apples', 'bananas', 'carrots')
>>> myTuple.remove("carrots")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'remove'
>>> myTuple[0]
'apples'
```

```bash
# Create a variable and set it as an List
myList = ["Jacob", 25, "Ahmed", 80]
print(myList)

# Adds an element onto the end of a List
myList.append("Matt")
print(myList)

# Returns the index of the first object with a matching value
print(myList.index("Matt"))

# Changes a specified element within an List at the given index
myList[3] = 85
print(myList)

# Returns the length of the List
print(len(myList))

# Removes a specified object from an List
myList.remove("Matt")
print(myList)

# Removes the object at the index specified
myList.pop(0)
myList.pop(0)
print(myList)

# Creates a tuple, a sequence of immutable Python objects that cannot be changed
myTuple = ('Python', 100, 'VBA', False)
print(myTuple)
```

## 11-Ins_Loops

```bash
# Loop through a range of numbers (0 through 4)
for x in range(5):
    print(x)

print("-----------------------------------------")

# Loop through a range of numbers (2 through 6 - yes 6! Up to, but not including, 7)
for x in range(2, 7):
    print(x)

print("----------------------------------------")

# Iterate through letters in a string
word = "Peace"
for letters in word:
    print(letters)

print("----------------------------------------")

# Iterate through a list
zoo = ["cow", "dog", "bee", "zebra"]
for animal in zoo:
    print(animal)

print("----------------------------------------")

# Loop while a condition is being met
run = "y"

while run == "y":
    print("Hi!")
    run = input("To run again. Enter 'y'")
```