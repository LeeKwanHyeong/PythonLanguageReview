class User:
    def __init__(self, user_id, username):
        print('new user being created...')
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self):
        self.followers += 1
        self.following += 1

user_1 = User(user_id='001', username='lee')
user_1.followers = 100
user_1.follow()

print(user_1.followers)