import os
import zlib
import hashlib
from utils.search import find_dot


class DotObject:

    def __init__(self, object_format):

        self.object_format = object_format

    def serialize(self, data):

        dot_path = find_dot(os.getcwd())

        sha1 = hashlib.sha1(data.encode()).hexdigest()
        objects_path = os.path.realpath(os.path.join(dot_path, "objects", sha1[:2]))

        if not os.path.exists(objects_path):
            os.makedirs(objects_path)

            with open(
                os.path.realpath(os.path.join(objects_path, sha1[2:])), "wb"
            ) as object_file:
                serialization_fmt = (
                    self.object_format.encode()
                    + b" "
                    + str(len(data)).encode("ascii")
                    + b"\x00"
                    + data.encode()
                )
                object_file.write(zlib.compress(serialization_fmt))

    def deserialize(self, hash_value):

        dot_path = find_dot(os.getcwd())

        object_path = os.path.realpath(
            dot_path, "objects", hash_value[:2], hash_value[2:]
        )

        if os.path.exists(object_path):

            with open(object_path, "rb") as object_file:

                content = zlib.decompress(object_file.read())
                print(content)

    #     return zlib.compress(data)

    # def deserialize(self , path , type_):
    #     if os.path.exists(path):

    #         with open(path , "rb") as object_file:
    #             decompressed_fmt = zlib.decompress(object_file.read()).split(b"@")
    #             if decompressed_fmt[0].decode("utf-8") == type_:
    #                 print(decompressed_fmt[-1].decode("utf-8"))
    #             else:
    #                 print("dot : Corrupted HEAD pointer file error")
    #     else:
    #             print("dot : Bad HEAD pointer")

    # def get_object(self , repo , type_ , hash):

    #     if os.path.exists(repo.dot_dir):
    #         path = os.path.join(repo.dot_dir , "objects" , hash[:2] , hash[2:])

    #         self.deserialize(path , type_)
    #     else:
    #         print("Not a dot repo")

    # def get_hash(self , path):

    #     with open(path, "rb") as object_file:

    #         return hashlib.sha1(self.serialize(object_file.read())).hexdigest()
