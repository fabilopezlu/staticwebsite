from markdown_blocks import markdown_to_html_node, extract_title
import os

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as f:
        raw_lines = f.readlines()
    md_content = ''.join(raw_lines)

    with open(template_path) as f:
        raw_lines = f.readlines()
    template_content = ''.join(raw_lines)

    md_node = markdown_to_html_node(md_content)
    html_from_md = md_node.to_html()

    title = extract_title(md_content)
    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html_from_md)
    template_content = template_content.replace('href="/', f'href="{{{basepath}}}')
    template_content = template_content.replace('src="/', f'src="{{{basepath}}}')
    with open(dest_path, "a") as f:
        f.write(template_content)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = dest_path.replace(".md", ".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            oldmask = os.umask(000)
            os.mkdir(dest_path)
            os.umask(oldmask)
            generate_page_recursive(from_path, template_path, dest_path, basepath)