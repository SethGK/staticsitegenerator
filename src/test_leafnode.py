import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leafnode_with_tag_and_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leafnode_without_tag(self):
        node = LeafNode(None, "Raw text")
        self.assertEqual(node.to_html(), "Raw text")

    def test_leafnode_with_no_value(self):
        with self.assertRaises(ValueError) as context:
            LeafNode("p", None)
        self.assertEqual(str(context.exception), "LeafNode must have a value")

    def test_leafnode_with_no_props(self):
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")

    def test_leafnode_empty_props(self):
        node = LeafNode("div", "Content", {})
        self.assertEqual(node.to_html(), "<div>Content</div>")

if __name__ == "__main__":
    unittest.main()
