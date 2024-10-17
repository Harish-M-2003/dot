import sys
import argparse
import os
from repository import Repository
from dotobject import DotObject
from utils import search

class Dot:

    # def __init__(self):

    #     self.dot_object = DotObject()

    def idx(self, args):

        print(search.find_dot(os.getcwd()))
        

    def init(self, args):

        repo = Repository(os.getcwd())
        repo.create()

    def save(self, args):
        print("save", args.filenames)

    def log(self, args):
        print("log", args)

    def hash_object(self, args): ...
        # implement a separate function which finds out the path of a given file
        # print(self.dot_object.get_hash(args.file))

    def cat_file(self, args): ...

        # object_hash = args.object
        # object_type = args.type

        # repo = Repository(os.getcwd())

        # self.dot_object.get_object(repo , object_type , object_hash)

    def run(self):

        cli = argparse.ArgumentParser(description="Version control sytem")

        sub_parser = cli.add_subparsers(title="Commands", dest="command")

        init = sub_parser.add_parser("init", help="Initialize a dot repo")

        idx = sub_parser.add_parser("idx")
        idx.add_argument("filenames", nargs="+")

        save = sub_parser.add_parser("save")
        save.add_argument("filenames", nargs="+")

        log = sub_parser.add_parser("log")
        log.add_argument("-l", "--limit", type=int)

        hash_object = sub_parser.add_parser("hash-object")
        hash_object.add_argument("file" , type=str)

        cat_file = sub_parser.add_parser(
            "cat-file", help="Provide content of repository objects"
        )
        cat_file.add_argument(
            "type",
            metavar="type",
            choices=["blob", "commit", "tag", "tree"],
            help="Specify the type",
        )
        cat_file.add_argument("object", metavar="object", help="The object to display")

        cli.add_argument("-v", "-version", help="Display the current version of dot")

        cli_args = cli.parse_args()

        match cli_args.command:
            case "init":
                self.init(cli_args)
            case "idx":
                self.idx(cli_args)
            case "save":
                self.save(cli_args)
            case "log":
                self.log(cli_args)
            case "hash-object":
                self.hash_object(cli_args)
            case "cat-file":
                self.cat_file(cli_args)
            case _:
                cli.print_help()


Dot().run()
