# -*- coding: utf-8 -*-
import os
import sys
import tkinter
from tkinter import messagebox

sys.path.append('../')
from COMMON import MyFile

from COMMON.ReadJson import ReadJson
from COMMON.pub import *


def alert_buy():
    shop_good_name = sys.argv[1]
    shop_good_price = sys.argv[2]
    shop_good_count = sys.argv[3]

    try:
        int(user_entry1.get().strip())
    except:
        messagebox.showinfo('提示信息', '数量需要为整数')
        return
    if int(user_entry1.get().strip()) <= 0:
        messagebox.showinfo('提示信息', '数量需要大于0')
        return

    want_buy_count = str(int(user_entry1.get().strip()))

    all_orders = ReadJson(ORDERS_FILE).load_data([])

    current_usr_info = ReadJson(CURRENT_USER_FILE).load_data()
    current_usr = current_usr_info.get(CUSTOMER_USER, '')

    current_shop_info = ReadJson(SEE_SHOP_FILE).load_data()
    current_shop_usr = current_shop_info.get(SHOP_USER, '')
    see_shop_name = current_shop_info.get(SHOP_NAME, '')

    current_see_shop_goods = list(current_shop_info.get(SHOP_GOODS, {}).values())

    for shop_good in current_see_shop_goods:
        if shop_good.get(GOODS_NAME, '') == shop_good_name and shop_good.get(
                GOODS_PRICE) == shop_good_price:

            goods_count = shop_good.get(COUNT, '-1')

            if int(goods_count) - int(want_buy_count) < 0:
                msg = '库存不够，请少买点'
                messagebox.showinfo('提示信息', msg)
                return None
            break

    this_order = dict()
    this_order[CUSTOMER_USER] = current_usr
    this_order[SHOP_USER] = current_shop_usr
    this_order[STATUS] = ORDERED
    this_order[GOODS_NAME] = shop_good_name
    this_order[GOODS_PRICE] = shop_good_price
    this_order[BUY_COUNT] = want_buy_count
    this_order[SHOP_NAME] = see_shop_name

    all_orders.append(this_order)

    MyFile.write_file(ORDERS_FILE, all_orders)

    messagebox.showinfo('提示信息', '生成订单成功')
    root.destroy()
    os.system('python goods.py')
    pass


def btn2_event():
    root.destroy()
    os.system('python goods.py')
    pass


if __name__ == '__main__':

    root = tkinter.Tk()
    frame1 = tkinter.Frame(root)
    label1 = tkinter.Label(frame1, text='数量', font=('', 16), )
    btn2 = tkinter.Button(frame1, text='下单', command=alert_buy, font=('', 16), )
    btn1 = tkinter.Button(frame1, text='返回', command=btn2_event, font=('', 16), )
    user_entry1 = tkinter.Entry(frame1)
    padxx = 1
    padyy = 20
    frame1.pack()

    label1.grid(row=0, column=0, padx=padxx, pady=padyy)
    user_entry1.grid(row=0, column=1, padx=padxx, pady=padyy)
    btn2.grid(row=2, column=0, padx=padxx, pady=padyy)
    btn1.grid(row=2, column=1, padx=padxx, pady=padyy, sticky='e')

    root.title(CUSTOMER_APP_TITLE)

    screenwidth1 = root.winfo_screenwidth()
    screenheight2 = root.winfo_screenheight()
    width1 = 300
    height1 = 200
    x1 = int((screenwidth1 - width1) / 2)
    y1 = int((screenheight2 - height1) / 2)
    root.geometry('{}x{}+{}+{}'.format(width1, height1, x1, y1))
    root.mainloop()
