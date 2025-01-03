from htmlnode import HTMLNode
from text_to_text_nodes import text_to_textnodes
from block_to_block_type import block_to_block_type
from markdown_to_blocks import markdown_to_blocks

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [HTMLNode("span", value=node) for node in text_nodes]

def create_paragraph_node(text):
    return HTMLNode("p", children=text_to_children(text))

def create_heading_node(text, level):
    return HTMLNode(f"h{level}", children=text_to_children(text))

def create_code_block_node(text):
    return HTMLNode("pre", children=[HTMLNode("code", text)])

def create_quote_node(lines):
    children = [create_paragraph_node(line[1:].strip()) for line in lines]
    return HTMLNode("blockquote", children=children)

def create_unordered_list_node(lines):
    children = [HTMLNode("li", children=text_to_children(line[2:].strip())) for line in lines]
    return HTMLNode("ul", children=children)

def create_ordered_list_node(lines):
    children = [HTMLNode("li", children=text_to_children(line.split(". ", 1)[-1])) for line in lines if ". " in line]
    return HTMLNode("ol", children=children)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent_node = HTMLNode("div")

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == "paragraph":
            parent_node.children.append(create_paragraph_node(block))

        elif block_type == "heading":
            level = block.count("#")
            text = block[level + 1:].strip()
            parent_node.children.append(create_heading_node(text, level))

        elif block_type == "code":
            content = "\n".join(block.split("\n")[1:-1])
            parent_node.children.append(create_code_block_node(content))

        elif block_type == "quote":
            lines = block.split("\n")
            parent_node.children.append(create_quote_node(lines))

        elif block_type == "unordered_list":
            lines = block.split("\n")
            parent_node.children.append(create_unordered_list_node(lines))

        elif block_type == "ordered_list":
            lines = block.split("\n")
            parent_node.children.append(create_ordered_list_node(lines))

    return parent_node
