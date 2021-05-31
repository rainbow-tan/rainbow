# -*- coding: utf-8 -*-
import os
import sys
import tkinter
from tkinter import messagebox
from tkinter import ttk

sys.path.append('../')
from COMMON.ReadJson import ReadJson
from COMMON.pub import *


def insert_data(data_list):
    for one_data in data_list:
        tree.insert('', tkinter.END, value=one_data)


def buy_goods():
    selects = tree.selection()
    if len(selects) != 1:
        messagebox.showinfo('提示', '选择需要购买的一种商品')
    else:
        data1 = tree.item(selects[0], 'values')

        window.destroy()
        os.system('python buy_number.py {good_name} {good_price} {good_count}'.format(
                good_name=data1[0], good_price=data1[1], good_count=data1[2]))


def btn1_event():
    window.destroy()
    os.system('python see_shop.py')


if __name__ == '__main__':
    window = tkinter.Tk()
    frame = tkinter.Frame(window)
    select_label = tkinter.Label(window, text='查看信息', font=('', FONT_SIZE_24))
    field_names = ['商品名称', '商品价格', '商品数量']
    tree = ttk.Treeview(frame, columns=field_names, show='headings')
    for field_name in field_names:
        tree.column(field_name, width=100)
        tree.heading(field_name, text=field_name)

    my_json = ReadJson(SEE_SHOP_FILE)
    data = my_json.load_data()
    old_account = data.get(SHOP_USER, '')

    all_goods = data.get(SHOP_GOODS, {})

    field_data = list(all_goods.values())
    things = []
    for obj in field_data:
        name = obj.get(GOODS_NAME, '')
        price = obj.get(GOODS_PRICE, '')
        count = obj.get(COUNT, '')
        things.append((name, price, count))
    insert_data(things)
    s = tkinter.Scrollbar(frame)
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

    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    width = 600
    height = 600
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    window.title(CUSTOMER_APP_TITLE)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.mainloop()
