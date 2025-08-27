from utils import slugify
import unittest

class TestUtils(unittest.TestCase):
   
    def test_mostlySpecialCharacters(self):
        result = slugify('Hello*%!@*()')
        self.assertEqual(result, 'hello')

    def test_allSpaces(self):
        result = slugify('        ')
        self.assertEqual(result, '')

    def test_simplePhrase(self):
        result = slugify('Hello World!')
        self.assertEqual(result, 'hello-world')

if __name__ == '__main__':
    unittest.main()