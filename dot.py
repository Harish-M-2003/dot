import sys
import argparse
import os
import zlib
from repository import Repository
from dotobject import DotObject
from utils.search import *
from utils.object import *
from hashlib import sha1


class Dot:

    # def __init__(self):

    #     self.repo = Repository(find_dot(os.getcwd()))
    #     self.dot_object = DotObject()

    def idx(self, args):

        dot_path = find_dot(os.getcwd())
        object_path = os.path.realpath(os.path.join(dot_path , "objects"))

        for filename in args.filenames:

            dot_object = DotObject("blob")
            
            file_path = find_file(filename)
            if file_path:
                with open(file_path , "r") as file:
                    dot_object.serialize(file.read())
            else:
                print("StageError : File does not exits") 


        

    def init(self, args):

        repo = Repository(os.getcwd())
        repo.create()

    def save(self, args):
        print("save", args.filenames)

    def log(self, args):
        print("log", args)

    def hash_object(self, args):
        # implement a separate function which finds out the path of a given file
        # print(self.dot_object.get_hash(args.file))

        file_path = find_file(args.file)

        if not file_path:
            raise FileNotFoundError("File " , args.file , "does not present in the work tree")
        
        with open(file_path , "rb") as file:
            content = file.read()
        
        sha_hash = sha1(content).hexdigest()

        # hashed_file = os.path.realpath(os.path.join(find_dot(os.getcwd()) , "objects" , sha_hash[:2]))
        # if not os.path.exists(hashed_file):
        #     os.makedirs(hashed_file)
        
        #     with open(os.path.join(hashed_file , sha_hash[2:]) , "wb") as file:
        #         object_fmt = b"blob" + b" " + str(len(content)).encode("ascii") + b"\x00" +  content
        #         file.write(zlib.compress(object_fmt))

        print(sha_hash)


    def cat_file(self, args):

        dot_path = find_dot(os.getcwd())
        hashed_file = os.path.join(dot_path , "objects" , args.object[:2] , args.object[2:])
        object_file = os.path.realpath(hashed_file)

        if os.path.exists(object_file):
            with open(object_file , "rb") as file:
                content = zlib.decompress(file.read()).decode()
                object_type = content[:content.find(" ")]
                data = content[content.find("\x00") + 1 : ]
                if object_type in ("commit" , "tree" , "blob"):
                    print(data)
                else:
                    print("Invalid data for cat-file")
        else:
            print("sha file Does not exits")

    def run(self):

        cli = argparse.ArgumentParser(description="Version control sytem")

        sub_parser = cli.add_subparsers(title="Commands", dest="command")

        init = sub_parser.add_parser("init", help="Initialize a dot repo")

        idx = sub_parser.add_parser("stage")
        idx.add_argument("filenames", nargs="+")

        save = sub_parser.add_parser("save")
        save.add_argument("filenames", nargs="+")

        log = sub_parser.add_parser("log")
        log.add_argument("-l", "--limit", type=int)

        hash_object = sub_parser.add_parser("hash")
        hash_object.add_argument("file" , type=str)

        cat_file = sub_parser.add_parser(
            "print", help="Provide content of repository objects"
        )
        # cat_file.add_argument(
        #     "type",
        #     metavar="type",
        #     choices=["blob", "commit", "tag", "tree"],
        #     help="Specify the type",
        # )
        cat_file.add_argument("object", metavar="object", help="The object to display")

        cli.add_argument("-v", "-version", help="Display the current version of dot")

        cli_args = cli.parse_args()

        match cli_args.command:
            case "init":
                self.init(cli_args)
            case "stage":
                self.idx(cli_args)
            case "save":
                self.save(cli_args)
            case "log":
                self.log(cli_args)
            case "hash":
                self.hash_object(cli_args)
            case "print":
                self.cat_file(cli_args)
            case _:
                cli.print_help()


Dot().run()
