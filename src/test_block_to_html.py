import unittest
from block_to_html import markdown_to_html_node

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraph(self):
        markdown = "This is a paragraph."
        result = markdown_to_html_node(markdown)
        self.assertEqual(result.children[0].tag, "p")
        self.assertEqual(result.children[0].children[0].value.text, "This is a paragraph.")

    def test_heading(self):
        markdown = "# Heading"
        result = markdown_to_html_node(markdown)
        self.assertEqual(result.children[0].tag, "h1")
        self.assertEqual(result.children[0].children[0].value.text, "Heading")

    def test_code_block(self):
        markdown = "```\ncode block\n```"
        result = markdown_to_html_node(markdown)
        self.assertEqual(result.children[0].tag, "pre")
        self.assertEqual(result.children[0].children[0].tag, "code")
        self.assertEqual(result.children[0].children[0].value, "code block")

    def test_quote(self):
        markdown = "> This is a quote\n> Another line"
        result = markdown_to_html_node(markdown)
        self.assertEqual(result.children[0].tag, "blockquote")
        self.assertEqual(result.children[0].children[0].tag, "p")
        self.assertEqual(result.children[0].children[0].children[0].value.text, "This is a quote")

    def test_unordered_list(self):
        markdown = "* Item 1\n* Item 2"
        result = markdown_to_html_node(markdown)
        self.assertEqual(result.children[0].tag, "ul")
        self.assertEqual(result.children[0].children[0].tag, "li")
        self.assertEqual(result.children[0].children[0].children[0].value.text, "Item 1")

    def test_ordered_list(self):
        markdown = "1. Item 1\n2. Item 2"
        result = markdown_to_html_node(markdown)
        self.assertEqual(result.children[0].tag, "ol")
        self.assertEqual(result.children[0].children[0].tag, "li")
        self.assertEqual(result.children[0].children[0].children[0].value.text, "Item 1")

if __name__ == "__main__":
    unittest.main()
