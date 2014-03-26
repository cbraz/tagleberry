#!/usr/bin/env python

#from os import listdir
#from os.path import isfile, join
#onlyfiles = [ f for f in listdir(".") if isfile(join(".",f)) ]
#print onlyfiles

from os import walk

f = []
for (dirpath, dirnames, filenames) in walk(mypath):
        f.extend(filenames)
            break

