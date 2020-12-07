# -*- coding: utf-8 -*-
import json
import os
import tkinter
from tkinter import messagebox
from tkinter import ttk

from COMMON.ReadJson import ReadJson
from COMMON.pub import COUNT
from COMMON.pub import FONT_SIZE_16
from COMMON.pub import FONT_SIZE_24
from COMMON.pub import GOODS_NAME
from COMMON.pub import GOODS_PRICE
from COMMON.pub import PHONE
from COMMON.pub import SEE_SHOP
from COMMON.pub import SHOP_ADDRESS
from COMMON.pub import SHOP_GOODS
from COMMON.pub import SHOP_INFO
from COMMON.pub import SHOP_NAME
from COMMON.pub import SHOP_OWNER
from COMMON.pub import SHOP_USER


def insert_data(data_list):
    for one_data in data_list:  # 插入数据
        tree.insert('', tkinter.END, value=one_data)


def into_shop():
    selects = tree.selection()
    if len(selects) != 1:
        messagebox.showwarning('提示', '请选择店铺')
    else:
        select_shop = tree.item(selects[0], 'values')
        print('选中的店铺')
        print(select_shop)
        obj2 = ReadJson(SHOP_INFO)
        info = obj2.load_data()
        print('总商店信息')
        print(info)
        shops1 = list(info.values())
        for i in shops1:
            if i.get(SHOP_NAME, '') == select_shop[0]:
                select_shop_user = i.get(SHOP_USER, '')
                print('选中的店铺的用户名:{}'.format(select_shop_user))
                print('选中的店铺信息:{}'.format(i))
                with open(SEE_SHOP, 'w', encoding='UTF-8') as f:
                    json.dump(i, f, ensure_ascii=False)
                break
        window.destroy()
        os.system('python goods.py')


def btn1_event():
    print('返回')
    window.destroy()
    os.system('python choose.py')


if __name__ == '__main__':
    window = tkinter.Tk()
    frame = tkinter.Frame(window)
    select_label = tkinter.Label(window, text='查看店铺', font=('', FONT_SIZE_24))
    field_names = ['店铺名称', '店铺地址', '店主', '联系方式']
    tree = ttk.Treeview(frame, columns=field_names, show='headings', height=20)
    for field_name in field_names:
        tree.column(field_name, width=250)  # 对列进行定义
        tree.heading(field_name, text=field_name)

    my_json = ReadJson(SHOP_INFO)
    data = my_json.load_data()
    shops = list(data.values())
    print('================现有的所有店铺===============')
    print(shops)
    shops_list = []
    for shop in shops:
        shop_list = list()
        shop_list.append(shop.get(SHOP_NAME, ''))
        shop_list.append(shop.get(SHOP_ADDRESS, ''))
        shop_list.append(shop.get(SHOP_OWNER, ''))
        shop_list.append(shop.get(PHONE, ''))
        tree.insert('', tkinter.END, value=shop_list)

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
    update_btn = tkinter.Button(frame2, text='进店', command=into_shop, font=('', FONT_SIZE_16), )
    btn1 = tkinter.Button(frame2, text='返回', command=btn1_event, font=('', FONT_SIZE_16), )

    s.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    tree.pack()
    select_label.pack(side=tkinter.TOP, padx=30, pady=60)
    frame.pack()
    padx = 200
    pady = 60
    update_btn.grid(row=0, column=1, padx=padx, pady=pady)
    btn1.grid(row=0, column=4, padx=padx, pady=pady)
    frame2.pack()

    screenwidth = window.winfo_screenwidth()  # 屏幕宽度
    screenheight = window.winfo_screenheight()  # 屏幕高度
    width = 1200
    height = 800
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.mainloop()
