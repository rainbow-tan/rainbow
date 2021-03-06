# -*- coding: utf-8 -*-
import json
import os
import tkinter
from tkinter import messagebox
from tkinter import ttk

from ReadJson import ReadJson
from pub import COUNT
from pub import CURRENT_SHOP
from pub import FONT_SIZE_16
from pub import FONT_SIZE_24
from pub import GOODS_NAME
from pub import GOODS_PRICE
from pub import SHOP_GOODS
from pub import SHOP_INFO
from pub import SHOP_USER


def insert_data(data_list):
    for one_data in data_list:  # 插入数据
        tree.insert('', tkinter.END, value=one_data)


def clear_item():
    # 获取item并移除
    choose = messagebox.askyesno('提示', '确认删除已选择记录吗？')
    if choose:

        obj1 = ReadJson(CURRENT_SHOP)
        current_data = obj1.load_data()
        print("当前用户信息")
        print(current_data)
        current_user = current_data.get(SHOP_USER, '')
        print('当前用户:{}'.format(current_user))
        obj2 = ReadJson(SHOP_INFO)
        info = obj2.load_data()
        print('总商店信息')
        print(info)
        for i, j in info.items():
            usr = j.get(SHOP_USER, '')
            if current_user == usr:
                print('找到当前用户')
                print(j)
                j[SHOP_GOODS] = dict()
        print('删除所有商品后')
        current_data[SHOP_GOODS] = dict()
        print(current_data)
        print('===============')
        print(info)
        with open(CURRENT_SHOP, 'w', encoding='utf-8') as f:
            json.dump(current_data, f, ensure_ascii=False)
        with open(SHOP_INFO, 'w', encoding='utf-8') as f:
            json.dump(info, f, ensure_ascii=False)
        for child in tree.get_children():
            tree.delete(child)
        window.destroy()
        os.system('python shop_goods.py')
    pass


def add():
    print('添加')
    window.destroy()
    os.system('python shop_add_goods.py')
    pass


def update():
    selects = tree.selection()
    if len(selects) != 1:
        messagebox.showwarning('提示', '选择一条记录进行修改')
    else:
        data1 = tree.item(selects[0], 'values')
        print(data1)
        window.destroy()
        os.system('python shop_update_goods.py {} {} {}'.format(data1[0], data1[1], data1[2]))


def delete():
    selects = tree.selection()
    if len(selects) > 0:
        all_data = []
        for select in selects:
            all_data.append(tree.item(select, 'values'))  # 获取item的值
        choose = messagebox.askyesno('提示', '确认删除已选择记录吗？')
        print(choose)
        print('选中要删除的的数据')
        print(all_data)
        if choose:
            for data1 in all_data:
                print(data1)
                obj1 = ReadJson(CURRENT_SHOP)
                current_data = obj1.load_data()
                print("当前用户信息")
                print(current_data)
                current_user = current_data.get(SHOP_USER, '')
                print('当前用户:{}'.format(current_user))
                current_goods = current_data.get(SHOP_GOODS, {})
                for i, j in current_goods.items():
                    if data1[0] == j.get(GOODS_NAME):
                        print('对应删除商品的key')
                        print(i)
                        print(j)
                        current_data[SHOP_GOODS].pop(i)
                        break
                print('删除单个商品后，店铺信息')
                print(current_data)
                with open(CURRENT_SHOP, 'w', encoding='utf-8') as f:
                    json.dump(current_data, f, ensure_ascii=False)

                obj2 = ReadJson(SHOP_INFO)
                info = obj2.load_data()
                print('总商店信息')
                print(info)
                remove_key = None
                for i, j in info.items():
                    usr = j.get(SHOP_USER, '')
                    if current_user == usr:
                        print('找到当前用户key')
                        print(i)
                        remove_key = i
                        break
                info.pop(remove_key)
                new = []
                for i in info:
                    new.append(i)
                new.append(current_data)
                new_data = dict()
                for i, j in enumerate(new):
                    new_data[str(i + 1)] = j
                print('新的总店铺信息')
                print(new_data)
                with open(SHOP_INFO, 'w', encoding='utf-8') as f:
                    json.dump(new_data, f, ensure_ascii=False)
            window.destroy()
            os.system('python shop_goods.py')
    else:
        messagebox.showwarning('提示', '至少选择一条记录进行删除')


def btn1_event():
    print('返回')
    window.destroy()
    os.system('python shop_choose.py')


if __name__ == '__main__':
    window = tkinter.Tk()
    frame = tkinter.Frame(window)
    select_label = tkinter.Label(window, text='查看信息', font=('', FONT_SIZE_24))
    field_names = ['商品名称', '商品价格', '商品数量']
    tree = ttk.Treeview(frame, columns=field_names, show='headings')
    for field_name in field_names:
        tree.column(field_name, width=100)  # 对列进行定义
        tree.heading(field_name, text=field_name)

    my_json = ReadJson(CURRENT_SHOP)
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
    add_btn = tkinter.Button(frame2, text='添加', command=add, font=('', FONT_SIZE_16), )
    update_btn = tkinter.Button(frame2, text='修改', command=update, font=('', FONT_SIZE_16), )
    clear_item_btn = tkinter.Button(frame2, text='清仓', command=clear_item,
                                    font=('', FONT_SIZE_16), )
    delete_btn = tkinter.Button(frame2, text='删除', command=delete, font=('', FONT_SIZE_16), )
    btn1 = tkinter.Button(frame2, text='返回', command=btn1_event, font=('', FONT_SIZE_16), )

    s.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    tree.pack()
    select_label.pack(side=tkinter.TOP, padx=30, pady=60)
    frame.pack()
    padx = 20
    pady = 60
    add_btn.grid(row=0, column=0, padx=padx, pady=pady)
    update_btn.grid(row=0, column=1, padx=padx, pady=pady)
    delete_btn.grid(row=0, column=2, padx=padx, pady=pady)
    clear_item_btn.grid(row=0, column=3, padx=padx, pady=pady)
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
