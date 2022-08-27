class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Angela")
user_2 = User("002", "Jack")

user_1.follow(user_2)
user_1.follow(user_2)
user_2.follow(user_1)


print(f"Name: {user_1.username}, ID: {user_1.id}")
print(f"Followers: {user_1.followers}")
print(f"Following: {user_1.following} People\n")

print(f"Name: {user_2.username}, ID: {user_2.id}")
print(f"Followers: {user_2.followers}")
print(f"Following: {user_2.following} Person")
