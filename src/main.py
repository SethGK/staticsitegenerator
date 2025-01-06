import os
import shutil
from block_to_html import markdown_to_html_node



def extract_title(markdown):
    for line in markdown.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No H1 header found in markdown")


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

def generate_page(from_path,template_path,dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown_content = f.read()

    with open(template_path, "r") as f:
        template_content = f.read()

    html_node = markdown_to_html_node(markdown_content)

    print(f"html_node type: {type(html_node)}") 
        
    html_content = html_node.to_html()

    title = extract_title(markdown_content)

    full_page = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(full_page)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    for root, _, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                markdown_path = os.path.join(root, file)
                relative_path = os.path.relpath(markdown_path, dir_path_content)
                output_path = os.path.join(dest_dir_path, relative_path).replace(".md", ".html")

                generate_page(markdown_path, template_path, output_path)

def main():
    if os.path.exists("public"):
         shutil.rmtree("public")

    copy_directory_recursive("static", "public")

    generate_page("content/index.md", "template.html", "public/index.html")
    

if __name__ == "__main__":
    dir_path_content = "content"
    template_path = "template.html"
    dest_dir_path = "public"
    generate_page_recursive(dir_path_content, template_path, dest_dir_path)
    

