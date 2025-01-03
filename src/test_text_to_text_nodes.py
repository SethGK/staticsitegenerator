import unittest
from textnode import TextType, TextNode
from text_to_text_nodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_basic_text(self):
        text = "This is simple text."
        expected = [
            TextNode("This is simple text.", TextType.NORMAL)
        ]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_bold_text(self):
        text = "This is **bold** text."
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.NORMAL)
        ]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_italic_text(self):
        text = "This is *italic* text."
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text.", TextType.NORMAL)
        ]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_code_text(self):
        text = "This is `code` text."
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("code", TextType.CODE),
            TextNode(" text.", TextType.NORMAL)
        ]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_image_text(self):
        text = "This is an image: ![alt text](https://example.com/image.png)"
        expected = [
            TextNode("This is an image: ", TextType.NORMAL),
            TextNode("alt text", TextType.IMAGE, "https://example.com/image.png")
        ]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_link_text(self):
        text = "This is a [link](https://example.com)."
        expected = [
            TextNode("This is a ", TextType.NORMAL),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(".", TextType.NORMAL)
        ]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_combined_text(self):
        text = (
            "This is **bold**, *italic*, and `code` with an "
            "![image](https://example.com/image.png) and a [link](https://example.com)."
        )
        expected = [
            TextNode("This is ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(", ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(", and ", TextType.NORMAL),
            TextNode("code", TextType.CODE),
            TextNode(" with an ", TextType.NORMAL),
            TextNode("image", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(" and a ", TextType.NORMAL),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(".", TextType.NORMAL)
        ]
        self.assertEqual(text_to_textnodes(text), expected)


    def test_invalid_markdown(self):
        text = "This is an unclosed **bold and unclosed [link](https://example.com"
        expected = [TextNode(text, TextType.NORMAL)]
        self.assertEqual(text_to_textnodes(text), expected)

if __name__ == "__main__":
    unittest.main()
