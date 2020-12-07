# -*- coding: utf-8 -*-
import json
import os
import sys
import tkinter
from tkinter import messagebox

from COMMON.ReadJson import ReadJson
from COMMON.pub import BUY_COUNT
from COMMON.pub import COUNT
from COMMON.pub import CURRENT_USER
from COMMON.pub import GOODS_NAME
from COMMON.pub import GOODS_PRICE
from COMMON.pub import ORDERS
from COMMON.pub import SEE_SHOP
from COMMON.pub import SHOP_GOODS
from COMMON.pub import SHOP_NAME
from COMMON.pub import STATUS
from COMMON.pub import USER


def alert_buy():
    try:
        value = str(int(user_entry1.get().strip()))
        print('购买数量:{}'.format(value))

        my_json = ReadJson(ORDERS)
        old_orders_dict = my_json.load_data()
        print('旧订单字典')
        print(old_orders_dict)
        old_orders_list = list(old_orders_dict.values())
        print('旧订单列表')
        print(old_orders_list)

        my_json1 = ReadJson(CURRENT_USER)
        current_usr_info = my_json1.load_data()
        current_usr = current_usr_info.get(USER, '')
        print('当前登录用户名:{}'.format(current_usr))

        my_json1 = ReadJson(SEE_SHOP)
        current_shop_info = my_json1.load_data()
        current_shop_usr = current_shop_info.get(SHOP_NAME, '')
        print('当前查看的店铺:{}'.format(current_shop_usr))

        current_buy_goods_name = sys.argv[1]
        current_buy_goods_price = sys.argv[2]
        print('当前要买的商品:{}'.format(current_buy_goods_name))
        print('当前要买的商品价格:{}'.format(current_buy_goods_price))
        print('当前要买的数量:{}'.format(value))

        shop_goods = list(current_shop_info.get(SHOP_GOODS, {}).values())
        print('商家的商品')
        print(shop_goods)

        for shop_good in shop_goods:
            if shop_good.get(GOODS_NAME, '') == current_buy_goods_name:
                goods_count = shop_good.get(COUNT, '-1')
                print('商品库存:{}'.format(goods_count))
                if int(goods_count) - int(value) < 0:
                    msg = '库存不够，请少买点'
                    messagebox.showinfo('提示信息', msg)
                    return None
                break

        current_order = dict()
        current_order[USER] = current_usr
        current_order[SHOP_NAME] = current_shop_usr
        current_order[STATUS] = '已下单'
        current_order[GOODS_NAME] = current_buy_goods_name
        current_order[GOODS_PRICE] = current_buy_goods_price
        current_order[BUY_COUNT] = value
        print('新增的订单')
        print(current_order)

        old_orders_list.append(current_order)
        print('新增后总订单列表')
        print(old_orders_list)

        new_orders_dict = {}
        for i, j in enumerate(old_orders_list):
            new_orders_dict[str(i + 1)] = j
        print('新增后总订单字典')
        print(new_orders_dict)

        with open(ORDERS, 'w', encoding='utf-8') as f:
            json.dump(new_orders_dict, f, ensure_ascii=False)
        msg = '生成订单成功'
        messagebox.showinfo('提示信息', msg)
        root.destroy()
        os.system('python goods.py')
    except Exception as e:
        print(e)
        messagebox.showinfo('提示信息', '请输入购买数量（整数）')
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

    root.title('购物系统')

    screenwidth1 = root.winfo_screenwidth()  # 屏幕宽度
    screenheight2 = root.winfo_screenheight()  # 屏幕高度
    width1 = 300
    height1 = 200
    x1 = int((screenwidth1 - width1) / 2)
    y1 = int((screenheight2 - height1) / 2)
    root.geometry('{}x{}+{}+{}'.format(width1, height1, x1, y1))
    root.mainloop()
