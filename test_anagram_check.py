import unittest
from anagram_check import Anagram


class TestAnagram(unittest.TestCase):


    def setUp(self):
        self.try_anagrams = Anagram()
    
    def tearDown(self):
        del self.try_anagrams

    def test_equal_length_strings_anagram(self):
        result = self.try_anagrams.strings_anagram_checker("act", "cat")
        self.assertTrue(result)

    def test_equal_length_strings_not_anagram(self):
        result = self.try_anagrams.strings_anagram_checker("act", "who")
        self.assertFalse(result)

    def test_unequal_length_strings(self):
        result = self.try_anagrams.strings_anagram_checker("sunny", "day")
        self.assertFalse(result)

    def test_first_parameter_not_strings(self):
        result = self.try_anagrams.strings_anagram_checker(123, "day")
        self.assertIsNone(result)
    
    def test_second_parameter_not_strings(self):
        result = self.try_anagrams.strings_anagram_checker("sunny", 345)
        self.assertIsNone(result)

    def test_both_parameters_not_strings(self):
        result = self.try_anagrams.strings_anagram_checker(1, 2)
        self.assertIsNone(result)
                          

if __name__ == "__main__":
    unittest.main()
