import unittest
from splitnodes import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
)
from textnode import TextNode, TextType


class TestSplitNode(unittest.TestCase):
    def test_bold_split(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )

    def test_split_nodes_delimiter_invalid_markdown(self):
        node = TextNode("this is *invalid markdown", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "*", TextType.ITALIC)

    def test_split_nodes_delimiter_bold(self):
        node = TextNode("this is **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            result,
            [
                TextNode("this is ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT),
            ],
        )

    def test_split_nodes_delimiter_non_text_node_unchanged(self):
        node = TextNode("already bold", TextType.BOLD)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, [TextNode("already bold", TextType.BOLD)])

    def test_split_nodes_delimiter_multiple_pairs(self):
        node = TextNode("*one* and *two*", TextType.TEXT)
        result = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(
            result,
            [
                TextNode("one", TextType.ITALIC),
                TextNode(" and ", TextType.TEXT),
                TextNode("two", TextType.ITALIC),
            ],
        )

    def test_extract_markdown_images(self):
        text = "this is an ![image](https://example.com/image.png) in text"
        result = extract_markdown_images(text)
        self.assertEqual(result, [("image", "https://example.com/image.png")])

    def test_extract_markdown_images_multiple(self):
        text = "![first](https://example.com/1.png) and ![second](https://example.com/2.png)"
        result = extract_markdown_images(text)
        self.assertEqual(
            result,
            [
                ("first", "https://example.com/1.png"),
                ("second", "https://example.com/2.png"),
            ],
        )

    def test_extract_markdown_links_ignores_images(self):
        text = "a [link](https://example.com) and an ![image](https://example.com/image.png)"
        result = extract_markdown_links(text)
        self.assertEqual(result, [("link", "https://example.com")])


if __name__ == "__main__":
    unittest.main()
