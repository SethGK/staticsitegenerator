import re

def extract_markdown_images(text):
    #Extract markdown image tags and return a list of tuples containing alt text and URLs.
    
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    
    return matches

def extract_markdown_links(text):
    #Extract markdown links and return a list of tuples containing anchor text and URLs.
    
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    
    return matches
