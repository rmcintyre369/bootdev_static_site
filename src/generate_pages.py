from markdown_to_html import extract_title, markdown_to_html_node
import os


def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        contents = f.read()
        f.close()
    with open(template_path, "r") as f:
        template = f.read()
        f.close()

    html_content = markdown_to_html_node(contents).to_html()
    title = extract_title(contents)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_content)
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w+") as f:
        f.write(template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dir_path_content):
        raise ValueError(f"{dir_path_content} does not exist")
    files = os.listdir(dir_path_content)
    for file in files:
        print(file)
        path = os.path.join(dir_path_content, file)
        if file.endswith(".md"):
            html_name = os.path.splitext(file)[0] + ".html"
            generate_page(path, template_path, os.path.join(dest_dir_path, html_name))
        if os.path.isdir(path):
            generate_pages_recursive(
                os.path.join(dir_path_content, file),
                template_path,
                os.path.join(dest_dir_path, file),
            )
