from FileMD import FileMD
from scan import scan_file_info, full_digest

def add_to_dict(file_list, file_dict):
    for path in file_list:
        if is_path_in_dict(path, file_dict):
            pass
        else:
            new_file = FileMD(path)
            scan_file_info(new_file)
            full_digest(new_file)
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


