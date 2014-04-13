class FileData:
    def __init__(self, p):
        self.path = p
        self.filesize = 0
        self.filehash = 0
#    def __str__(self):
#        return self.path
   
    def to_json(self):
        return self.__dict__
