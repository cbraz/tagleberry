#!/usr/bin/env python3
import lib.scan
from lib.filedict import add_to_dict
import lib.FileMD
import json

file_dict = {}

def to_json(python_object):
    if isinstance(python_object, FileMD.FileMD):
        return {'__class__': 'FileMD', '__value__': python_object.__dict__}
    raise TypeError(repr(python_object) + ' is not JSON serializable')

def from_json(json_object):
    if '__class__' in json_object: 
        if json_object['__class__'] == 'FileMD':
            new_filemd = FileMD.FileMD(json_object['__value__']['path'])
            new_filemd.set_size(json_object['__value__']['size'])
            new_filemd.set_digest(json_object['__value__']['digest'])
            new_filemd.set_mtime(json_object['__value__']['mtime'])
            return new_filemd 
    return json_object

while True:
    print("options:\n\
    \t(r) - scan recursively\n\
    \t(l) - scan local directory only\n\
    \t(p) - print list of files\n\
    \t(w) - write data to disk\n\
    \t(o) - read data from disk\n\
    \t(x) - exit")
    option = input("select option: ")
    if option == "x":
        exit() 
    elif option == "r" or option == "l":
        user_dir = input("input directory to scan: ") 
        file_list = lib.scan.scandir(user_dir,option)
        add_to_dict(file_list, file_dict)
    elif option == "p":
        for k, v in file_dict.items():
            print("KEY:", k, "\nVALUE:", v)
    elif option == "w":
        with open('basic.json', mode='w', encoding='utf-8') as output_file:
            json.dump(file_dict, output_file,default=to_json, indent=2 )
    elif option == "o":
        with open('basic.json', mode='r', encoding='utf-8') as input_file:
            file_dict = json.load(input_file, object_hook=from_json)
    else:
        print("invalid option!")

