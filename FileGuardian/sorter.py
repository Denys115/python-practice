import os
import shutil

def sort_files_by_extension(file_path, base_directory):
    ext = os.path.splitext(file_path)[1].replace('.', "")
    if not ext: ext = "no_extension"
    
    target_subdir = os.path.join(base_directory, f"{ext}_files")
    
    if not os.path.exists(target_subdir):
        os.makedirs(target_subdir)
    
    dest_path = os.path.join(target_subdir, os.path.basename(file_path))
    
    if file_path != dest_path:
        shutil.move(file_path, dest_path)
        return dest_path
    return file_path