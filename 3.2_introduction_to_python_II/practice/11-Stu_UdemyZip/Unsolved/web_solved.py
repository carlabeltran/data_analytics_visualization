import os
import csv

csvpath = os.path.join('..', 'Resources', 'web_starter.csv')

titles = []
prices = []
subscriber_count = []
number_reviews = []
course_length = []
review_percent = []

with open(csvpath, newline='', encoding="utf8") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    for row in csvreader:
      titles.append(row[1])
      prices.append(row[4])
      subscriber_count.append(row[5])
      number_reviews.append(row[6])
      course_length.append(float(row[9].split(' ', 1)[0]))
      percent = round(int(row[6]) / int(row[5]), 2)
      review_percent.append(percent)

    courses = zip(titles, prices, subscriber_count, number_reviews, course_length, review_percent)

# save the output file path
output_file = os.path.join("output3.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Title", "Price", "Subscriber Count", "Number of Reviews", "Course Length"])

    writer.writerows(courses)