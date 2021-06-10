import json
import os
import shutil


def __create_folder(folder):
    folder = os.path.abspath(folder)
    if not os.path.exists(folder):
        try:
            os.makedirs(folder)
            msg = 'Success create folder({})'.format(folder)
            print(msg)
        except Exception as e:
            msg = 'Failed create folder({}), exception({})'.format(folder, e)
            print(msg)


def read_file(file, mode='r', line_type=False, encoding=None):
    file = os.path.abspath(file)
    if line_type:
        content = []
    else:
        content = ''
    if os.path.isfile(file):
        with open(file, mode, encoding=encoding) as f:
            if line_type:
                content = f.readlines()
            else:
                content = f.read()
    return content


def write_file(file, info, mode='w', encoding=None, indent=4):
    __create_folder(os.path.dirname(file))
    with open(file, mode, encoding=encoding) as f:
        if isinstance(info, str):
            f.write(info)
        elif isinstance(info, list):
            new_info = map(lambda x: str(x), info)
            f.writelines(new_info)
        elif isinstance(info, dict):
            info = json.dumps(info, indent=indent, ensure_ascii=False)
            f.write(info)
        else:
            msg = 'Unrecognized type'
            print(msg)


def delete_file(file):
    file = os.path.abspath(file)
    if os.path.isfile(file):
        try:
            os.remove(file)
            msg = 'Success delete file({})'.format(file)
            print(msg)
        except Exception as e:
            msg = 'Failed delete file({}), exception({})'.format(file, e)
            print(msg)


def copy_file(src, dst):
    # 目标文件存在,直接覆盖
    # 目标是文件夹,则在文件夹中生成同名文件
    __create_folder(os.path.dirname(dst))
    try:
        shutil.copy2(src, dst)
        msg = 'Success copy file({}) to ({})'.format(os.path.abspath(src), os.path.abspath(dst))
        print(msg)
    except Exception as e:
        msg = 'Fail copy file({}) to ({}), exception({})'.format(os.path.abspath(src),
                                                                 os.path.abspath(dst), e)
        print(msg)
