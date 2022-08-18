# Creating a class

class User:
    def __init__(self, user_id, username):
        self.userId = user_id
        self.username = username
        self.followers = 0
        
        
user_1 = User("001", "MrRain")

print(user_1.username)
print(user_1.followers)