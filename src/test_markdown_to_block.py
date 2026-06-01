import unittest
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


if __name__ == "__main__":
    unittest.main()
