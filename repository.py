import os
import configparser
import shutil

class Repository:

    def __init__(self, path):

        self.work_tree = path
        self.dot_dir = os.path.join(self.work_tree, ".dot")

    def create(self):

        if not os.path.exists(self.dot_dir):
            os.mkdir(self.dot_dir)
            os.mkdir(os.path.join(self.dot_dir, "objects"))
            os.mkdir(os.path.join(self.dot_dir, "refs"))
            os.mkdir(os.path.join(self.dot_dir, "refs", "heads"))
            os.mkdir(os.path.join(self.dot_dir, "refs", "tags"))
            os.mkdir(os.path.join(self.dot_dir, "hooks"))

            with open(os.path.join(self.dot_dir, "HEAD"), "w") as HEAD_FILE:
                HEAD_FILE.write("ref: refs/heads/main\n")

            with open(os.path.join(self.dot_dir, "description"), "w") as DESC_FILE:
                DESC_FILE.write(
                    "Unnamed repo ; edit this file 'description' to name the repos."
                )

            with open(os.path.join(self.dot_dir, "config.ini"), "w") as CONFIG_FILE:

                config = configparser.ConfigParser()
                config.add_section("core")
                config.set("core", "\trepositoryformatversion", "0")
                config.set("core", "\tfilemode", "false")
                config.set("core", "\tbare", "false")
                config.write(CONFIG_FILE)

        else:
            user_option = input("Do you want to reinitialize this repo [y/n] : ").strip()
            if user_option.startswith("y"):
                shutil.rmtree(self.dot_dir)
                self.create()
    
    def get_repo_root(self):
        return self.work_tree

    
