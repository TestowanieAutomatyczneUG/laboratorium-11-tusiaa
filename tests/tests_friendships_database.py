import unittest
from unittest.mock import *
from parameterized import parameterized
from src.FrienshipsDatabase import FrienshipsDatabase

class TestsFrienshipsDatabase(unittest.TestCase):
    
    def setUp(self):
        self.test_object = FrienshipsDatabase()

    def test_addFriend(self):
        self.test_object.database.addFriend = MagicMock()
        self.test_object.addFriend("person1", "person2")
        self.test_object.database.addFriend.assert_called_once_with("person1", "person2")

    def test_makeFriends(self):
        self.test_object.database.makeFriends = MagicMock()
        self.test_object.makeFriends("person1", "person2")
        self.test_object.database.makeFriends.assert_has_calls([call("person1", "person2")])

    def test_getFriendsList(self):
        self.test_object.database.getFriendsList = MagicMock(side_effect=[["person1", "person2"]])
        self.assertEqual(["person1", "person2"], self.test_object.getFriendsList("person"))

    def test_getFriendsList_empty(self):
        self.test_object.database.getFriendsList = MagicMock(side_effect=[[]])
        self.assertEqual([], self.test_object.getFriendsList("person1"))

    def test_makeFriendsFalse(self):
        self.test_object.database.areFriends = MagicMock(side_effect=[False])
        self.assertFalse(self.test_object.areFriends("person1", "person2"))

    def test_areFriendsTrue(self):
        self.test_object.database.areFriends = MagicMock(side_effect=[True])
        self.assertTrue(self.test_object.areFriends("person2", "person1"))
       
    @parameterized.expand([
        ("", ValueError),
        (5, ValueError),
        (5.5, ValueError),
        (True, ValueError),
        (None, ValueError),
        ([1,2,3], ValueError),
        ({'name': 2, 'grades': 4}, ValueError),
    ])
    def test_addFriend_wrong_person1(self, person1, expected_exception):
        with self.assertRaises(expected_exception):
            self.test_object.addFriend(person1, "person2")

    @parameterized.expand([
        ("", ValueError),
        (5, ValueError),
        (5.5, ValueError),
        (True, ValueError),
        (None, ValueError),
        ([1,2,3], ValueError),
        ({'name': 2, 'grades': 4}, ValueError),
    ])
    def test_addFriend_wrong_person2(self, person2, expected_exception):
        with self.assertRaises(expected_exception):
            self.test_object.addFriend("person1", person2)
        
    @parameterized.expand([
        ("", ValueError),
        (5, ValueError),
        (5.5, ValueError),
        (True, ValueError),
        (None, ValueError),
        ([1,2,3], ValueError),
        ({'name': 2, 'grades': 4}, ValueError),
    ])
    def test_makeFriendsFalse_wrong_person2(self, person2, expected_exception):
        with self.assertRaises(expected_exception):
            self.test_object.makeFriends("person1", person2)

    @parameterized.expand([
        ("", ValueError),
        (5, ValueError),
        (5.5, ValueError),
        (True, ValueError),
        (None, ValueError),
        ([1,2,3], ValueError),
        ({'name': 2, 'grades': 4}, ValueError),
    ])
    def test_makeFriendsFalse_wrong_person1(self, person1, expected_exception):
        with self.assertRaises(expected_exception):
            self.test_object.makeFriends(person1, "person2")
    
    @parameterized.expand([
        ("", ValueError),
        (5, ValueError),
        (5.5, ValueError),
        (True, ValueError),
        (None, ValueError),
        ([1,2,3], ValueError),
        ({'name': 2, 'grades': 4}, ValueError),
    ])
    def test_getFriendsList_wrong_person(self, person, expected_exception):
        with self.assertRaises(expected_exception):
            self.test_object.getFriendsList(person)
    
    @parameterized.expand([
        ("", ValueError),
        (5, ValueError),
        (5.5, ValueError),
        (True, ValueError),
        (None, ValueError),
        ([1,2,3], ValueError),
        ({'name': 2, 'grades': 4}, ValueError),
    ])
    def test_areFriends_wrong_person2(self, person2, expected_exception):
        with self.assertRaises(expected_exception):
            self.test_object.areFriends("person1", person2)

    @parameterized.expand([
        ("", ValueError),
        (5, ValueError),
        (5.5, ValueError),
        (True, ValueError),
        (None, ValueError),
        ([1,2,3], ValueError),
        ({'name': 2, 'grades': 4}, ValueError),
    ])
    def test_areFriends_wrong_person1(self, person1, expected_exception):
        with self.assertRaises(expected_exception):
            self.test_object.areFriends(person1, "person2")

    def tearDown(self):
        del self.test_object


