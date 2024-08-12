import os
from datetime import datetime
import argparse

#taken from pyls sketch provided by professor
parser = argparse.ArgumentParser(
    prog="pyls",
    description="Lists files in given or current directory",
    epilog="Poor man's ls",
)
parser.add_argument(
    "dirname",
    help="Name of directory to list the contents of",
    action="store",
    nargs="?",
    default=".",
)
parser.add_argument(
    "-l",
    "--long-format",
    help="Presents more details about files in columnar format",
    action="store_true",
)
parser.add_argument(
    "-F",
    "--filetype",
    help="""Adds an extra character to the end of the printed
                            filename that indicates its type.""",
    action="store_true",
)
args = parser.parse_args()

def get_data(dir):
    if dir == None or dir==".":
        directory = os.getcwd()
    else:
        directory = os.getcwd()+"/"+dir
    file_data = []
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        metadata = os.stat(filepath)
        type = ""
        if os.path.isfile(filepath):
            type = "f"
        #checking if executable taken from stack overflow
        if os.path.os.access(filepath, os.X_OK):
            type = "x"
        if os.path.isdir(filepath):
            type = "d"
            #datetime formatting taken from stack overflow
        data = {"name":filename,"size": metadata.st_size,"last_mod":datetime.fromtimestamp(metadata.st_mtime),"type":type}
        file_data.append(data)
    return file_data

def format_data(file_meatadata,f,l):
    if f:
        for i in file_meatadata:
            if i["type"] == "d":
                i["name"] = i["name"]+"/"
            if i["type"] == "x":
                i["name"] = i["name"]+"*"
    if l:
        for i in file_meatadata:
            out_str = i["last_mod"].strftime("%Y-%m-%d %H:%M:%S")    + str(i["size"]).rjust(10) +"\t"+ i["name"]
            print(out_str)
    if not l:
        for i in file_meatadata:
            print(i["name"])

metadata = get_data(args.dirname)
format_data(metadata,args.filetype, args.long_format )
