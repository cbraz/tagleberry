#!/usr/bin/env python3

import scan
from filedict import add_to_dict
import FileMD
import json

file_dict = {}


#def to_json(o):
#    return o.__dict__



def to_json(python_object):
    if isinstance(python_object, FileMD.FileMD):
        return {'__class__': 'FileMD', '__value__': python_object.__dict__}
    raise TypeError(repr(python_object) + ' is not JSON serializable')

def from_json(json_object):
    if '__class__' in json_object: 
        if json_object['__class__'] == 'FileMD':
            new_filemd = FileMD.FileMD(json_object['__value__']['path'])
            new_filemd.set_filesize(json_object['__value__']['filesize'])
            new_filemd.set_filehash(json_object['__value__']['filehash'])
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
        file_list = scan.scandir(user_dir,option)
        add_to_dict(file_list, file_dict)
    elif option == "p":
        for k, v in file_dict.items():
            print("KEY:", k, "VALUE:", v)
    elif option == "w":
        with open('basic.json', mode='w', encoding='utf-8') as output_file:
            json.dump(file_dict, output_file,default=to_json, indent=2 )
    elif option == "o":
        with open('basic.json', mode='r', encoding='utf-8') as input_file:
            file_dict = json.load(input_file, object_hook=from_json)
    else:
        print("invalid option!")

