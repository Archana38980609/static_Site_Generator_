from textnode import TextNode, TextType

def main():
    node = TextNode("this is google link", TextType.LINK, "www.google.com")
    print(node)

if __name__ == "__main__":
    main()