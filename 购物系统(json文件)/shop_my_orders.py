# -*- coding: utf-8 -*-
import json
import os
import tkinter
from tkinter import messagebox
from tkinter import ttk

from ReadJson import ReadJson
from pub import BUY_COUNT
from pub import COUNT
from pub import CURRENT_SHOP
from pub import FONT_SIZE_16
from pub import FONT_SIZE_24
from pub import GOODS_NAME
from pub import GOODS_PRICE
from pub import NAME
from pub import ORDERS
from pub import SHOP_GOODS
from pub import SHOP_INFO
from pub import SHOP_NAME
from pub import STATUS
from pub import USER
from pub import USER_ADDRESS
from pub import USER_CONTACT
from pub import USER_INFO


def insert_data(data_list):
    for one_data in data_list:  # 插入数据
        tree.insert('', tkinter.END, value=one_data)



def buy_goods():
    selects = tree.selection()
    if len(selects) != 1:
        messagebox.showinfo('提示', '请选择一个订单')
    else:
        data2 = tree.item(selects[0], 'values')
        print('选择的订单')
        print(data2)

        my_json1 = ReadJson(ORDERS)
        all_orders1 = my_json1.load_data()
        print("=====所有的订单信息======")
        print(all_orders1)
        print("============")
        for i, j in all_orders1.items():
            if j.get(USER, '') == data2[0] and j.get(GOODS_NAME, '') == data2[2] and j.get(
                    GOODS_PRICE, '') == data2[3] and j.get(BUY_COUNT, '-1') == data2[4] and j.get(
                    STATUS, '') == data2[5]:
                print('找到要收货的订单了:{}'.format(i))
                all_orders1[i][STATUS] = '库存不足，暂缓发货'
                break
        print('发货后的订单')
        print(all_orders1)
        with open(ORDERS, 'w', encoding='utf-8') as f:
            json.dump(all_orders1, f, ensure_ascii=False)
        window.destroy()
        os.system('python shop_my_orders.py')


def buy_goods1():
    selects = tree.selection()
    if len(selects) != 1:
        messagebox.showinfo('提示', '请选择一个订单')
    else:
        data2 = tree.item(selects[0], 'values')
        print('选择的订单')
        print(data2)

        my_json1 = ReadJson(ORDERS)
        all_orders1 = my_json1.load_data()
        print("=====所有的订单信息======")
        print(all_orders1)
        print("============")
        for i, j in all_orders1.items():
            if j.get(USER, '') == data2[0] and j.get(GOODS_NAME, '') == data2[4] and j.get(
                    GOODS_PRICE, '') == data2[5] and j.get(BUY_COUNT, '-1') == data2[6] and j.get(
                    STATUS, '') == data2[7]:
                print('找到要收货的订单了:{}'.format(i))
                all_orders1[i][STATUS] = '已发货'

                my_json2 = ReadJson(CURRENT_SHOP)
                my_shop_info = my_json2.load_data()
                print('我的商店信息:{}'.format(my_shop_info))
                my_goods = list(my_shop_info.get(SHOP_GOODS,{}).values())
                print('我的商品信息:{}'.format(my_goods))
                for i,my_good in enumerate(my_goods):
                    if my_good.get(GOODS_NAME,'')==data2[4]:
                        my_good[COUNT] = int(my_good.get(COUNT,'-1'))-int(data2[6])
                        print(my_good)
                        break
                print('我发货后的商品信息:{}'.format(my_goods))
                with open(CURRENT_SHOP, 'w', encoding='utf-8') as f:
                    json.dump(my_shop_info, f, ensure_ascii=False)
                my_json3 = ReadJson(SHOP_INFO)
                all_shop_info = my_json3.load_data()
                print('所有的店铺信息：{}'.format(all_shop_info))
                for i ,j in all_shop_info.items():
                    if j.get(SHOP_NAME)==current_usr:
                        all_shop_info[i]=my_shop_info
                        print('所有店铺信息更新:{}'.format(all_shop_info))
                        with open(SHOP_INFO, 'w', encoding='utf-8') as f:
                            json.dump(all_shop_info, f, ensure_ascii=False)
                        break


                break

        print('发货后的订单')
        print(all_orders1)
        with open(ORDERS, 'w', encoding='utf-8') as f:
            json.dump(all_orders1, f, ensure_ascii=False)




        window.destroy()
        os.system('python shop_my_orders.py')


def btn1_event():
    print('返回')
    window.destroy()
    os.system('python shop_choose.py')


if __name__ == '__main__':
    window = tkinter.Tk()
    frame = tkinter.Frame(window)
    select_label = tkinter.Label(window, text='店铺订单', font=('', FONT_SIZE_24))
    field_names = ['用户账号', '用户名称','用户地址','联系方式', '商品名称', '商品数量', '购买数量', '订单状态']
    tree = ttk.Treeview(frame, columns=field_names, show='headings')
    for field_name in field_names:
        tree.column(field_name, width=150)  # 对列进行定义
        tree.heading(field_name, text=field_name)

    my_json = ReadJson(ORDERS)
    data = my_json.load_data()
    all_orders = data.values()

    my_json1 = ReadJson(CURRENT_SHOP)
    current_usr_info = my_json1.load_data()
    current_usr = current_usr_info.get(SHOP_NAME, '')
    print('当前登录店铺用户名:{}'.format(current_usr))

    # all_goods = data.get(SHOP_GOODS, {})
    print("=====所有的订单信息======")
    print(all_orders)
    print("============")
    self_orders = []
    for i in all_orders:
        if i.get(SHOP_NAME) == current_usr:
            print('找到自己的一个订单:{}'.format(i))
            self_orders.append(i)
            pass
    print('自己的所有订单')
    print(self_orders)

    things = []
    for obj in self_orders:
        usr = obj.get(USER, '')
        print('下单的用户:{}'.format(usr))
        my_json1 = ReadJson(USER_INFO)
        all_users = my_json1.load_data().values()
        name=''
        for i in all_users:
            if i.get(USER, '') == usr:
                name = i.get(NAME, '')
                user_contact = i.get(USER_CONTACT, '')
                user_address = i.get(USER_ADDRESS, '')
                print('找到下单的姓名:{}'.format(name))
                break
        goods_name = obj.get(GOODS_NAME, '')
        goods_price = obj.get(GOODS_PRICE, '')
        goods_count = obj.get(BUY_COUNT, '-1')
        status = obj.get(STATUS, '')
        things.append((usr, name,user_contact,user_address, goods_name, goods_price, goods_count, status))
    insert_data(things)
    s = tkinter.Scrollbar(frame)  # 滚动条
    s.config(command=tree.yview)
    tree.config(yscrollcommand=s.set)
    frame2 = tkinter.Frame(window)
    update_btn = tkinter.Button(frame2, text='暂缓发货', command=buy_goods, font=('', FONT_SIZE_16), )
    update_btn2 = tkinter.Button(frame2, text='确认发货', command=buy_goods1, font=('', FONT_SIZE_16), )
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
    width = 1200
    height = 600
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.mainloop()
