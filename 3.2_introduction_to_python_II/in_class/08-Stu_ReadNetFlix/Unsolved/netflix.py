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

    if found_video == True:
      print(f"{found_video_title} is rated {found_video_rating} with a rating of {found_video_rating_score}")
    else:
      print(f"Sorry, {video} could not be found. Try searching another video.")