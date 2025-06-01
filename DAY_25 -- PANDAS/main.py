# with open("weather_data.csv") as file:
#     content = file.readlines()
#     print(content)
# --------------->See the below one for better method

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)
# So much of line of code is required for a simple data...so to make it easier
# we gonna install Pandas Library

# ---------------------------------------------

import pandas

# data = pandas.read_csv("weather_data.csv")

# print(data)

# print(data["temp"])  ------> Try it once

# -------------------------------------------------

#Two types ----> Data frame (2 dimensional)  and Series (1 Dimensional)
#
# data_dict = data.to_dict()
# print(data_dict)   # In data frame
# -------------------------------------------------
# temp_list = data["temp"].to_list()
# print(temp_list)  # In Series

# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)  ----> see the easy method
# print(data["temp"].mean())
# print(data["temp"].max())

# ---------------------------------------------------------
#get data in column
# print(data["condition"])
# print(data.condition)  #both works in the same way...

#get data in row
# print(data[data.day == "Monday"])

#printing the row of the highest temperature
# print(data[data.temp == data.temp.max()])  # == data["temp"].max()

# ----------------------------------------------------------------------

#getting a day's temperature in Fahrenheit
# monday = data[data.day == "Monday"]
# monday_F= monday.temp[0] * 9/5 +32
# print(monday_F)

#-------------------------------------------------------------------------
# data_dict = {
#     "students" : ["amy","james","Dinesh"] ,
#     "scores" : ["89","91","94"]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_file.csv")

