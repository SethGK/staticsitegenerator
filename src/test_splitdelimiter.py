import unittest
from splitdelimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_with_bold(self):
        node = TextNode("This is **bold text**.", TextType.NORMAL)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold text", TextType.BOLD),
            TextNode(".", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_split_with_italic(self):
        node = TextNode("This is *italic text*.", TextType.NORMAL)
        result = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("italic text", TextType.ITALIC),
            TextNode(".", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_split_with_code(self):
        node = TextNode("Here is `code`.", TextType.NORMAL)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("Here is ", TextType.NORMAL),
            TextNode("code", TextType.CODE),
            TextNode(".", TextType.NORMAL),
        ]
        self.assertEqual(result, expected)

    def test_no_closing_delimiter(self):
        node = TextNode("Unmatched **bold text.", TextType.NORMAL)
        with self.assertRaises(ValueError) as context:
            split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(str(context.exception), "Unmatched delimiter '**' in text: Unmatched **bold text.")

    def test_no_delimiter_in_text(self):
        node = TextNode("Plain text with no delimiters.", TextType.NORMAL)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [TextNode("Plain text with no delimiters.", TextType.NORMAL)]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
