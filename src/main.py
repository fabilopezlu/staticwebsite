import os
import shutil
import sys
from copystatic import copy_files_recursive
from gencontent import generate_page_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

def main(**args):
    basepath = sys.argv[1]
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    full_path = os.path.join(basepath, dir_path_public[2:])+"/"
    generate_page_recursive (
        os.path.join(dir_path_content),
        template_path,
        os.path.join(dir_path_public),
        os.path.join(full_path),
    )


main()