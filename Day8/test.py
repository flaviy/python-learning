import unittest
import change_text


class TestChangeText(unittest.TestCase):  # TestChangeText is a subclass of unittest

    def test_uppercase(self):  # should start with test_
        self.assertEqual(change_text.all_capitals('test'), 'TEST')


if __name__ == '__main__':  # if the script is run directly from the command line
    unittest.main()  # run the tests
