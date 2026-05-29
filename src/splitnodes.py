from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown syntax: no closing delimiter")
        for i, section in enumerate(sections):
            if section == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(section, TextType.TEXT))
            else:
                new_nodes.append(TextNode(section, text_type))

    return new_nodes


import re


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)


# def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
#     new_nodes = []
#     for node in old_nodes:
#         images = extract_markdown_images(node.text)
#         for image in images:
#             section = node.text.split(f"{image}", 1)
