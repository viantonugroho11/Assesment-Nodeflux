import model.alldata
from flask import jsonify

def alldata():
    return model.alldata.modelalldata()