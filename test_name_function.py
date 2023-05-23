import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'"""

    def test_first_last_name(self):
        """Do names like 'Charlotte Dyer' work?"""
        formatted_name = get_formatted_name('charlotte','dyer')
        self.assertEqual(formatted_name, 'Charlotte Dyer')

    def test_first_middle_last_name(self):
        """Do names with a middle name work?"""
        formatted_name = get_formatted_name(
            'charlotte', 'dyer', 'abad')
        self.assertEqual(formatted_name, 'Charlotte Abad Dyer')


if __name__ == '__main__':
    unittest.main()

