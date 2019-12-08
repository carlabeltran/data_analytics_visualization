name = 'Parker'
country = 'Australia'
age = 17
hourly_wage = 13
satisfied = True
daily_wage = hourly_wage * 8

print("Hi, my name is " + name + ", and I am from " +
      country + ". I am " + str(age) + ' years old.')
print("My hourly wage is " + str(hourly_wage) +
      ", and my daily wage is " + str(daily_wage) + ".")
print("Satisfied: " + str(satisfied))

print(f"My daily wage is {daily_wage}. Satisfied: {satisfied}")

# https://realpython.com/python-f-strings/
