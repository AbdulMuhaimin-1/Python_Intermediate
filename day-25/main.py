import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# average = sum(temp_list) / len(temp_list)
# print(average)
#
# average_1 = data["temp"].mean()
# print(average_1)
# print(data["temp"].max())
#
# # Get Data in Columns
# print(data["condition"])
# print(data.condition)

# Get Data in Rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp_celsius = monday.temp.max()
# monday_temp_fahrenheit = (monday_temp_celsius * 1.8) + 32
# print(monday_temp_fahrenheit)


squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])


squirrel_fur_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count],
}

squirrel_data_convert = pandas.DataFrame(squirrel_fur_dict)
squirrel_data_convert.to_csv("squirrel_count.csv")
print(squirrel_data_convert)




