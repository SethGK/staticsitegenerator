import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_different_text(self):
        node1 = TextNode("Text A", TextType.BOLD, "https://example.com")
        node2 = TextNode("Text B", TextType.BOLD, "https://example.com")
        self.assertNotEqual(node1, node2)

    def test_eq_both_missing_url(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_eq_different_text_type(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://example.com")
        self.assertNotEqual(node1, node2) 





if __name__ == "__main__":
    unittest.main()