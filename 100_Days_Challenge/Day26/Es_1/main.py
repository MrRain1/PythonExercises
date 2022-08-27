names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# conditional list comprehension
# [new_item for item in list if (test)]

long_names = [name.upper() for name in names if len(name)>=5]
print(long_names)