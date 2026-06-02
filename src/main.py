from copy_content import copy_and_delete
from generate_pages import generate_pages_recursive
import sys

basepath = sys.argv[1] if len(sys.argv) > 1 else "/"


def main():
    copy_and_delete("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)


if __name__ == "__main__":
    main()
