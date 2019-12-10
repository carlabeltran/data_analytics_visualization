# relative path to file:
file = "Resources/input.txt"

# with is the english equivalent of "assume"
with open(file, 'r') as text:
    lines = text.read()
    print(lines)
