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
