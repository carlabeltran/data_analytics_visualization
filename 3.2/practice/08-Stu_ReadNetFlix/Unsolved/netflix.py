import os
import csv

csvpath = os.path.join('..', 'Resources', 'netflix_ratings.csv')

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    video = input("What video are you looking for?")
    has_video = False
    title = ""
    rated = ""
    user_rating = 0

    # Read each row of data after the header
    for row in csvreader:
      if row[0] == video:
        has_video = True
        title = row[0]
        rated = row[1]
        user_rating = row[6]
        break

    if has_video == True:
      print(f"{title} is rated {rated} with a rating of {user_rating}")
    else:
      print(f"Sorry, your video could not be found. Try looking up another video.")
