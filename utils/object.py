import os
import zlib
from utils.search import find_dot

# def read_object(type , sha):

#     dot_path = find_dot(os.getcwd())

#     object_path = os.path.join(dot_path , "objects" , sha[:2] , sha[2:])

#     with open(object_path) as object_file:

#         content = zlib.decompress(object_file.read())


def write_object(object, write=False):

    
    fmt = object.object_format

def isblob(content):
    return True
