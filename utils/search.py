import os

def find_dot(current_dir):

    # Find and return the location of the dot metadata directory.

    if os.path.exists(".dot"):
        return os.path.join(os.getcwd() , ".dot")
    
    parent  = os.path.realpath(os.path.join(current_dir, ".."))
    os.chdir(parent)
    return find_dot(parent)

def find_file(file_name):

    # return absolute path of any files in the worktree.
    dot_path = find_dot(os.getcwd())
    root_path = os.path.join( dot_path , os.pardir)
    work_tree = os.path.realpath(root_path)
    os.chdir(work_tree)

    for root, dirs, files in os.walk(work_tree):
        if ".git" in root or ".dot" in root :
            continue
        if file_name in dirs or file_name in files:
            return os.path.realpath(os.path.join(root , file_name))
    
    return None