# reporter report date for writing re
# csv : comma separate value
# regex : regular expression
# we use dict to dict
# we use json for our project

import os
# for windows
import datetime
# for date and time
import json
# for JavaScript
# re = {"date" : {"reporter":"report"} }
import time

work_report = {}



# one empty dict
counter = 0
# start from 0
while True:
    while True:
        try:
            report_hour = int(input("Enter report hours: "))
        except ValueError:
            print("Please enter a valid integer")
            continue
        if  0 <= report_hour < 24:
            break
        print("invalid report hour")

    while True:
        try:
            report_min = int(input("Enter report minutes: "))
        except ValueError:
            print("Please enter a valid integer")
            continue
        if 0 <= report_min < 60:
            break
        print("invalid report minute")

    report_time =f"{report_hour:02d}:{report_min:02d}"



    reporter = input("Enter reporter name: ")
    # get users name
    report = input("Enter report content: ")


    work_report[report_hour] = {reporter : report}
    # we put this inputs to the empty work_report
    resume = input("Do you want to continue (yes/no): ").strip().lower()
    # we ask user to continue and in every way user want to type and change it to lower case and no capital
    if resume == 'yes' or resume == 'no':
# we create if to resume
        break
    # end
    else:
    # another condition
        print("invalid input")

    if resume == 'no':
    # second if
        break

    print(work_report)

for i in range(0,24):
     for j in range(0,60):
# this is minutes
        current_time = f"{i:02d}:{j:02d}"
# we use f string to combine hours and minutes
        if current_time in work_report.keys():
    # this line check the patterns outputs and find a repetitive report
            print(f"{current_time} --> {work_report[current_time]}")
        # add user time to our pattern
        else:

            print(current_time)
    # if user time is not in our pattern print the time solo

if os.path.exists("work_report.json"):
     with open("work_report.json", "r") as outfile:
        data = json.load(outfile)
else:
    data = {}
data.update(work_report)
with open("work_report.json", "w") as outfile:
    json.dump(data, outfile)





