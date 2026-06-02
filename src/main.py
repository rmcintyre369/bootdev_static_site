from copy_content import copy_and_delete
from generate_pages import generate_pages_recursive

dir_path_source = "./static"
dir_path_target = "./public"

gen_from_path = "./content/"
gen_template = "./template.html"
gen_to_path = "./public/"


def main():
    copy_and_delete(dir_path_source, dir_path_target)
    generate_pages_recursive(gen_from_path, gen_template, gen_to_path)


if __name__ == "__main__":
    main()
