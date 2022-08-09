import pprint

message= "It was a bright cold day in April, \
    and the clocks were stricking thirteen"
    
count ={}

for char in message.lower():
    count.setdefault(char, 0)
    count[char] += 1
    
#pprint.pprint(count)

rjtext = pprint.pformat(count) #converts in a string format
print(rjtext)