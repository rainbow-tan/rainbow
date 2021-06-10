# -*- encoding=utf-8 -*-
import datetime
import json
import os
import sys


def create_folder(folder):
    folder = os.path.abspath(folder)
    if not os.path.exists(folder):
        try:
            os.makedirs(folder)
        except Exception as e:
            msg = 'Failed to create folder({}), exception is({})'.format(folder, e)
            print(msg)


def read_file(file, mode='r', line_type=False, encoding=None):
    file = os.path.abspath(file)
    if line_type:
        content = []
    else:
        content = ''
    if not encoding:
        encoding = sys.getdefaultencoding()
    if os.path.isfile(file):
        with open(file, mode, encoding=encoding) as f:
            if line_type:
                content = f.readlines()
            else:
                content = f.read()
    return content


def write_file(file, info, mode='w', encoding=None):
    create_folder(os.path.dirname(file))
    if not encoding:
        encoding = sys.getdefaultencoding()
    with open(file, mode, encoding=encoding) as f:
        if isinstance(info, str):
            f.write(info)
        elif isinstance(info, list):
            info = map(lambda x: str(x), info)
            f.writelines(info)
        elif isinstance(info, dict):
            info = json.dumps(info, indent=4)
            f.write(info)
        else:
            pass


def now(fmt='%Y%m%d%H%M%S'):
    string = datetime.datetime.now().strftime(fmt)
    return string
