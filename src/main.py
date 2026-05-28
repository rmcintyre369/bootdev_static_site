from textnode import TextNode, TextType


def main():
    node = TextNode("test text", TextType.LINK, "www.test.com")
    print(node)


main()
