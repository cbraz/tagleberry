from os import listdir
from os.path import isfile, isdir, join


# list all files in 'scan_dir' path, in local ("l") or recursive ("r") 'mode'
# returns list of all files with full path relative to provided 'scan_dir'
def scandir(scan_dir,mode):

    # get list of elements in 'scan_dir'
    try:
        file_list = listdir(scan_dir)
    except OSError:
        return 

    # will store list of files found
    result = []
    for elements in file_list:
        elements = join(scan_dir, elements)
        if mode == "l":
            if isfile(elements):
                result.append(elements)
        if mode == "r":
            if isdir(elements):
                result.extend(scandir(elements, mode))
            if isfile(elements):
                result.append(elements)
    return result
