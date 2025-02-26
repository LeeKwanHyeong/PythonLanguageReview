import csv

# with open("/Users/igwanhyeong/PycharmProjects/Data/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# with open("/Users/igwanhyeong/PycharmProjects/Data/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas
# data_frame = pandas.read_csv("/Users/igwanhyeong/PycharmProjects/Data/weather_data.csv")
# data_dict = data_frame.to_dict()
# print(data_dict)
#
# print(data_frame.condition)

# Get Data in Row
# print(data_frame[data_frame.day == 'Monday'])
# print(data_frame.temp.max())
#
# print(data_frame[data_frame.temp == data_frame.temp.max()])

# monday = data_frame[data_frame.day == 'Monday']
# print(monday.condition)
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Create a dataframe from scratch
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)

data_frame = pandas.read_csv("/Users/igwanhyeong/PycharmProjects/Data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data_frame[data_frame['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(data_frame[data_frame['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data_frame[data_frame['Primary Fur Color'] == 'Black'])

print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
