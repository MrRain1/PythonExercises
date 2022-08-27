import pandas

squirrle_data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(squirrle_data)

squirrel_color = squirrle_data["Primary Fur Color"]
# squirrel_color_list = squirrle_data["Primary Fur Color"].to_list()
# print(squirrel_color)

# total_gray_color = 0 
# for index in range(len(squirrel_color_list)):
#     if(squirrel_color_list[index] == "Gray"):
#         total_gray_color += 1
# print(total_gray_color)

total_gray_color = len(squirrel_color[squirrel_color == "Gray"])
print(total_gray_color)

total_black_color = len(squirrel_color[squirrel_color == "Black"])
print(total_black_color)

total_cinnamon_color = len(squirrel_color[squirrel_color == "Cinnamon"])
print(total_cinnamon_color)

data_squirrle_color = {
    "Fur Color": ["Gray", "Black", "Cinammon"],
    "Count": [total_gray_color, total_black_color, total_cinnamon_color],
}

df = pandas.DataFrame(data_squirrle_color)
df.to_csv("./squirrel_count.csv")