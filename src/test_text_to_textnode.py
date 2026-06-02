import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType


class TextToTextNode(unittest.TestCase):
    def test_text_to_textnodes_bold(self):
        text = "this is **bold** text"
        result = text_to_textnodes(text)
        self.assertEqual(
            result,
            [
                TextNode("this is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ],
        )

    def test_text_to_textnodes_italic(self):
        text = "this is _italic_ text"
        result = text_to_textnodes(text)
        self.assertEqual(
            result,
            [
                TextNode("this is ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.TEXT),
            ],
        )

    def test_text_to_textnodes_code(self):
        text = "this is `code` text"
        result = text_to_textnodes(text)
        self.assertEqual(
            result,
            [
                TextNode("this is ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" text", TextType.TEXT),
            ],
        )

    def test_text_to_textnodes_image(self):
        text = "this is an ![image](https://example.com/image.png)"
        result = text_to_textnodes(text)
        self.assertEqual(
            result,
            [
                TextNode("this is an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://example.com/image.png"),
            ],
        )

    def test_text_to_textnodes_mixed(self):
        text = "**bold** and _italic_ and `code` and ![image](https://example.com/image.png) and [link](https://example.com)"
        result = text_to_textnodes(text)
        self.assertEqual(
            result,
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" and ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" and ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://example.com/image.png"),
                TextNode(" and ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.com"),
            ],
        )


if __name__ == "__main__":
    unittest.main()
