from leafnode import LeafNode
from textnode import TextNode, TextType

def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise TypeError("Expected a TextNode object")
    
    text = text_node.text or ""  # Default to empty string if text is None
    url = text_node.url or ""  # Default to empty string if url is None

    print(f"Converting TextNode with text: {text} and url: {url}")

    if text_node.text_type == TextType.NORMAL:
        return LeafNode(None, text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text)
    elif text_node.text_type == TextType.LINK:
        if not url:
            raise ValueError("TextType.LINK requires a URL.")
        return LeafNode("a", text, {"href": url})
    elif text_node.text_type == TextType.IMAGE:
        if not url:
            raise ValueError("TextType.IMAGE requires a URL.")
        return LeafNode("img", "", {"src": url, "alt": text})
    else:
        raise ValueError(f"Unsupported TextType: {text_node.text_type}")

