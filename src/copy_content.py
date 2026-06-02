import os
import shutil


def delete_contents(directory: str):
    if os.path.exists(directory):
        shutil.rmtree(directory)
        print(f"{directory} has been deleted")
    else:
        print(f"{directory} already cleaned")


def copy_content(source: str, target: str):
    if not os.path.exists(source):
        raise ValueError(f"{source} does not exist")
    if not os.path.exists(target):
        os.mkdir(target)
    files = os.listdir(source)
    for file in files:
        path = os.path.join(source, file)
        if os.path.isfile(path):
            shutil.copy(path, target)
            print(f"{file} copied to {target}")
        else:
            new_dir = os.path.join(target, file)
            os.makedirs(new_dir, exist_ok=True)
            print(f"{new_dir} folder created")
            copy_content(path, new_dir)


def copy_and_delete(source: str, target: str):
    delete_contents(target)
    copy_content(source, target)
