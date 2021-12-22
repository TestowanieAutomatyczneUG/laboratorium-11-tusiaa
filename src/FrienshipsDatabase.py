from src.Friendships import Friendships

class FrienshipsDatabase:
    def __init__(self):
        self.database = Friendships()

    def addFriend(self, person1, person2):
        self.database.addFriend(person1, person2)

    def makeFriends(self, person1, person2):
        self.database.makeFriends(person1, person2)

    def getFriendsList(self, person):
        return self.database.getFriendsList(person)

    def areFriends(self, person1, person2):
        return self.database.areFriends(person1, person2)

