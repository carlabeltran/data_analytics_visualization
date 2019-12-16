# @TODO: Write a function that returns the arithmetic average for a list of numbers

def average(list):
  list_length = len(list)
  sum = 0

  for number in list:
    sum += number

  return sum / list_length


# Test your function with the following:
print(average([1, 5, 9]))
print(average(range(11)))
