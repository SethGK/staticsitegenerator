import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_no_props(self):
        """Test that props_to_html returns an empty string when there are no properties."""
        node = HTMLNode(tag="p", value="Hello, World!")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_with_single_prop(self):
        """Test that props_to_html generates a single HTML attribute."""
        node = HTMLNode(tag="a", value="Click here", props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_with_multiple_props(self):
        """Test that props_to_html generates multiple HTML attributes."""
        node = HTMLNode(
            tag="a",
            value="Click here",
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        """Test that __repr__ returns a string representation of the HTMLNode."""
        node = HTMLNode(tag="div", value="Content", props={"id": "main", "class": "container"})
        expected_repr = (
            "HTMLNode(tag='div', value='Content', children=[], "
            "props={'id': 'main', 'class': 'container'})"
        )
        self.assertEqual(repr(node), expected_repr)


if __name__ == "__main__":
    unittest.main()
