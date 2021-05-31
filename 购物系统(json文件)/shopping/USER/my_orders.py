# -*- coding: utf-8 -*-
import os
import sys
import tkinter
from tkinter import messagebox
from tkinter import ttk

sys.path.append('../')
from COMMON import MyFile

from COMMON.ReadJson import ReadJson
from COMMON.pub import *


def insert_data(data_list):
    for one_data in data_list:
        tree.insert('', tkinter.END, value=one_data)


def cancel():
    selects = tree.selection()
    if len(selects) != 1:
        messagebox.showinfo('提示', '请选择一个订单')
    else:
        data2 = tree.item(selects[0], 'values')

        all_orders1 = ReadJson(ORDERS_FILE).load_data()

        pop_index = None
        for j in all_orders1:
            if j.get(SHOP_NAME, '') == data2[0] and j.get(GOODS_NAME, '') == data2[1] and j.get(
                    GOODS_PRICE, '') == data2[2] and j.get(BUY_COUNT, '-1') == data2[3] and j.get(
                    STATUS, '') == data2[4]:

                pop_index = all_orders1.index(j)
                if j.get(STATUS, '') == SHIPPED:
                    messagebox.showinfo('提示信息', '商家已经发货了喲，联系客服退货后取消')
                    return
                if j.get(STATUS, '') == RECEIVED:
                    messagebox.showinfo('提示信息', '您已经收货了喲，联系客服退货后取消')
                    return
                if j.get(STATUS, '') == DELAY_SEND:
                    messagebox.showinfo('提示信息', '商家暂缓发货，联系客服退货后取消')
                    return

                break

        if pop_index is not None:
            all_orders1.pop(pop_index)

        MyFile.write_file(ORDERS_FILE, all_orders1)
        window.destroy()
        os.system('python my_orders.py')


def confirm_geted_goods():
    selects = tree.selection()
    if len(selects) != 1:
        messagebox.showinfo('提示', '请选择一个订单')
    else:
        data2 = tree.item(selects[0], 'values')

        all_orders = ReadJson(ORDERS_FILE).load_data()

        for j in all_orders:
            if j.get(SHOP_NAME, '') == data2[0] and j.get(GOODS_NAME, '') == data2[1] and j.get(
                    GOODS_PRICE, '') == data2[2] and j.get(BUY_COUNT, '-1') == data2[3] and j.get(
                    STATUS, '') == data2[4]:

                if j.get(STATUS, '') in [ORDERED, DELAY_SEND]:
                    messagebox.showinfo('提示信息', '商家还未发货喲')
                    return
                if j.get(STATUS, '') == RECEIVED:
                    messagebox.showinfo('提示信息', '不可以重复收货喲')
                    return

                j[STATUS] = RECEIVED
                break

        MyFile.write_file(ORDERS_FILE, all_orders)

        window.destroy()

        os.system('python my_orders.py')


def delete_kucun(j):
    pass


def btn1_event():
    window.destroy()
    os.system('python choose.py')


if __name__ == '__main__':
    window = tkinter.Tk()
    frame = tkinter.Frame(window)
    select_label = tkinter.Label(window, text='个人订单', font=('', FONT_SIZE_24))
    field_names = ['店铺名称', '商品名称', '商品价格', '购买数量', '订单状态']
    tree = ttk.Treeview(frame, columns=field_names, show='headings')
    for field_name in field_names:
        tree.column(field_name, width=150)
        tree.heading(field_name, text=field_name)

    my_json = ReadJson(ORDERS_FILE)
    data = my_json.load_data()
    all_orders = data

    my_json1 = ReadJson(CURRENT_USER_FILE)
    current_usr_info = my_json1.load_data()
    current_usr = current_usr_info.get(CUSTOMER_USER, '')

    self_orders = []
    for i in all_orders:
        if i.get(CUSTOMER_USER) == current_usr:

            self_orders.append(i)
            pass

    things = []
    for obj in self_orders:
        shop_name = obj.get(SHOP_NAME, '')
        goods_name = obj.get(GOODS_NAME, '')
        goods_price = obj.get(GOODS_PRICE, '')
        goods_count = obj.get(BUY_COUNT, '-1')
        status = obj.get(STATUS, '')
        things.append((shop_name, goods_name, goods_price, goods_count, status))
    insert_data(things)
    s = tkinter.Scrollbar(frame)
    s.config(command=tree.yview)
    tree.config(yscrollcommand=s.set)
    frame2 = tkinter.Frame(window)
    update_btn = tkinter.Button(frame2, text='取消订单', command=cancel, font=('', FONT_SIZE_16), )
    update_btn2 = tkinter.Button(frame2, text='确认收货', command=confirm_geted_goods,
                                 font=('', FONT_SIZE_16), )
    btn1 = tkinter.Button(frame2, text='返回', command=btn1_event, font=('', FONT_SIZE_16), )

    s.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    tree.pack()
    select_label.pack(side=tkinter.TOP, padx=30, pady=60)
    frame.pack()
    padx = 20
    pady = 60
    update_btn.grid(row=0, column=1, padx=padx, pady=pady)
    update_btn2.grid(row=0, column=2, padx=padx, pady=pady)
    btn1.grid(row=0, column=4, padx=padx, pady=pady)
    frame2.pack()

    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    width = 800
    height = 600
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    window.title(CUSTOMER_APP_TITLE)
    window.resizable(0, 0)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.mainloop()
