from flask import render_template
from webapp import webapp

import lib.scan
from lib.filedict import add_to_dict
import lib.FileMD
import json

@webapp.route('/')
@webapp.route('/index')
def index():
    file_dict = {}
    user_dir = '/Users/celso/code/pitao/tagleberry/test'
    file_list = lib.scan.scandir(user_dir,'r')
    add_to_dict(file_list, file_dict)
    
    return render_template("index.html", file_dict = file_dict)

