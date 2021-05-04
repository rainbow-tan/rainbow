# -*- encoding=utf-8 -*-
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


def write_dict(file, info, mode='w', encoding=None):
    create_folder(os.path.dirname(file))
    data = json.dumps(info, indent=4, ensure_ascii=False)
    with open(file, mode, encoding=encoding) as f:
        f.write(data)


def load_json(file):
    data = dict()
    file = os.path.abspath(file)
    if os.path.isfile(file):
        with open(file, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except Exception as e:
                msg = 'Failed to load json, file is({}), exception is({})'.format(file, e)
                print(msg)
    return data


if __name__ == '__main__':
    b = [dict(a='年后', b=2)]
    write_dict('test.json', b, encoding='utf-8')
    # with open('test1.json','w',encoding='utf-8') as f:
    #     pass
