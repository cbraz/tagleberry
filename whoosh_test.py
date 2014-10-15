#!/usr/local/bin/python3

from whoosh.fields import Schema, TEXT, ID
import os.path
from whoosh.index import create_in, open_dir
from whoosh.query import *
from whoosh.qparser import QueryParser


schema = Schema(path=ID(stored=True), hash=ID(stored=True))

if not os.path.exists("index"):
    os.mkdir("index")
    ix = create_in("index", schema)



ix = open_dir("index")
writer = ix.writer()

writer.add_document(path="/path/to/my/file", hash="D8F6DC5S5D7FD7D8")
writer.add_document(path="/path/to/copy/of/my/file", hash="D8F6DC5S5D7FD7D8")
writer.add_document(path="/path/to/some/other/file", hash="DD")
writer.commit()
with ix.searcher() as searcher:
    parser = QueryParser("hash", ix.schema)
    myquery = parser.parse("D8F6DC5S5D7FD7D8")
    results = searcher.search(myquery)
    #for i in results:
    l = len(results)
    print ("len(results) = ", l)
    i=0
    while i < l: 
    #for i in len(results):
        print("PATH: ",results[i]["path"])
        print("HASH: ",results[i]["hash"])
        print(results[i])
        i=i+1
