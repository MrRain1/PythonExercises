with open("./file1.txt") as data1:
    first_list = data1.readlines()
    
with open("./file2.txt") as data2:
    second_list = data2.readlines()
    

first_list = [int(data.replace("\n", "")) for data in first_list]
second_list = [int(data.replace("\n", "")) for data in second_list]

result = [number for number in first_list if number in second_list]

print(result)
