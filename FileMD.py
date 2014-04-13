import json

def fmd_to_json(o):
    return o.__dict__

class FileMD:
    def __init__(self, p):
        self.path = p
        self.size = 0
        self.digest = 0
        self.mtime = 0
    def __str__(self):
        return json.dumps(self,default=fmd_to_json, indent=2 )
    def set_size(self, s):
        self.size = s
    def set_digest(self, h):
        self.digest = h
    def set_mtime(self, t):
        self.mtime = t
