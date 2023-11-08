"""machinetranslation translation test cases"""
import unittest
from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    """english_to_french Test case"""

    def test1(self):
        """test1"""
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Test')


class TestFrenchToEnglish(unittest.TestCase):
    """french_to_english Test case"""

    def test1(self):
        """test1"""
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Test')


unittest.main()
