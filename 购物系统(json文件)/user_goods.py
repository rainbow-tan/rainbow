# -*- coding: utf-8 -*-
import os
import tkinter
from tkinter import messagebox
from tkinter import ttk

from ReadJson import ReadJson
from pub import COUNT
from pub import FONT_SIZE_16
from pub import FONT_SIZE_24
from pub import GOODS_NAME
from pub import GOODS_PRICE
from pub import SEE_SHOP
from pub import SHOP_GOODS
from pub import SHOP_USER


def insert_data(data_list):
    for one_data in data_list:  # 插入数据
        tree.insert('', tkinter.END, value=one_data)


def buy_goods():
    selects = tree.selection()
    if len(selects) != 1:
        messagebox.showinfo('提示', '选择需要购买的一种商品')
    else:
        data1 = tree.item(selects[0], 'values')
        print(data1)
        window.destroy()
        os.system('python user_buy_number.py {} {}'.format(data1[0], data1[1]))


def btn1_event():
    print('返回')
    window.destroy()
    os.system('python user_see_shop.py')


if __name__ == '__main__':
    window = tkinter.Tk()
    frame = tkinter.Frame(window)
    select_label = tkinter.Label(window, text='查看信息', font=('', FONT_SIZE_24))
    field_names = ['商品名称', '商品价格', '商品数量']
    tree = ttk.Treeview(frame, columns=field_names, show='headings')
    for field_name in field_names:
        tree.column(field_name, width=100)  # 对列进行定义
        tree.heading(field_name, text=field_name)

    my_json = ReadJson(SEE_SHOP)
    data = my_json.load_data()
    old_account = data.get(SHOP_USER, '')

    all_goods = data.get(SHOP_GOODS, {})
    print("=====所有有的商品信息======")
    print(all_goods)
    print("============")

    field_data = list(all_goods.values())
    things = []
    for obj in field_data:
        name = obj.get(GOODS_NAME, '')
        price = obj.get(GOODS_PRICE, '')
        count = obj.get(COUNT, '')
        things.append((name, price, count))
    insert_data(things)
    s = tkinter.Scrollbar(frame)  # 滚动条
    s.config(command=tree.yview)
    tree.config(yscrollcommand=s.set)
    frame2 = tkinter.Frame(window)
    update_btn = tkinter.Button(frame2, text='购买', command=buy_goods, font=('', FONT_SIZE_16), )
    btn1 = tkinter.Button(frame2, text='返回', command=btn1_event, font=('', FONT_SIZE_16), )

    s.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    tree.pack()
    select_label.pack(side=tkinter.TOP, padx=30, pady=60)
    frame.pack()
    padx = 20
    pady = 60
    update_btn.grid(row=0, column=1, padx=padx, pady=pady)
    btn1.grid(row=0, column=4, padx=padx, pady=pady)
    frame2.pack()

    screenwidth = window.winfo_screenwidth()  # 屏幕宽度
    screenheight = window.winfo_screenheight()  # 屏幕高度
    width = 600
    height = 600
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.mainloop()
