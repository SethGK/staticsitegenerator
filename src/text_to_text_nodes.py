from textnode import TextType, TextNode
from split_nodes import split_nodes_image, split_nodes_link
from splitdelimiter import split_nodes_delimiter

def text_to_textnodes(text):
    try:
    # Step 1: Convert raw text into a single TextNode
        nodes = [TextNode(text, TextType.NORMAL)]
        
        # Step 2: Apply splitting functions in order
        # Split bold text
        nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        # Split italic text
        nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
        # Split code text
        nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        # Split image markdown
        nodes = split_nodes_image(nodes)
        # Split link markdown
        nodes = split_nodes_link(nodes)

    except ValueError as e:
        # If there's an unmatched delimiter, treat the text as normal
        nodes = [TextNode(text, TextType.NORMAL)]

    # Return the final list of TextNodes
    return nodes
