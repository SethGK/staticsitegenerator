import unittest
from main import extract_title

class ExtractTitleTest(unittest.TestCase):
    def test_extract_title_valid(self):
        self.assertEqual(extract_title("# Hello"), "Hello")
        self.assertEqual(extract_title("# Hello\n## Subheader"),"Hello")

    def text_extract_title_no_h1(self):
        with self.assertRaises(ValueError):
            extract_title("## Subheader")


if __name__ == "__main__":
    unittest.main()