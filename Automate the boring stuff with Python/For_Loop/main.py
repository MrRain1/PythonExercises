print("My name is")

#for loop
for i in range(5):
    print(f"Bruno Five Times: {i+1}")
    
total = 0

for num in range(101):
    total += num
    
print(total)

for i in range(5,15):
    print(f"Bruno Five Times: {i}")
   
#range() can take three arguments, the start of the range
#and the end of the range
#if the first argument is omitted it starts from 0
#there's also the step to increment, the default is +1
#setting a negative step decreses the counter