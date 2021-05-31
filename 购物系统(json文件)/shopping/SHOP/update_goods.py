# -*- coding: utf-8 -*-
import json
import os
import tkinter
from tkinter import *
from tkinter import messagebox

sys.path.append('../')
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
    window.destroy()
    os.system('python goods.py')


def add():
    old_name = sys.argv[1]
    add_name = entry1.get().strip()
    add_price = entry2.get().strip()
    add_count = entry3.get().strip()
    if add_name == '' or add_price == '' or add_count == '':
        messagebox.showinfo('提示信息', '信息不能为空')
        return None
    try:
        if int(add_count) <= 0:
            messagebox.showinfo('提示信息', '数量必须大于0')
            return
    except:
        messagebox.showinfo('提示信息', '数量必须为整数')
        return
    obj = ReadJson(CURRENT_SHOP_FILE)
    data = obj.load_data()

    current_user = data.get(SHOP_USER, '')
    remove_id = None
    current_goods = data.get(SHOP_GOODS, {})

    for i, j in current_goods.items():
        if j.get(GOODS_NAME) == old_name:

            remove_id = i
            break
    data[SHOP_GOODS].pop(remove_id)

    for i, j in current_goods.items():
        if j.get(GOODS_NAME) == add_name:

            msg = '该商品({})已经存在'.format(add_name)
            messagebox.showinfo('提示信息', msg)
            return None

    new_one_goods = dict()
    new_one_goods[GOODS_NAME] = add_name
    new_one_goods[GOODS_PRICE] = add_price
    new_one_goods[COUNT] = add_count

    all_goods = list(data[SHOP_GOODS].values())
    all_goods.append(new_one_goods)

    new = dict()
    for i, j in enumerate(all_goods):
        new[str(i + 1)] = j

    data[SHOP_GOODS] = new

    with open(CURRENT_SHOP_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    obj2 = ReadJson(SHOP_INFO_FILE)
    info = obj2.load_data()

    for i, j in info.items():
        usr = j.get(SHOP_USER, '')
        if current_user == usr:

            info[i] = data

    from COMMON import MyFile
    MyFile.write_file(SHOP_INFO_FILE, info)

    window.destroy()
    os.system('python goods.py')


if __name__ == '__main__':
    window = tkinter.Tk()
    window.title(SHOP_APP_TITLE)
    frame = tkinter.Frame(window)
    welcome_label = Label(window, text='修改商品', font=('', FONT_SIZE_24))
    label1 = tkinter.Label(frame, text='名称', font=('', FONT_SIZE_16), )
    label2 = tkinter.Label(frame, text='价格', font=('', FONT_SIZE_16), )
    label3 = tkinter.Label(frame, text='数量', font=('', FONT_SIZE_16), )
    login_btn = tkinter.Button(frame, text='修改', font=('', FONT_SIZE_16), command=add)
    register_btn = tkinter.Button(frame, text='返回', font=('', FONT_SIZE_16), command=back)

    shop_user1 = tkinter.StringVar()
    shop_user2 = tkinter.StringVar()
    shop_user3 = tkinter.StringVar()
    shop_user1.set(1)
    shop_user2.set(1)
    shop_user3.set(1)
    shop_user1.set(sys.argv[1])
    shop_user2.set(sys.argv[2])
    shop_user3.set(sys.argv[3])
    entry1 = tkinter.Entry(frame, text=shop_user1)
    entry2 = tkinter.Entry(frame, text=shop_user2)
    entry3 = tkinter.Entry(frame, text=shop_user3)

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

    window.title('购物系统')

    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    width = 500
    height = 600
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.mainloop()
