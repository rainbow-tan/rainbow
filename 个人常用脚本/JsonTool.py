import json
import os


def load_json(file, default=None):
    if default is None:
        default = dict()
    json_data = default
    file = os.path.abspath(file)
    if os.path.isfile(file):
        with open(file, 'r') as f:
            try:
                json_data = json.load(f)
                msg = 'Success load json file({})'.format(file)
                print(msg)
            except Exception as e:
                msg = 'Failed load json file({})  exception({})'.format(file, e)
                print(msg)
    else:
        msg = 'Can not find file({}) for load json'.format(file)
        print(msg)
    return json_data
