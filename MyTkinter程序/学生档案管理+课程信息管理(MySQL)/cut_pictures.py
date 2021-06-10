from io import BytesIO
import os
from tkinter import *

from PIL import Image
from PIL import ImageTk

import mytool


def resize_image_size(src, dst, width, height):
    msg = ''
    src = os.path.abspath(src)
    dst = os.path.abspath(dst)
    mytool.create_folder(os.path.dirname(dst))
    if os.path.isfile(src):
        try:
            old_img = Image.open(src)
            new_img = old_img.resize((width, height), Image.ANTIALIAS)
            new_img.save(dst)
        except Exception as e:
            msg = f'格式化图片失败:{e}'
    else:
        msg = f'未找到图片文件,格式化图片失败:{src}'
    return msg


def save_binary_image(src, dst):
    msg = ''
    src = os.path.abspath(src)
    dst = os.path.abspath(dst)
    byte = BytesIO()
    mytool.create_folder(os.path.dirname(dst))
    if os.path.isfile(src):
        try:
            img = Image.open(src)
            img.save(byte, format='png')
            value = byte.getvalue()
            with open(dst, 'wb') as f:
                f.write(value)
        except Exception as e:
            msg = f'保存图片为二进制失败:{e}'
    else:
        msg = f'未找到图片文件,存储二进制失败:{src}'
    return msg


def read_binary_image(src):
    open_image = None
    src = os.path.abspath(src)
    if os.path.isfile(src):
        try:
            with open(src, 'rb') as f:
                content = f.read()
            img = Image.open(BytesIO(content))  # 二进制转PIL
            open_image = ImageTk.PhotoImage(img)
        except Exception as e:
            msg = f'读取二进制图片失败:{e}'
            print(msg)
    else:
        msg = f'未找到二进制图片文件:{src}'
        print(msg)
    return open_image


if __name__ == '__main__':
    win = Tk()
    image = read_binary_image('tmp/aaa.txt')
    Label(image=image).pack()
    win.mainloop()
