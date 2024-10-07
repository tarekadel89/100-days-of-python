import pandas as pd

data = pd.read_csv("Day 025/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241007.csv")

unique_colors = data["Primary Fur Color"].unique().tolist()

data_dictionary = {}
for color in unique_colors:
    squirrels_of_color = data[data["Primary Fur Color"] == color]
    total_count = len(squirrels_of_color)
    data_dictionary[color] = total_count

df = pd.DataFrame(list(data_dictionary.items()), columns=["Color", "Count"])
df.to_csv("Day 025/squirrel_color_counts.csv", index=False)
