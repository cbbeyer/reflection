import inspect
import re


################################################
###   Serialization to JSON

TAB = '\t'

def to_json(obj, level=1):
    '''Serializes the given object to JSON, printing to the console as it goes.'''

    obj_type = obj.__dict__

    json_strings = []

    for key, val in sorted(obj_type.items()):

        if isinstance(val, bool):
            if val == True:
                json_strings.append('\n{}\"{}\": {}'.format(TAB * level, key, 'true'))
            elif val == False:
                json_strings.append('\n{}\"{}\": {}'.format(TAB * level, key, 'false'))

        elif isinstance(val, (int, float)):
            json_strings.append('\n{}\"{}\": {}'.format(TAB * level, key, val))

        # bool in python seen as 0 and 1 (int)

        elif isinstance(val, str):
            quote = re.search('"', val)
            slash = re.search('\\\\', val)

            if quote:
                val = val.replace('"', '\\"')

            if slash:
                val = val.replace('\\', '\\\\')

            json_strings.append('\n{}\"{}\": \"{}\"'.format(TAB * level, key, val))

        elif val is None:
            json_strings.append('\n{}\"{}\": {}'.format(TAB * level, key, 'null'))

        else:
            json_strings.append('\n{}\"{}\": {}'.format(TAB * level, key, to_json(val, level + 1)))

    return '{}{}\n{}{}'.format('{', ','.join(json_strings), (TAB * (level - 1)), '}')
