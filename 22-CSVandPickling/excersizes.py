# 1

# def add_user(fname, lname):
#   from csv import DictWriter
#   with open("users.csv", "a") as file:
#     headers = ["First Name", "Last Name"]
#     csv_writer = DictWriter(file, fieldnames=headers)
#     csv_writer.writerow({
#       "First Name": fname,
#       "Last Name": lname
#     })


# Other Way

import csv
 
def add_user(first_name, last_name):
    with open("users.csv", "a") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([first_name, last_name])


add_user("Dwayne", "Johnson")