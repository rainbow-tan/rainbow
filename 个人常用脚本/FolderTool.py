import os
import shutil


def delete_folder(folder):
    folder = os.path.abspath(folder)
    if os.path.isdir(folder):
        try:
            shutil.rmtree(folder)
            msg = 'Success delete folder({})'.format(folder)
            print(msg)
        except Exception as e:
            msg = 'Failed delete folder({}), exception({})'.format(folder, e)
            print(msg)


def copy_folder(src, dst, delete=True):
    """
    :param src:
    :param dst:
    :param delete: 目标文件夹存在时,是否删除
    :return:
    """
    src = os.path.abspath(src)
    dst = os.path.abspath(dst)
    if delete:
        delete_folder(dst)
    try:
        shutil.copytree(src, dst)
        msg = 'Success copy folder({}) to ({})'.format(src, dst)
        print(msg)
    except Exception as e:
        msg = 'Fail copy folder({}) to ({}), exception({})'.format(src, dst, e)
        print(msg)


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
        msg = 'Can not find folder({}) for traverse'.format(folder)
        print(msg)
    return all_dirs, all_files
