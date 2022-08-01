myCat = { "size" : "fat",
          "color" : "grey",
          "disposition" : "loud"}

myCat["size"]

print(f"My cat has {myCat['color']} fur")

spam = {
    12345: "Luggage Combination",
    42: "The Answer"    
}

#check if something is in the dictionary

"size" in myCat
"name" not in spam

#keys in a dict
myCat.keys()

#values in a dict
myCat.values()

#items in a dict => return tuples
myCat.items()

myCat.get("disposition", 0)
myCat.get("name" , "")

myCat.setdefault("color", "black")