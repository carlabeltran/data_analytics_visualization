import os
import csv

cereal_csv = os.path.join("../Resources", "cereal_bonus.csv")

with open(cereal_csv, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    # csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
      if float(row[7]) < 5:
        print(row)
