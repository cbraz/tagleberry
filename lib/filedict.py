from lib.FileMD import FileMD
from lib.scan import scan_file_info, full_digest

# adds new files to the file hash table
# file_list - list of file paths to add
# file_dict - hash table that contains all the file objects
def add_to_dict(file_list, file_dict):
    for path in file_list:
        # if path is not in dict, it generates exception and we add the file 
        try:
            file_dict[path]
            print("new")
        except KeyError:
            print("old")
            new_file = FileMD(path)
            file_dict[path] = new_file
            scan_file_info(new_file)
            full_digest(new_file)
