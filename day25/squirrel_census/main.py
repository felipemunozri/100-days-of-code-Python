# import pandas
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
#
# # print(black_squirrels_count)
# # print(cinnamon_squirrels_count)
# # print(gray_squirrels_count)
#
# data_object = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
# }
#
# df = pandas.DataFrame(data_object)
# df.to_csv("squirrel_count.csv")

# # Another solution
# import pandas
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# data_count = data["Primary Fur Color"].value_counts().reset_index()  # reset.index() converts from Series to DataFrame
# data_count.columns = ["Fur Color", "Count"]
# # print(data_count)

# data_count.to_csv("squirrel_count.csv")

# # Another solution
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_count = data.groupby("Primary Fur Color").size()
print(data_count)
# data_count.to_csv("squirrel_count.csv")
