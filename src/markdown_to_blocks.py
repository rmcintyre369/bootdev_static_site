from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = ("paragraph",)
    HEADING = ("heading",)
    CODE = ("code",)
    QUOTE = ("quote",)
    ULIST = ("unordered_list",)
    OLIST = "ordered_list"


def markdown_to_blocks(text: str) -> list[str]:
    new_blocks = []
    blocks = text.split("\n\n")
    for block in blocks:
        block = block.strip()
        if block != "":
            new_blocks.append(block)
    return new_blocks


def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")

    if re.match("#{1,6} ", block):
        return BlockType.HEADING
    if re.match(r"^```[\s\S]*```$", block):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH
