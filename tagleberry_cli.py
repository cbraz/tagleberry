#!/usr/bin/env python3

import scan

while True:
    print("options:\n\
    \t(r) - scan recursively\n\
    \t(l) - scan local directory only\n\
    \t(x) - exit")
    option = input("select option: ")
    if option == "x":
        exit() 
    if option == "r" or option == "l":
        user_dir = input("input directory to scan: ") 
        scan.scandir(user_dir,option)
    else:
        print("invalid option!")


