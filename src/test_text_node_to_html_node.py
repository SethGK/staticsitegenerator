import unittest
from textnode import TextNode, TextType
from text_node_to_html_node import text_node_to_html_node


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_type_text(self):
        text_node = TextNode("Plain text", TextType.NORMAL)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "Plain text")

    def test_text_type_bold(self):
        text_node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>Bold text</b>")

    def test_text_type_italic(self):
        text_node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<i>Italic text</i>")

    def test_invalid_input(self):
        with self.assertRaises(TypeError) as context:
            text_node_to_html_node("Not a TextNode")
        self.assertEqual(str(context.exception), "Expected a TextNode object")


if __name__ == "__main__":
    unittest.main()
