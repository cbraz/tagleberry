#!/usr/bin/env python3

import scan
from filelib import add_to_lib
import FileData
from pprint import pprint


library = []

while True:
    print("options:\n\
    \t(r) - scan recursively\n\
    \t(l) - scan local directory only\n\
    \t(p) - print list of files\n\
    \t(x) - exit")
    option = input("select option: ")
    if option == "x":
        exit() 
    elif option == "r" or option == "l":
        user_dir = input("input directory to scan: ") 
        file_list = scan.scandir(user_dir,option)
        add_to_lib(file_list, library) 
    elif option == "p":
        pprint(library)
    else:
        print("invalid option!")
   

