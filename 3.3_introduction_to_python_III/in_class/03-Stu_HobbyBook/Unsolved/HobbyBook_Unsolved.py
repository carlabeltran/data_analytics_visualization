me = {
  "name": 'phil',
  "age": 28,
  "hobbies": ["basketball", "running", "hockey"],
  "wake_up_times": {
    "Monday": "5 a.m.",
    "Tuesday": "6 a.m.",
    "Wednesday": "5:30 a.m.",
    "Thursday": "5:45 a.m.",
    "Friday": "7:00 a.m.",
    "Saturday": "8:00 a.m.",
    "Sunday": "7:10 a.m."
  }
}


print(f"Hi, my name is {me['name']}. I have {len(me['hobbies'])} hobbies.")
print(f" I get up at {me['wake_up_times']['Friday']} on Friday.")
