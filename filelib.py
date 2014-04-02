from FileData import FileData

def add_to_lib(file_list, library):
    for path in file_list:
        if path_exists(path, library):
            pass
        else:
            new_file = FileData(path)
            library.append(new_file)
        

def path_exists(path, library):
    print("checking file", path)
    for fd in library:
        if path == fd.path:
            print("equal") 
            return True
    print("not equal")
    return False


