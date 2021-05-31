# -*- coding: utf-8 -*-
import os
import sys
import tkinter
from tkinter import messagebox
from tkinter import ttk

sys.path.append('../')
from COMMON import MyFile
from COMMON.pub import SHOP_USER
from COMMON.pub import SHIPPED
from COMMON.pub import ORDERED
from COMMON.pub import DELAY_SEND

from COMMON.ReadJson import ReadJson
from COMMON.pub import BUY_COUNT
from COMMON.pub import COUNT
from COMMON.pub import CURRENT_SHOP_FILE
from COMMON.pub import FONT_SIZE_16
from COMMON.pub import FONT_SIZE_24
from COMMON.pub import GOODS_NAME
from COMMON.pub import GOODS_PRICE
from COMMON.pub import NAME
from COMMON.pub import ORDERS_FILE
from COMMON.pub import SHOP_GOODS
from COMMON.pub import SHOP_INFO_FILE
from COMMON.pub import STATUS
from COMMON.pub import CUSTOMER_USER
from COMMON.pub import USER_ADDRESS
from COMMON.pub import USER_CONTACT
from COMMON.pub import USER_INFO_FILE
from COMMON.pub import SHOP_APP_TITLE


def insert_data(data_list):
    for one_data in data_list:
        tree.insert('', tkinter.END, value=one_data)


def buy_goods():
    selects = tree.selection()
    if len(selects) != 1:
        messagebox.showinfo('提示', '请选择一个订单')
    else:
        data2 = tree.item(selects[0], 'values')

        status_order = data2[7]

        if status_order == '已下单':

            all_orders1 = ReadJson(ORDERS_FILE).load_data()

            for one in all_orders1:
                customer_user = one.get(CUSTOMER_USER)

                status = one.get(STATUS)
                goods_name = one.get(GOODS_NAME)
                goods_price = one.get(GOODS_PRICE)
                if customer_user == data2[0] and goods_name == data2[4] and goods_price == data2[
                    5] and status == data2[7]:

                    one[STATUS] = DELAY_SEND
                    break

            MyFile.write_file(ORDERS_FILE, all_orders1)

            window.destroy()
            os.system('python my_orders.py')


def send_goods():
    selects = tree.selection()
    if len(selects) != 1:
        messagebox.showinfo('提示', '请选择一个订单')
    else:
        data2 = tree.item(selects[0], 'values')

        status_order = data2[7]
        if status_order == SHIPPED:
            messagebox.showinfo('提示信息', '不可以重复发货')
            return
        if status_order == ORDERED or status_order == DELAY_SEND:

            all_orders1 = ReadJson(ORDERS_FILE).load_data()

            for one in all_orders1:
                customer_user = one.get(CUSTOMER_USER)
                shop_usr = one.get(SHOP_USER)
                status = one.get(STATUS)
                goods_name = one.get(GOODS_NAME)
                goods_price = one.get(GOODS_PRICE)
                if customer_user == data2[0] and goods_name == data2[4] and goods_price == data2[
                    5] and status == data2[7]:

                    shopinfo = ReadJson(SHOP_INFO_FILE).load_data()

                    for one1 in shopinfo.values():
                        if one1.get(SHOP_USER) == shop_usr:

                            for good in one1.get(SHOP_GOODS, {}).values():

                                if good.get(GOODS_NAME) == goods_name and good.get(
                                        GOODS_PRICE) == goods_price:

                                    good_all_count = good.get(COUNT)

                                    if int(good_all_count) - int(data2[6]) < 0:
                                        messagebox.showinfo('提示信息',
                                                            '库存不足发货，发货需要{}，你现在有{}'.format(data2[6],
                                                                                          good_all_count))
                                        return
                                    else:
                                        good[COUNT] = str(int(good_all_count) - int(data2[6]))

                                        MyFile.write_file(SHOP_INFO_FILE, shopinfo)
                                        MyFile.write_file(CURRENT_SHOP_FILE, one1)
                                        break
                    one[STATUS] = SHIPPED

                    MyFile.write_file(ORDERS_FILE, all_orders1)
                    window.destroy()
                    os.system('python my_orders.py')
                    break


def btn1_event():
    window.destroy()
    os.system('python choose.py')


if __name__ == '__main__':
    window = tkinter.Tk()
    frame = tkinter.Frame(window)
    select_label = tkinter.Label(window, text='店铺订单', font=('', FONT_SIZE_24))
    field_names = ['用户账号', '用户姓名', '联系方式', '用户地址', '商品名称', '商品价格', '购买数量', '订单状态']
    tree = ttk.Treeview(frame, columns=field_names, show='headings')
    for field_name in field_names:
        tree.column(field_name, width=150)
        tree.heading(field_name, text=field_name)

    my_json = ReadJson(ORDERS_FILE)

    all_orders = my_json.load_data()

    my_json1 = ReadJson(CURRENT_SHOP_FILE)
    current_usr_info = my_json1.load_data()
    current_usr = current_usr_info.get(SHOP_USER, '')

    self_orders = []
    for i in all_orders:
        if i.get(SHOP_USER) == current_usr:

            self_orders.append(i)
            pass

    things = []
    for obj in self_orders:
        usr = obj.get(CUSTOMER_USER, '')

        my_json1 = ReadJson(USER_INFO_FILE)
        all_users = my_json1.load_data().values()
        name = ''
        for i in all_users:
            if i.get(CUSTOMER_USER, '') == usr:
                name = i.get(NAME, '')
                user_contact = i.get(USER_CONTACT, '')
                user_address = i.get(USER_ADDRESS, '')

                break
        goods_name = obj.get(GOODS_NAME, '')
        goods_price = obj.get(GOODS_PRICE, '')
        goods_count = obj.get(BUY_COUNT, '-1')
        status = obj.get(STATUS, '')
        things.append((usr, name, user_contact, user_address, goods_name, goods_price, goods_count,
                       status))
    insert_data(things)
    s = tkinter.Scrollbar(frame)
    s.config(command=tree.yview)
    tree.config(yscrollcommand=s.set)
    frame2 = tkinter.Frame(window)
    update_btn = tkinter.Button(frame2, text='暂缓发货', command=buy_goods, font=('', FONT_SIZE_16), )
    update_btn2 = tkinter.Button(frame2, text='确认发货', command=send_goods, font=('', FONT_SIZE_16), )
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
    width = 1200
    height = 600
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    window.title(SHOP_APP_TITLE)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.mainloop()
