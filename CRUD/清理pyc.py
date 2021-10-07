# -*- encoding=utf-8 -*-
import os
import shutil


def traverse_folder(folder, only_first=False):
    folder = os.path.abspath(folder)
    all_files = []
    all_dirs = []
    if os.path.isdir(folder):
        for root, dirs, files in os.walk(folder):
            for one_file in files:
                all_files.append(os.path.join(root, one_file))  # 所有文件
            for one_dir in dirs:
                all_dirs.append(os.path.join(root, one_dir))  # 所有文件夹
            if only_first:
                break
    else:
        msg = 'Can not find folder:{} for traverse'.format(folder)
        print(msg)
    return all_dirs, all_files

def delete_folder(folder):
    folder = os.path.abspath(folder)
    if os.path.isdir(folder):
        try:
            shutil.rmtree(folder)
            msg = 'Success delete folder:{}'.format(folder)
            print(msg)
        except Exception as e:
            msg = 'Failed delete folder:{}, exception:{}'.format(folder, e)
            print(msg)


def delete_file(file):
    file = os.path.abspath(file)
    if os.path.isfile(file):
        try:
            os.remove(file)
            msg = 'Success delete file:{}'.format(file)
            print(msg)
        except Exception as e:
            msg = 'Failed delete file:{}, exception:{}'.format(file, e)
            print(msg)
def debug():
    all_dirs, all_files = traverse_folder('.')
    for dirname in all_dirs:
       if dirname.endswith('__pycache__'):
           delete_folder(dirname)
    for filename in all_files:
        if filename.endswith('.pyc'):
            delete_file(filename)

if __name__ == '__main__':
    debug()
