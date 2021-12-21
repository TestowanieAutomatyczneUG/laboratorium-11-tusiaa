import unittest
from unittest.mock import *
from parameterized import parameterized
from src.Note import *
from src.NotesService import *

class TestNoteService(unittest.TestCase):

    def setUp(self):
        self.test_object = NotesService()

    def test_averageOf(self):
        NotesStorage.getAllNotesOf = MagicMock(return_value=[Note("note", 3), Note("note", 4), Note("note", 5)])
        result = self.test_object.averageOf("note")
        self.assertEqual(4, result, 'return value incorrect')

    def test_averageOf_0Notes(self):
        NotesStorage.getAllNotesOf = MagicMock(return_value=[])
        result = self.test_object.averageOf("note")
        self.assertEqual(0, result, 'return value incorrect')

    def test_add(self):
        NotesStorage.add = MagicMock()
        note = Note("note", 3)
        self.test_object.add(note)
        NotesStorage.add.assert_called_once_with(note)

    def test_clear(self):
        NotesStorage.clear = MagicMock()
        self.test_object.clear()
        NotesStorage.clear.assert_called_once_with()

    @parameterized.expand([
        ("", ValueError),
        (5, ValueError),
        (5.5, ValueError),
        (True, ValueError),
        (None, ValueError),
        ([1,2,3], ValueError),
        ({'name': 2, 'grades': 4}, ValueError),
    ])
    def test_averageOf_wrong_name(self, name, expected_exception):
        NotesStorage.getAllNotesOf = MagicMock(return_value=[Note("note", 3), Note("note", 4), Note("note", 5)])
        with self.assertRaises(expected_exception):
            self.test_object.averageOf(name)

    @parameterized.expand([
        ("note", ValueError),
        ("", ValueError),
        (5, ValueError),
        (5.5, ValueError),
        (True, ValueError),
        (None, ValueError),
        ([1,2,3], ValueError),
        ({'name': 2, 'grades': 4}, ValueError),
    ])
    def test_add_wrong_note(self, name, expected_exception):
        NotesStorage.add = MagicMock()
        with self.assertRaises(expected_exception):
            self.test_object.add(name)

    def tearDown(self):
        del self.test_object