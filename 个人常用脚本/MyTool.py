# -*- encoding=utf-8 -*-
import datetime
import json
import logging
import logging.handlers
import os
import shutil
import sys


def create_folder(folder):
    folder = os.path.abspath(folder)
    if not os.path.exists(folder):
        try:
            os.makedirs(folder)
        except Exception as e:
            msg = 'Failed to create folder({}), exception is({})'.format(folder, e)
            print(msg)


def delete_folder(folder):
    folder = os.path.abspath(folder)
    if os.path.isdir(folder):
        try:
            shutil.rmtree(folder)
        except Exception as e:
            msg = 'Failed to delete folder({}), exception is({})'.format(folder, e)
            print(msg)


def delete_file(file):
    file = os.path.abspath(file)
    if os.path.isfile(file):
        try:
            os.remove(file)
        except Exception as e:
            msg = 'Failed to delete file({}), exception is({})'.format(file, e)
            print(msg)


def copy_file(src, dst):
    # 目标文件存在,直接覆盖
    # 目标是文件夹,则在文件夹中生成同名文件
    create_folder(os.path.dirname(dst))
    try:
        shutil.copy2(src, dst)
    except Exception as e:
        src = os.path.abspath(src)
        dst = os.path.abspath(dst)
        msg = 'Failed to copy file({})->({}), exception is({})'.format(src, dst, e)
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
    except Exception as e:
        msg = 'Failed to copy folder({})->({}), exception is({})'.format(src, dst, e)
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


def load_json(file):
    data = dict()
    file = os.path.abspath(file)
    if os.path.isfile(file):
        with open(file, 'r') as f:
            try:
                data = json.load(f)
            except Exception as e:
                msg = 'Failed to load json, file is({}), exception is({})'.format(file, e)
                print(msg)
    return data


def now(fmt='%Y%m%d%H%M%S'):
    string = datetime.datetime.now().strftime(fmt)
    return string


def string_to_date(string, fmt='%Y-%m-%d %H:%M:%S'):
    # 2021-01-28 10:51:26
    date = datetime.datetime.strptime(string, fmt)
    return date


def date_to_string(date, fmt='%Y-%m-%d %H:%M:%S'):
    # 2021-01-28 10:51:26
    string = date.strftime(fmt)
    return string


def traverse_folder(folder):
    folder = os.path.abspath(folder)
    all_files = []
    all_dirs = []
    if os.path.isdir(folder):
        for root, dirs, files in os.walk(folder):
            for one_file in files:
                all_files.append(os.path.join(root, one_file))  # 所有文件
            for one_dir in dirs:
                all_dirs.append(os.path.join(root, one_dir))  # 所有文件夹
    return all_dirs, all_files


def init_logger(log_name='logs/log.log', max_bytes=1024 * 1024 * 1, backup_count=10,
                record_level=logging.INFO, console_level=logging.WARN, file_level=logging.INFO):
    """
    CRITICAL = 50
    FATAL = CRITICAL
    ERROR = 40
    WARNING = 30
    WARN = WARNING
    INFO = 20
    DEBUG = 10
    NOTSET = 0
    :param log_name:
    :param max_bytes:
    :param backup_count:
    :param record_level:
    :param console_level:
    :param file_level:
    :return:
    """
    create_folder(os.path.dirname(log_name))
    fmt = logging.Formatter('[%(asctime)s][%(levelname)s]%(message)s')  # 设置日志格式
    logger = logging.getLogger(log_name)
    logger.setLevel(record_level)

    stream_handler = logging.StreamHandler()  # 控制台日志句柄,设置则可以打印到控制台
    stream_handler.setLevel(console_level)  # 设置打印到控制台日志等级
    stream_handler.setFormatter(fmt)
    logger.addHandler(stream_handler)  # 添加控制台句柄
    # 设置回滚日志句柄
    rollback_handler = logging.handlers.RotatingFileHandler(log_name, 'a', max_bytes, backup_count)

    rollback_handler.setLevel(file_level)  # 设置回滚日志记录INFO以及以上信息
    rollback_handler.setFormatter(fmt)
    logger.addHandler(rollback_handler)  # 添加回滚日志句柄
    return logger  # 返回句柄，以便于使用


log = init_logger()
if __name__ == '__main__':
    print(now())