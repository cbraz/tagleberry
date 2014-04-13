import json

def fmd_to_json(o):
    return o.__dict__

class FileMD:
    def __init__(self, p):
        self.path = p
        self.filesize = 0
        self.filehash = 0
    def __str__(self):
        return json.dumps(self,default=fmd_to_json, indent=2 )
    def set_filesize(self, s):
        self.filesize = s
    def set_filehash(self, h):
        self.filehash = h
