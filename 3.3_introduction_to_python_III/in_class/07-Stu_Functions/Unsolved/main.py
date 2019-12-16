# @TODO: Write a function that returns the arithmetic average for a list of numbers
def average(list):
  sum = 0
  list_length = len(list)
  for number in list:
    sum += number
  average = sum / list_length
  return average


# Test your function with the following:
print(average([1, 5, 9]))
print(average(range(11)))
print(average([2, 3, 4, 1, 5]))
