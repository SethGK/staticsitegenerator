from textnode import TextNode, TextType
import os
import shutil


def copy_directory_recursive(source,destination):

    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)

    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
            print(f"Copied file: {source_path} -> {destination_path}")

        elif os.path.isdir(source_path):
            os.mkdir(destination_path)
            print(f"Created directory: {destination_path}")
            copy_directory_recursive(source_path,destination_path)


def main():
    source_dir = "static"
    destination_dir = "public"

    copy_directory_recursive(source_dir, destination_dir)
    print("All files and directories copied successfully")

if __name__ == "__main__":
    main()
