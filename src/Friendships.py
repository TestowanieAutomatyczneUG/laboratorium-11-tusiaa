class Friendships:
    def __init__(self):
        self.frienships = {}

    def addFriend(self, person1, person2):
        if not person1 or type(person1) != str or not person2 or type(person2) != str:
            raise ValueError("Invalid name")
        if person1 in self.frienships:
            self.frienships[person1].append(person2)
        else:
            self.frienships[person1] = [person2]

    def makeFriends(self, person1, person2):
        if not person1 or type(person1) != str or not person2 or type(person2) != str:
            raise ValueError("Invalid name")
        self.addFriend(person1, person2)
        self.addFriend(person2, person1)

    def getFriendsList(self, person):
        if not person or type(person) != str:
            raise ValueError("Invalid name")
        if person in self.frienships:
            return self.frienships[person]
        return []

    def areFriends(self, person1, person2):
        if not person1 or type(person1) != str or not person2 or type(person2) != str:
            raise ValueError("Invalid name")
        if person2 in self.frienships and person1 in self.frienships[person2]:
            return True
        return False
