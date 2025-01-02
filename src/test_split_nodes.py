import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_image, split_nodes_link

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an ![example](https://example.com/image.png) in it",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        expected_nodes = [
            TextNode("This is text with an ", TextType.NORMAL),
            TextNode("", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(" in it", TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_mixed_nodes(self):
        node = TextNode(
            "This is text with an ![example](https://example.com/image.png) and [a link](https://example.com) in it",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_image([node])
        new_nodes = split_nodes_link(new_nodes)
        expected_nodes = [
            TextNode("This is text with an ", TextType.NORMAL),
            TextNode("", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(" and ", TextType.NORMAL),
            TextNode("a link", TextType.LINK, "https://example.com"),
            TextNode(" in it", TextType.NORMAL),
        ]
        self.assertEqual(new_nodes, expected_nodes)

if __name__ == "__main__":
    unittest.main()
