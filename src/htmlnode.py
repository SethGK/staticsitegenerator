class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props 
    
    def to_html(self):
        if not self.tag:  # If there's no tag, return just the text (value)
            return self.value
        props_html = self.props_to_html()
        children_html = "".join([child.to_html() for child in self.children])  # Handle child nodes
        return f"<{self.tag}{props_html}>{self.value}{children_html}</{self.tag}>"
        
    def props_to_html(self):
        if not self.props:
            return ""
        return "".join(f' {key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
    