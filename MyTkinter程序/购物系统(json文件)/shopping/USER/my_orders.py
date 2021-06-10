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
    for one_data in data_list:  # 插入数据
        tree.insert('', tkinter.END, value=one_data)


def cancel():
    selects = tree.selection()
    if len(selects) != 1:
        messagebox.showinfo('提示', '请选择一个订单')
    else:
        data2 = tree.item(selects[0], 'values')
        # print('选择的订单')
        # print(data2)

        # my_json1 = ReadJson(ORDERS_FILE)
        all_orders1 = ReadJson(ORDERS_FILE).load_data()
        # print("=====所有的订单信息======")
        # print(all_orders1)
        ###print("============")
        pop_index = None
        for j in all_orders1:
            if j.get(SHOP_NAME, '') == data2[0] and j.get(GOODS_NAME, '') == data2[1] and j.get(
                    GOODS_PRICE, '') == data2[2] and j.get(BUY_COUNT, '-1') == data2[3] and j.get(
                    STATUS, '') == data2[4]:
                # print('找到要取消的订单了:{}'.format(j))
                pop_index = all_orders1.index(j)
                if j.get(STATUS, '') == YIFAHUO:
                    messagebox.showinfo('提示信息', '商家已经发货了喲，联系客服退货后取消')
                    return
                if j.get(STATUS, '') == YISHOUHUO:
                    messagebox.showinfo('提示信息', '您已经收货了喲，联系客服退货后取消')
                    return
                if j.get(STATUS, '') == ZANHUANFAHUO:
                    messagebox.showinfo('提示信息', '商家暂缓发货，联系客服退货后取消')
                    return
                # delete_kucun(j)

                break
        # print(pop_index)
        if pop_index is not None:
            all_orders1.pop(pop_index)
            # print('@@@')
        # print('删除后的订单')
        # print(all_orders1)
        # with open(ORDERS_FILE, 'w', encoding='utf-8') as f:
        #     json.dump(all_orders1, f, ensure_ascii=False)
        MyFile.write_file(ORDERS_FILE, all_orders1)
        window.destroy()
        os.system('python my_orders.py')


def confirm_geted_goods():
    selects = tree.selection()
    if len(selects) != 1:
        messagebox.showinfo('提示', '请选择一个订单')
    else:
        data2 = tree.item(selects[0], 'values')
        # ##print('选择的订单')
        # ##print(data2)

        # my_json1 = ReadJson(ORDERS_FILE)
        all_orders = ReadJson(ORDERS_FILE).load_data()
        # print("=====所有的订单信息======")
        # print(all_orders)
        ###print("============")
        for j in all_orders:
            if j.get(SHOP_NAME, '') == data2[0] and j.get(GOODS_NAME, '') == data2[1] and j.get(
                    GOODS_PRICE, '') == data2[2] and j.get(BUY_COUNT, '-1') == data2[3] and j.get(
                    STATUS, '') == data2[4]:
                # print('找到要收货的订单了:{}'.format(j))
                if j.get(STATUS, '') in [YIXIADAN,ZANHUANFAHUO]:
                    messagebox.showinfo('提示信息', '商家还未发货喲')
                    return
                if j.get(STATUS, '') == YISHOUHUO:
                    messagebox.showinfo('提示信息', '不可以重复收货喲')
                    return
                # if j.get(STATUS, '') == ZANHUANFAHUO:
                #     messagebox.showinfo('提示信息', '不可以重复收货喲')
                #     return
                # delete_kucun(j)
                j[STATUS] = YISHOUHUO
                break
        # print('收货后的订单')
        # print(all_orders)
        MyFile.write_file(ORDERS_FILE, all_orders)
        # with open(ORDERS_FILE, 'w', encoding='utf-8') as f:
        #     json.dump(all_orders1, f, ensure_ascii=False)
        window.destroy()

        os.system('python my_orders.py')


def delete_kucun(j):
    # #print(j)
    pass
    # if j.get('status') != '已收货':
    #     shop_name = j.get('shop_name', '')
    #     #print('shop_name:{}'.format(shop_name))
    #     goods_name = j.get('goods_name', '')
    #     #print('goods_name :{}'.format(goods_name ))
    #     goods_price = j.get('goods_price', '')
    #     #print('goods_price:{}'.format(goods_price))
    #     buy_count = j.get('buy_count', '')
    #     #print('buy_count:{}'.format(buy_count))
    #
    #     data = ReadJson(SHOP_INFO).load_data()
    #     # ##print(data)
    #     for i in list(data.values()):
    #         # ##print(i)
    #         shop_name1 = i.get('shop_name', 'None')
    #         if shop_name1 == shop_name:
    #             # #print('找到了')
    #             # #print(i)
    #             shop_goods1 = i.get('shop_goods', {}).values()
    #             for j in shop_goods1:
    #                 if j.get('goods_name', 'None') == goods_name and j.get('goods_price',
    #                 'None') == goods_price:
    #                     #print(j)
    #                     #print(j['count'])
    #                     #print(buy_count)
    #                     j['count'] = str(int(j['count']) - int(buy_count))
    #                     # #print('修改完了')
    #                     # #print(j)
    #                     break
    #
    #             break
    #     # #print(data)
    #     with open(SHOP_INFO, 'w', encoding='utf-8') as f:
    #         json.dump(data, f, indent=4, ensure_ascii=False)


def btn1_event():
    ###print('返回')
    window.destroy()
    os.system('python choose.py')


if __name__ == '__main__':
    window = tkinter.Tk()
    frame = tkinter.Frame(window)
    select_label = tkinter.Label(window, text='个人订单', font=('', FONT_SIZE_24))
    field_names = ['店铺名称', '商品名称', '商品价格', '购买数量', '订单状态']
    tree = ttk.Treeview(frame, columns=field_names, show='headings')
    for field_name in field_names:
        tree.column(field_name, width=150)  # 对列进行定义
        tree.heading(field_name, text=field_name)

    my_json = ReadJson(ORDERS_FILE)
    data = my_json.load_data()
    all_orders = data

    my_json1 = ReadJson(CURRENT_USER_FILE)
    current_usr_info = my_json1.load_data()
    current_usr = current_usr_info.get(CUSTOMER_USER, '')
    ###print('当前登录用户名:{}'.format(current_usr))

    # all_goods = data.get(SHOP_GOODS, {})
    ###print("=====所有的订单信息======")
    ###print(all_orders)
    ###print("============")
    self_orders = []
    for i in all_orders:
        if i.get(CUSTOMER_USER) == current_usr:
            ###print('找到自己的一个订单:{}'.format(i))
            self_orders.append(i)
            pass
    ###print('自己的所有订单')
    ###print(self_orders)

    # field_data = list(self_orders.values())
    things = []
    for obj in self_orders:
        shop_name = obj.get(SHOP_NAME, '')
        goods_name = obj.get(GOODS_NAME, '')
        goods_price = obj.get(GOODS_PRICE, '')
        goods_count = obj.get(BUY_COUNT, '-1')
        status = obj.get(STATUS, '')
        things.append((shop_name, goods_name, goods_price, goods_count, status))
    insert_data(things)
    s = tkinter.Scrollbar(frame)  # 滚动条
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

    screenwidth = window.winfo_screenwidth()  # 屏幕宽度
    screenheight = window.winfo_screenheight()  # 屏幕高度
    width = 800
    height = 600
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    window.title(CUSTOMER_APP_TITLE)
    window.resizable(0, 0)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.mainloop()
