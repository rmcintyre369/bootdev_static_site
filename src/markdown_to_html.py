from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType
from htmlnode import HTMLNode, ParentNode
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node
import re


def markdown_to_html_node(markdown: str):
    nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type is BlockType.PARAGRAPH:
            nodes.append(paragraph_helper(block))
        elif block_type is BlockType.HEADING:
            nodes.append(heading_helper(block))
        elif block_type is BlockType.QUOTE:
            nodes.append(quote_helper(block))
        elif block_type is BlockType.CODE:
            nodes.append(code_helper(block))
        elif block_type is BlockType.ULIST:
            nodes.append(ulist_helper(block))
        elif block_type is BlockType.OLIST:
            nodes.append(olist_helper(block))
        else:
            raise ValueError("invalid blcok type")
    return ParentNode("div", nodes)


def text_to_children(text: str) -> list[HTMLNode]:
    new_nodes = []
    nodes = text_to_textnodes(text)
    for node in nodes:
        new_nodes.append(text_node_to_html_node(node))
    return new_nodes


def paragraph_helper(text: str) -> ParentNode:
    txt = text.replace("\n", " ")
    return ParentNode("p", text_to_children(txt))


def heading_helper(text: str) -> ParentNode:
    hashes, txt = text.split(" ", 1)
    tag = f"h{len(hashes)}"
    return ParentNode(tag, text_to_children(txt))


def quote_helper(text: str) -> ParentNode:
    txt = " ".join(line.lstrip(">").strip() for line in text.split("\n"))
    return ParentNode("blockquote", text_to_children(txt))


def code_helper(text: str) -> ParentNode:
    txt = text.strip("`").strip("\n")
    node = TextNode(txt, TextType.CODE)
    child = text_node_to_html_node(node)
    code_node = ParentNode("code", [child])
    return ParentNode("pre", [code_node])


def ulist_helper(text: str):
    new_nodes = []
    for line in text.split("\n"):
        line = line[2:].strip()
        new_nodes.append(ParentNode("li", text_to_children(line)))
    return ParentNode("ul", new_nodes)


def olist_helper(text: str):
    new_nodes = []
    for line in text.split("\n"):
        line = line.split(". ", 1)[1].strip()
        new_nodes.append(ParentNode("li", text_to_children(line)))
    return ParentNode("ol", new_nodes)


def extract_title(markdown: str) -> str:
    for line in markdown.split("\n"):
        if re.match("# ", line):
            line = line.lstrip("# ")
            return line.strip()
    raise ValueError("no heading found")
