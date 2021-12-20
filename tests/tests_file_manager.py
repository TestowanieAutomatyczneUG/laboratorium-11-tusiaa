import unittest
from unittest.mock import *
from src.File_manager import *
from parameterized import parameterized

filePath = '/fake/file/path.txt'
class Test_file_manager(unittest.TestCase):
    def setUp(self):
        self.tmp = File_manager()

    def test_file_manager_read_file(self):
        OpenMock = mock_open(read_data="Hello World")
        with OpenMock(filePath, 'r') as mock:
            self.assertEqual(self.tmp.read_file(mock), "Hello World")

    def test_file_manager_add_to_file(self):
        OpenMock = mock_open(read_data="Hello World")
        with OpenMock(filePath, 'a') as mock:
            self.tmp.add_to_file(mock, " Hello")
            mock.write.assert_called_once_with(" Hello")

    def test_file_manager_delete_from_file(self):
        OpenMock = mock_open(read_data="Hello World")
        with OpenMock(filePath, 'w+') as mock:
            self.tmp.delete_from_file(mock, "Hello ")
            mock.assert_has_calls([call.read(), call.write('World')])

    @parameterized.expand([
        ("", ValueError),
        (5, ValueError),
        (5.5, ValueError),
        (True, ValueError),
        (None, ValueError),
        ([1,2,3], ValueError),
        ({'name': 2, 'grades': 4}, ValueError),
    ])
    def test_file_manager_add_to_file_wrong(self, value, error):
        OpenMock = mock_open(read_data="Hello World")
        with OpenMock(filePath, 'a') as mock:
            with self.assertRaises(error):
                self.tmp.add_to_file(mock, value)

    @parameterized.expand([
        ("", ValueError),
        (5, ValueError),
        (5.5, ValueError),
        (True, ValueError),
        (None, ValueError),
        ([1,2,3], ValueError),
        ({'name': 2, 'grades': 4}, ValueError),
    ])
    def test_file_manager_delete_from_file_wrong(self, value, error):
        OpenMock = mock_open(read_data="Hello World")
        with OpenMock(filePath, 'w+') as mock:
            with self.assertRaises(error):
                self.tmp.delete_from_file(mock, value)
            
    def tearDown(self):
        del self.tmp
