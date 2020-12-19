# -*- coding: utf-8 -*-
import json
import os
import tkinter
from tkinter import *
from tkinter import messagebox

from COMMON.ReadJson import ReadJson
from COMMON.pub import COUNT
from COMMON.pub import CURRENT_SHOP
from COMMON.pub import FONT_SIZE_16
from COMMON.pub import FONT_SIZE_24
from COMMON.pub import GOODS_NAME
from COMMON.pub import GOODS_PRICE
from COMMON.pub import SHOP_GOODS
from COMMON.pub import SHOP_INFO
from COMMON.pub import SHOP_USER


def back():
    print('返回')
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

    obj = ReadJson(CURRENT_SHOP)
    data = obj.load_data()
    print('当前用户信息')
    print(data)
    current_user = data.get(SHOP_USER, '')
    remove_id = None
    current_goods = data.get(SHOP_GOODS, {})

    for i, j in current_goods.items():
        if j.get(GOODS_NAME) == old_name:
            print('找到修改的单个商品信息')
            print(j)
            remove_id = i
            break
    data[SHOP_GOODS].pop(remove_id)
    print(data)

    for i, j in current_goods.items():
        if j.get(GOODS_NAME) == add_name:
            print('存在单个商品')
            msg = '该商品({})已经存在'.format(add_name)
            messagebox.showinfo('提示信息', msg)
            return None

    new_one_goods = dict()
    new_one_goods[GOODS_NAME] = add_name
    new_one_goods[GOODS_PRICE] = add_price
    new_one_goods[COUNT] = add_count

    all_goods = list(data[SHOP_GOODS].values())
    all_goods.append(new_one_goods)
    print('新增后商品信息')
    print(all_goods)

    new = dict()
    for i, j in enumerate(all_goods):
        new[str(i + 1)] = j
    print('新增后的dict')
    print(new)

    data[SHOP_GOODS] = new
    print('新增后的店铺信息')
    print(data)

    with open(CURRENT_SHOP, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

    obj2 = ReadJson(SHOP_INFO)
    info = obj2.load_data()
    print('总商店信息')
    print(info)
    for i, j in info.items():
        usr = j.get(SHOP_USER, '')
        if current_user == usr:
            print('找到店铺的key:{}'.format(i))
            info[i] = data
    print('*********更新店铺*********')
    print(info)
    with open(SHOP_INFO, 'w', encoding='utf-8') as f:
        json.dump(info, f, ensure_ascii=False)
    msg = '修改成功！！！'
    messagebox.showinfo('提示信息', msg)
    window.destroy()
    os.system('python goods.py')


if __name__ == '__main__':
    window = tkinter.Tk()
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

    screenwidth = window.winfo_screenwidth()  # 屏幕宽度
    screenheight = window.winfo_screenheight()  # 屏幕高度
    width = 500
    height = 600
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.mainloop()
