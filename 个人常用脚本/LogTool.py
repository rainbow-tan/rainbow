# -*- encoding=utf-8 -*-
import logging
import os
from logging.handlers import RotatingFileHandler


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


def rollback_logger(log_name='logs/log.log',
                    logger_name='ROLLBACK_LOGGER',
                    max_bytes=1024 * 1024 * 1,  # 1M
                    backup_count=10,
                    mode='a',
                    fmt_string='[%(asctime)s][%(name)s][%(levelname)s]%(message)s',
                    record_level=logging.INFO,
                    console_level=logging.INFO,
                    file_level=logging.INFO):
    __create_folder(os.path.dirname(log_name))
    fmt = logging.Formatter(fmt_string)  # 设置日志格式
    logger = logging.getLogger(logger_name)
    logger.setLevel(record_level)
    if not logger.handlers:  # 保证日志不重复
        stream_handler = logging.StreamHandler()  # 控制台日志句柄,设置则可以打印到控制台
        stream_handler.setLevel(console_level)  # 设置打印到控制台日志等级
        stream_handler.setFormatter(fmt)  # 设置打印的日志格式
        logger.addHandler(stream_handler)  # 添加控制台句柄
        # 设置回滚日志句柄
        rollback_handler = RotatingFileHandler(log_name, mode, max_bytes,
                                               backup_count)

        rollback_handler.setLevel(file_level)  # 设置回滚日志记录INFO以及以上信息
        rollback_handler.setFormatter(fmt)  # 设置打印的日志格式
        logger.addHandler(rollback_handler)  # 添加回滚日志句柄
    return logger  # 返回句柄，以便于使用


def general_logger(log_name,
                   logger_name='GENERAL_LOGGER',
                   mode='a',
                   record_level=logging.INFO,
                   console_level=logging.INFO,
                   file_level=logging.INFO,
                   fmt='[%(asctime)s][%(name)s][%(levelname)s]%(message)s'):
    log = logging.getLogger(logger_name)
    log.setLevel(record_level)

    if not log.handlers:  # 保证日志不重复
        formatter = logging.Formatter(fmt)
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(console_level)
        stream_handler.setFormatter(formatter)
        log.addHandler(stream_handler)

        if log_name:
            log_name = os.path.abspath(log_name)
            __create_folder(os.path.dirname(log_name))
            file_handler = logging.FileHandler(log_name, mode)
            file_handler.setLevel(file_level)
            file_handler.setFormatter(formatter)
            log.addHandler(file_handler)
    return log


def debug():
    log = rollback_logger()
    for i in range(1000):
        log.debug('debug message')
        log.info('info message')
        log.warning('warning message')
        log.error('error message')

    obj = general_logger('my_log/log.log')
    obj.info('AAA')


if __name__ == '__main__':
    debug()
