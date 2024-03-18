import unittest
from app.io.input import input_from_file_builtin, input_from_file_pandas

class TestInputFunctions(unittest.TestCase):
    def test_input_from_file_builtin_1(self):
        text = input_from_file_builtin("test_data/test_input.txt")
        self.assertEqual(text, "Hello. It works!")

    def test_input_from_file_builtin_2(self):
        text = input_from_file_builtin("test_data/non_existing_test_input.txt")
        self.assertEqual(text, "File not found.")




if __name__ == '__main__':
    unittest.main()
