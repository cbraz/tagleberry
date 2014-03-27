from os import listdir
from os.path import isfile, isdir, join


def scandir(scan_dir,mode):
    dir_elements = []
    for dir_elements in listdir(scan_dir):
        dir_elements = join(scan_dir,dir_elements)
        if mode == "l":
            if isfile(dir_elements):
                print("",dir_elements)
        if mode == "r":
            if isdir(dir_elements):
                print("DIR: ",dir_elements)
                scandir(dir_elements, mode)
            if isfile(dir_elements):
                print("",dir_elements)
 


