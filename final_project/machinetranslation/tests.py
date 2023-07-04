import unittest
from translator import english_to_french,french_to_english

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        english_text = 'Hello'
        expected = 'Bonjour'
        french_text = english_to_french(english_text)
        self.assertEqual(french_text,expected)
        self.assertNotEqual(french_text,'Hello')

    def test_frenchToEnglish(self):
        french_text = 'Bonjour'
        expected = 'Hello'
        english_text = french_to_english(french_text)
        self.assertEqual(english_text,expected)
        self.assertNotEqual(english_text,'Bonjour')

if __name__=="__main__":
    unittest.main()