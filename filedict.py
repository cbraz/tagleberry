from FileMD import FileMD

def add_to_lib(file_list, library):
    for path in file_list:
        if path_exists(path, library):
            pass
        else:
            new_file = FileMD(path)
            library.append(new_file)
        
def path_exists(path, library):
#    print("checking file", path)
    for fd in library:
        if path == fd.path:
#            print("path exists") 
            return True
#    print("path does not exist")
    return False


def add_to_dict(file_list, file_dict):
    for path in file_list:
        if is_path_in_dict(path, file_dict):
            pass
        else:
            new_file = FileData(path)
            file_dict[path] = new_file

def is_path_in_dict(path, file_dict):
#    print("checking file", path)
    
    #try to get path from dict
    try:
        file_dict[path]
#        print("path exists") 
        return True
    except KeyError:
#        print("path does not exist")
        return False


