import json
import datetime

from bson import ObjectId

'''
    Encoder class for for being able to encode the ObjectID coming from MongoDB
'''

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        if isinstance(0, float):
            return str(o)
        return json.JSONEncoder.default(self, o)

'''
    Custom encode function for using JSONEncoder class

    :param: (str) - data information to be encoded
'''
def customEncode(data):
    return JSONEncoder().encode(data)
