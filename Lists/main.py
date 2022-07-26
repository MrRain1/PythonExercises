#lista semplice 
spam = ["cat", "dog", "bat" ,"dolphin"]

#lista innestata
#Simile ad una matrice
spam2 = [["cat","bat"], [10,40,50,60]]
#spam2[0] => ["cat","bat"]
#spam2[0][1] =>"bat"

#slice:
spam[1:3] # => ["dog", "bat"]

spam3 = [10, 20 ,30]
spam3[1:3] = ["cat", "dog", "mouse"] # spam3=> [10, "cat", "dog", "mouse"] 

#delete something from the list

spam4 = ["cat", "dog", "bat" ,"dolphin"]
del spam4[2] # spam4 => ["cat", "dog","dolphin"]

#conversion to list
list("Hello") #returns a list containing the characters that form Hello

#is something in a list?

"cat" in spam # => returns TRUE
"rat" in spam # => returns FALSE

#something isn't in a list
"cat" not in spam # => returns FALSE
"rat" not in spam # => returns TRUE

#the range() object is a list like object
#in fact we can easly convert it in one with the list() function

spam5 = list(range(0, 102, 2))