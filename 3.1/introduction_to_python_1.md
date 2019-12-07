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

## To run python program

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

## Lists

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