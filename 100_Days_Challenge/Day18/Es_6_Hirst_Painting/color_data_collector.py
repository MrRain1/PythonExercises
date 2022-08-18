import colorgram
import os

rgb_colors = []
colors = colorgram.extract('./image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    
    new_color = (r,g,b)
    rgb_colors.append(new_color)
    
    
color_file = open("./colors.py", "w")

color_file.write("color_data = [\n")

for index in range(0, len(rgb_colors)):
    color_file.write(f"    {rgb_colors[index]},\n")
    
color_file.write("]\n")
color_file.close()