import inspect


################################################
###   Serialization to JSON

TAB = '\t'


def to_json(obj, level=0):
    '''Serializes the given object to JSON, printing to the console as it goes.'''

