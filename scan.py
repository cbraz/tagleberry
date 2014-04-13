from os import listdir
from os.path import isfile, isdir, join, realpath


# list all files in 'scan_dir' path, in local ("l") or recursive ("r") 'mode'
# returns list of all files with full path relative to provided 'scan_dir'
def scandir(scan_dir,mode):

    # get list of file_i in 'scan_dir'
    try:
        file_list = listdir(scan_dir)
    except OSError:
        return 
    
    # will store list of files found
    result = []
    for file_i in file_list:
        # joins
        file_i = join(scan_dir, file_i)
        file_i = realpath(file_i)
         
        if mode == "l":
            if isfile(file_i):
                result.append(file_i)
        if mode == "r":
            if isdir(file_i):
                result.extend(scandir(file_i, mode))
            if isfile(file_i):
                result.append(file_i)
    return result


