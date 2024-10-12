import os
import zlib
import hashlib

class GitObject:

    def serialize(self , data):
        
        return zlib.compress(data)

    def deserialize(self , path , type_):
        if os.path.exists(path):
                
            with open(path , "rb") as object_file:
                decompressed_fmt = zlib.decompress(object_file.read()).split(b"@")
                if decompressed_fmt[0].decode("utf-8") == type_:
                    print(decompressed_fmt[-1].decode("utf-8"))
                else:
                    print("dot : Corrupted HEAD pointer file error")
        else:
                print("dot : Bad HEAD pointer")

    def get_object(self , repo , type_ , hash):

        if os.path.exists(repo.dot_dir):
            path = os.path.join(repo.dot_dir , "objects" , hash[:2] , hash[2:])
         
            self.deserialize(path , type_)
        else:
            print("Not a dot repo")

    def get_hash(self , path):

        with open(path, "rb") as object_file:

            return hashlib.sha1(self.serialize(object_file.read())).hexdigest()
