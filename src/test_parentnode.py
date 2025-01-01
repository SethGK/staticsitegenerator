import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    def test_parentnode_with_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_parentnode_without_tag(self):
        with self.assertRaises(ValueError) as context:
            ParentNode(None, [LeafNode("b", "Bold text")])
        self.assertEqual(str(context.exception), "ParentNode must have a tag.")


    def test_parentnode_with_empty_children(self):
        with self.assertRaises(ValueError) as context:
            ParentNode("div", None)
        self.assertEqual(str(context.exception), "ParentNode must have children.")

if __name__ == "__main__":
    unittest.main()
