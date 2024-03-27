# Without libraries
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
# print(data)

# Using csv library
# import csv  # import csv library
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)  # csv.reader() reads a file and returns an iterable object
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# Using pandas library (must install first). The pandas library allows us to work with .csv files. The .read_csv()
# function opens, reads, and formats data from a .csv file and returns an object similar to a table called DataFrame.
# Each column in a DataFrame is a 1-dim object called Series which is similar to a list.
import pandas

data = pandas.read_csv("weather_data.csv")  # pandas DataFrame
print(data)
temperatures = data["temp"]  # pandas Series
print(temperatures)

print(data.to_dict())  # pandas function to convert a DataFrame to a dictionary

print(temperatures.to_list())  # pandas function to convert a Series to a list

# average_temp = round(sum(temperatures)/len(temperatures), 2)
# print(average_temp)

print(round(temperatures.mean(), 2))  # get avg temperature using pandas mean() function

print(temperatures.max())  # get max temperature using pandas max() function

# Pandas can use both [] notation or . notation (better to use [])
print(data["condition"])
print(data.condition)

# Get data from a row. We first call the DataFrame, and then we select a column and compare it to a certain value
print(data[data["day"] == "Monday"])

print(data[data["temp"] == data["temp"].max()])  # get row where temp was max

# Once we get a row we can get values for each column on that row by passing the name of the column between []
monday_row = data[data["day"] == "Monday"]
monday_celcius_temp = int(monday_row["temp"])
# monday_celcius_temp = int(monday_row.iloc[0, 1])  # alternative to line above and future correct way to do it
monday_farenheit_temp = (monday_celcius_temp * 9 / 5) + 32
print(monday_farenheit_temp)

# Create DataFrame from scratch
data_dic = {
    "students": ["Any", "James", "Angela"],
    "scores": [76, 56, 65]
}
new_data = pandas.DataFrame(data_dic)
print(new_data)
new_data.to_csv("new_data.csv")  # from the DataFrame we can create a .csv file using the .to_csv() function
