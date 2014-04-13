#!/usr/bin/env python3

import scan
from filelib import add_to_lib, add_to_dict
import FileData
import json

file_dict = {}


def to_json(o):
    return o.__dict__
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
        with open("basic.json", mode='w', encoding='utf-8') as output_file:
            json.dump(file_dict, output_file,default=to_json, indent=2 )
    else:
        print("invalid option!")

