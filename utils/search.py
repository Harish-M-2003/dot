import os

def find_dot(current_dir):

    if os.path.exists(".dot"):
        return os.path.join(os.getcwd() , ".dot")
    
    parent  = os.path.realpath(os.path.join(current_dir, ".."))
    os.chdir(parent)
    return find_dot(parent)
