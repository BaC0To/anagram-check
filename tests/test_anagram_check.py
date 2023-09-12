import unittest

from anagram_check import are_anagrams

class TestAnagramString(unittest.TestCase):


    def test_if_strings_are_anagrams(self):
        test_string1 = "python"
        test_string2 = "nohtyp"
        self.assertTrue(are_anagrams(test_string1, test_string2))

    def test_if_strings_are_not_anagrams(self):
        test_string1 = "python"
        test_string2 = "qwerty"
        self.assertFalse(are_anagrams(test_string1, test_string2))


if __name__ == '__main__':
    unittest.main()
