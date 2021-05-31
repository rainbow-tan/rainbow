# -*- encoding=utf-8 -*-
import json
import os


def create_folder(folder):
    folder = os.path.abspath(folder)
    if not os.path.exists(folder):
        try:
            os.makedirs(folder)
            msg = 'Successful to create folder:{}'.format(folder)
            print(msg)
        except Exception as e:
            msg = 'Failed to create folder:{}, exception:{}'.format(folder, e)
            print(msg)


def write_file(filename, info, mode='w', encoding='utf-8', indent=4):
    filename = os.path.abspath(filename)
    create_folder(os.path.dirname(filename))
    with open(filename, mode, encoding=encoding) as f:
        json.dump(info, f, indent=indent, ensure_ascii=False)
