
import sys
import argparse
import os
from repository import Repository

class Dot:

    """
        init  -- initialize a repository
        idx   -- index files and folders
        save  -- commit the changes to the dot history
        log   -- display the logs of the repository 
    """

    def idx(self , args):
        print("idx" , args)
    
    def init(self , args):

        repo = Repository(os.getcwd())
        repo.create()
    
    def save(self , args):
        print("save" , args.filenames)
        

    def log(self , args):
        print("log" , args)
        

    def run(self):

        cli = argparse.ArgumentParser(description="Version control sytem")

        sub_parser = cli.add_subparsers(title="Commands" , dest="command")

        init = sub_parser.add_parser("init" , help="Initialize a dot repo")

        idx  = sub_parser.add_parser("idx")
        idx.add_argument("filenames" , nargs="+")

        save = sub_parser.add_parser("save")
        save.add_argument("filenames" , nargs="+")

        log  = sub_parser.add_parser("log")
        log.add_argument("-l" , "--limit" , type=int)

        cli.add_argument("-v" , "-version" , help="Display the current version of dot")
        
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
            case _:
                cli.print_help()

Dot().run()