import os
import csv

# cereal_csv = os.path.join("../Resources", "cereal.csv")
cereal_csv = os.path.join("../Resources", "cereal_bonus.csv")

with open(cereal_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    for row in csvreader:
      if float(row[7]) >= 5:
        print("===========================================================")
        print(f"name: {row[0]}")
        print(f"mfr: {row[1]}")
        print(f"type: {row[2]}")
        print(f"calories: {row[3]}")
        print(f"fiber: {row[7]}")
        print("===========================================================")



