import unittest
from markdown_to_html import markdown_to_html_node, extract_title
from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType


class MarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_heading_block_type(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)

    def test_code_block_type(self):
        self.assertEqual(block_to_block_type("```print('hi')```"), BlockType.CODE)

    def test_quote_block_type(self):
        self.assertEqual(block_to_block_type("> quoted text"), BlockType.QUOTE)

    def test_ordered_list_block_type(self):
        self.assertEqual(block_to_block_type("1. first item"), BlockType.OLIST)

    def test_paragraph(self):
        md = "this is a paragraph"
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><p>this is a paragraph</p></div>")

    def test_heading(self):
        md = "## this is a heading"
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><h2>this is a heading</h2></div>")

    def test_extract_heading(self):
        md = "# this is a heading"
        self.assertEqual(extract_title(md), "this is a heading")


if __name__ == "__main__":
    unittest.main()
