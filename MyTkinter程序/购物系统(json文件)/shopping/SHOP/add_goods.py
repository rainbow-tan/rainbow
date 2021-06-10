# -*- coding: utf-8 -*-
import sys

sys.path.append('../')
from COMMON import MyFile
import json
import os
import tkinter
from tkinter import *
from tkinter import messagebox

from COMMON.ReadJson import ReadJson
from COMMON.pub import COUNT
from COMMON.pub import CURRENT_SHOP_FILE
from COMMON.pub import FONT_SIZE_16
from COMMON.pub import FONT_SIZE_24
from COMMON.pub import GOODS_NAME
from COMMON.pub import GOODS_PRICE
from COMMON.pub import SHOP_GOODS
from COMMON.pub import SHOP_INFO_FILE
from COMMON.pub import SHOP_USER
from COMMON.pub import SHOP_APP_TITLE


def back():
    # print('返回')
    window.destroy()
    os.system('python goods.py')


def add():
    value1 = entry1.get().strip()
    value2 = entry2.get().strip()
    value3 = entry3.get().strip()
    if value1 == '' or value2 == '' or value3 == '':
        messagebox.showinfo('提示信息', '信息不能为空')
        return None
    try:
        int(value3)
    except:
        messagebox.showerror('提示信息', '数量必须为整数')
        return
    obj = ReadJson(CURRENT_SHOP_FILE)
    data = obj.load_data()
    current_usr = data.get(SHOP_USER, '')
    # print('当前的店铺用户名:{}'.format(current_usr))
    # print('当前信息')
    # print(data)
    goods = data.get(SHOP_GOODS, {})
    # print('商品信息')
    # print(goods)
    now_goods = list(goods.values())
    # print('当前商品')
    # print(now_goods)
    new_goods_names = []
    for i in now_goods:
        new_goods_names.append(i.get(GOODS_NAME, ''))
    # print('商品名称列表')
    # print(new_goods_names)
    if value1 in new_goods_names:
        msg = '商品名称({})已经存在'.format(value1)
        messagebox.showinfo('提示信息', msg)
        return None
    new_goods = dict()
    new_goods[GOODS_NAME] = value1
    new_goods[GOODS_PRICE] = value2
    new_goods[COUNT] = value3
    # print('新加的商品')
    # print(new_goods)
    now_goods.append(new_goods)
    # print('加完商品后')
    # print(now_goods)
    new = {}
    for index, now_good in enumerate(now_goods):
        new[str(index + 1)] = now_good

    data[SHOP_GOODS] = new
    # print('===========')
    # print(data)
    with open(CURRENT_SHOP_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    obj2 = ReadJson(SHOP_INFO_FILE)
    info = obj2.load_data()
    # print('总商店信息')
    # print(info)
    for i, j in info.items():
        usr = j.get(SHOP_USER, '')
        if current_usr == usr:
            info[i] = data
    # print('*********更新店铺*********')
    # print(info)
    # with open(SHOP_INFO_FILE, 'w', encoding='utf-8') as f:
    #     json.dump(info, f, indent=4, ensure_ascii=False)
    MyFile.write_file(SHOP_INFO_FILE, info)
    # msg = '添加成功！！！'
    # messagebox.showinfo('提示信息', msg)
    window.destroy()
    os.system('python goods.py')


if __name__ == '__main__':
    window = tkinter.Tk()
    frame = tkinter.Frame(window)
    welcome_label = Label(window, text='添加商品', font=('', FONT_SIZE_24))
    label1 = tkinter.Label(frame, text='名称', font=('', FONT_SIZE_16), )
    label2 = tkinter.Label(frame, text='价格', font=('', FONT_SIZE_16), )
    label3 = tkinter.Label(frame, text='数量', font=('', FONT_SIZE_16), )
    login_btn = tkinter.Button(frame, text='添加', font=('', FONT_SIZE_16), command=add)
    register_btn = tkinter.Button(frame, text='返回', font=('', FONT_SIZE_16), command=back)
    entry1 = tkinter.Entry(frame)
    entry1.focus_set()
    entry2 = tkinter.Entry(frame)
    entry3 = tkinter.Entry(frame)

    welcome_label.pack(side=tkinter.TOP, padx=10, pady=40)
    frame.pack()
    padx = 10
    pady = 35
    label1.grid(row=0, column=0, padx=padx, pady=pady)
    label2.grid(row=1, column=0, padx=padx, pady=pady)
    label3.grid(row=2, column=0, padx=padx, pady=pady)
    entry1.grid(row=0, column=1, padx=padx, pady=pady)
    entry2.grid(row=1, column=1, padx=padx, pady=pady)
    entry3.grid(row=2, column=1, padx=padx, pady=pady)
    login_btn.grid(row=3, column=0, padx=10, pady=pady)
    register_btn.grid(row=3, column=1, padx=10, pady=35, sticky='e')

    window.title(SHOP_APP_TITLE)
    window.resizable(0, 0)
    screenwidth = window.winfo_screenwidth()  # 屏幕宽度
    screenheight = window.winfo_screenheight()  # 屏幕高度
    width = 500
    height = 600
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.mainloop()
