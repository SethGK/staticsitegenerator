from text_node_to_html_node import TextNode, TextType
from markdown_extractor import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue

        remaining_text = node.text
        for alt_text, url in images:
            # Split the text at the image markdown
            parts = remaining_text.split(f"![{alt_text}]({url})", 1)
            
            # Add the text before the image
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.NORMAL))  # Add text before the image
            
            # Add the image node with alt_text
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            
            remaining_text = parts[1] if len(parts) > 1 else ""  # Update remaining text after the image

        if remaining_text:  # If there's leftover text after all images
            new_nodes.append(TextNode(remaining_text, TextType.NORMAL))
    
    return new_nodes








def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue

        remaining_text = node.text
        for anchor_text, url in links:
            # Split the text at the link markdown
            parts = remaining_text.split(f"[{anchor_text}]({url})", 1)
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.NORMAL))  # Add text before the link
            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))  # Link node with anchor text
            remaining_text = parts[1]
        
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.NORMAL))
    
    return new_nodes

