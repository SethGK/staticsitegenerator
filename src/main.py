from textnode import TextNode, TextType

def main():
    # Create a TextNode object with dummy values
    text_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    
    # Print the object
    print(text_node)

if __name__ == "__main__":
    main()
