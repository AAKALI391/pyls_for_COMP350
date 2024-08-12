import os
from datetime import datetime


def get_data(dir):
    if dir == None or dir=="":
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
        if os.path.os.access(filepath, os.X_OK):
            type = "x"
        if os.path.isdir(filepath):
            type = "d"
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
            out_str = i["last_mod"].strftime("%Y-%m-%d %H:%M:%S") + "\t" + str(i["size"]) +"\t"+ i["name"]
            print(out_str)
    if not l:
        for i in file_meatadata:
            print(i["name"])

metadata = get_data("")
print(metadata)