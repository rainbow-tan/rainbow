# -*- coding: utf-8 -*-
import os
import sys
import tkinter
from tkinter import messagebox
from tkinter import ttk

sys.path.append('../')
from COMMON import MyFile
from COMMON.pub import SHOP_USER
from COMMON.pub import YIFAHUO
from COMMON.pub import YIXIADAN
from COMMON.pub import ZANHUANFAHUO

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
    for one_data in data_list:  # 插入数据
        tree.insert('', tkinter.END, value=one_data)


def buy_goods():
    selects = tree.selection()
    if len(selects) != 1:
        messagebox.showinfo('提示', '请选择一个订单')
    else:
        data2 = tree.item(selects[0], 'values')
        ##print('选择的订单')
        ##print(data2)
        status_order = data2[7]

        if status_order == '已下单':
            # my_json1 = ReadJson(ORDERS_FILE)
            all_orders1 = ReadJson(ORDERS_FILE).load_data()
            ##print("=====所有的订单信息======")
            ##print(all_orders1)
            for one in all_orders1:
                customer_user = one.get(CUSTOMER_USER)
                # shop_ust = one.get(SHOP_USER)
                status = one.get(STATUS)
                goods_name = one.get(GOODS_NAME)
                goods_price = one.get(GOODS_PRICE)
                if customer_user == data2[0] and goods_name == data2[4] and goods_price == data2[
                    5] and status == data2[7]:
                    ##print('找到要暂缓发货的订单了')
                    one[STATUS] = ZANHUANFAHUO
                    break
            ##print('设置暂缓发货后:{}'.format(all_orders1))
            MyFile.write_file(ORDERS_FILE, all_orders1)
            # ###print("============")
            # for i, j in all_orders1.items():
            #     ##print(j)
            #     if j.get(CUSTOMER_USER, '') == data2[0] and j.get(GOODS_NAME, '') == data2[2]
            #     and j.get(
            #             GOODS_PRICE, '') == data2[3] and j.get(BUY_COUNT, '-1') == data2[4] and
            #             j.get(
            #             STATUS, '') == data2[5]:
            #         ##print('找到要收货的订单了:{}'.format(i))
            #         all_orders1[i][STATUS] = '库存不足，暂缓发货'
            #         break
            # ###print('发货后的订单')
            # ###print(all_orders1)
            #     with open(ORDERS_FILE, 'w', encoding='utf-8') as f:
            #         json.dump(all_orders1, f,indent=4, ensure_ascii=False)
            window.destroy()
            os.system('python my_orders.py')


def send_goods():
    selects = tree.selection()
    if len(selects) != 1:
        messagebox.showinfo('提示', '请选择一个订单')
    else:
        data2 = tree.item(selects[0], 'values')

        status_order = data2[7]
        if status_order==YIFAHUO:
            messagebox.showinfo('提示信息', '不可以重复发货')
            return
        if status_order == YIXIADAN or status_order == ZANHUANFAHUO:
            # my_json1 = ReadJson(ORDERS_FILE)
            all_orders1 = ReadJson(ORDERS_FILE).load_data()
            # #print("=====所有的订单信息======")
            # #print(all_orders1)
            for one in all_orders1:
                customer_user = one.get(CUSTOMER_USER)
                shop_usr = one.get(SHOP_USER)
                status = one.get(STATUS)
                goods_name = one.get(GOODS_NAME)
                goods_price = one.get(GOODS_PRICE)
                if customer_user == data2[0] and goods_name == data2[4] and goods_price == data2[
                    5] and status == data2[7]:
                    # print('找到要发货的订单了:{}'.format(one))

                    shopinfo = ReadJson(SHOP_INFO_FILE).load_data()
                    # print(shopinfo)
                    for one1 in shopinfo.values():
                        if one1.get(SHOP_USER) == shop_usr:
                            # print('找到店铺了:{}'.format(one1))
                            # print(one1.get(SHOP_GOODS,{}))
                            for good in one1.get(SHOP_GOODS, {}).values():
                                # print('goods:{}|'.format(good))
                                # for good in goods:
                                if good.get(GOODS_NAME) == goods_name and good.get(
                                        GOODS_PRICE) == goods_price:
                                    # print('找到商品了:{}'.format(good))
                                    good_all_count = good.get(COUNT)
                                    # print('还剩余的数量:{}'.format(good_all_count))
                                    if int(good_all_count) - int(data2[6]) < 0:
                                        messagebox.showinfo('提示信息',
                                                            '库存不足发货，发货需要{}，你现在有{}'.format(data2[6],
                                                                                          good_all_count))
                                        return
                                    else:
                                        good[COUNT] = str(int(good_all_count) - int(data2[6]))
                                        # print(shopinfo)
                                        # print(one1)
                                        MyFile.write_file(SHOP_INFO_FILE, shopinfo)
                                        MyFile.write_file(CURRENT_SHOP_FILE, one1)
                                        break
                    one[STATUS] = YIFAHUO

                    # print(all_orders1)
                    MyFile.write_file(ORDERS_FILE, all_orders1)
                    window.destroy()
                    os.system('python my_orders.py')
                    break
            ##print('设置暂缓发货后:{}'.format(all_orders1))
            # MyFile.write_file(ORDERS_FILE,all_orders1)
            # ###print("============")
            # for i, j in all_orders1.items():
            #     ##print(j)
            #     if j.get(CUSTOMER_USER, '') == data2[0] and j.get(GOODS_NAME, '') == data2[2]
            #     and j.get(
            #             GOODS_PRICE, '') == data2[3] and j.get(BUY_COUNT, '-1') == data2[4] and
            #             j.get(
            #             STATUS, '') == data2[5]:
            #         ##print('找到要收货的订单了:{}'.format(i))
            #         all_orders1[i][STATUS] = '库存不足，暂缓发货'
            #         break
            # ###print('发货后的订单')
            # ###print(all_orders1)
            #     with open(ORDERS_FILE, 'w', encoding='utf-8') as f:
            #         json.dump(all_orders1, f,indent=4, ensure_ascii=False)
            # window.destroy()
            # os.system('python my_orders.py')

        ##print('选择的订单')
        ##print(data2)
        # name=data2[4]
        # ###print(data2[7])

        # if data2[7] != '已发货':
        #
        #     my_json1 = ReadJson(ORDERS_FILE)
        #     all_orders1 = my_json1.load_data()
        #     # ###print("=====所有的订单信息======")
        #     # ###print(all_orders1)
        #     # ###print("============")
        #     for i, j in all_orders1.items():
        #         if j.get(CUSTOMER_USER, '') == data2[0] and j.get(GOODS_NAME, '') == data2[4]
        #         and j.get(
        #                 GOODS_PRICE, '') == data2[5] and j.get(BUY_COUNT, '-1') == data2[
        #             6] and j.get(
        #                 STATUS, '') == data2[7]:
        #             # ###print('找到要收货的订单了:{}'.format(i))
        #             all_orders1[i][STATUS] = '已发货'
        #
        #             my_json2 = ReadJson(CURRENT_SHOP_FILE)
        #             my_shop_info = my_json2.load_data()
        #             # ###print('我的商店信息:{}'.format(my_shop_info))
        #             my_goods = list(my_shop_info.get(SHOP_GOODS, {}).values())
        #             # ###print('我的商品信息:{}'.format(my_goods))
        #             for i, my_good in enumerate(my_goods):
        #                 if my_good.get(GOODS_NAME, '') == data2[4]:
        #                     my_good[COUNT] = int(my_good.get(COUNT, '-1')) - int(data2[6])
        #                     # ###print(my_good)
        #                     break
        #             # ###print('我发货后的商品信息:{}'.format(my_goods))
        #             with open(CURRENT_SHOP_FILE, 'w', encoding='utf-8') as f:
        #                 json.dump(my_shop_info, f, indent=4, ensure_ascii=False)
        #             # ###print('更新当前:L{}'.format(my_shop_info))
        #             # ###print('@@@@@@@@@@@')
        #
        #             my_json3 = ReadJson(SHOP_INFO_FILE)
        #             all_shop_info = my_json3.load_data()
        #             # ###print('所有的店铺信息：{}'.format(all_shop_info))
        #             for i, j in all_shop_info.items():
        #                 if j.get(SHOP_NAME) == current_usr:
        #                     all_shop_info[i] = my_shop_info
        #                     ###print('所有店铺信息更新:{}'.format(all_shop_info))
        #                     with open(SHOP_INFO_FILE, 'w', encoding='utf-8') as f:
        #                         json.dump(all_shop_info, f,indent=4, ensure_ascii=False)
        #                     break
        #
        #             break
        #
        #     # ###print('发货后的订单')
        #     # ###print(all_orders1)
        #     with open(ORDERS_FILE, 'w', encoding='utf-8') as f:
        #         json.dump(all_orders1, f,indent=4, ensure_ascii=False)
        #
        # window.destroy()
        # os.system('python my_orders.py')


def btn1_event():
    # ###print('返回')
    window.destroy()
    os.system('python choose.py')


if __name__ == '__main__':
    window = tkinter.Tk()
    frame = tkinter.Frame(window)
    select_label = tkinter.Label(window, text='店铺订单', font=('', FONT_SIZE_24))
    field_names = ['用户账号', '用户姓名', '联系方式', '用户地址', '商品名称', '商品价格', '购买数量', '订单状态']
    tree = ttk.Treeview(frame, columns=field_names, show='headings')
    for field_name in field_names:
        tree.column(field_name, width=150)  # 对列进行定义
        tree.heading(field_name, text=field_name)

    my_json = ReadJson(ORDERS_FILE)
    # data = my_json.load_data()
    all_orders = my_json.load_data()

    my_json1 = ReadJson(CURRENT_SHOP_FILE)
    current_usr_info = my_json1.load_data()
    current_usr = current_usr_info.get(SHOP_USER, '')
    # print('当前登录店铺用户名:{}'.format(current_usr))

    # all_goods = data.get(SHOP_GOODS, {})
    # ###print("=====所有的订单信息======")
    # ###print(all_orders)
    # ###print("============")
    self_orders = []
    for i in all_orders:
        if i.get(SHOP_USER) == current_usr:
            # print('找到自己的一个订单:{}'.format(i))
            self_orders.append(i)
            pass
    # ###print('自己的所有订单')
    # ###print(self_orders)

    things = []
    for obj in self_orders:
        usr = obj.get(CUSTOMER_USER, '')
        # ###print('下单的用户:{}'.format(usr))
        my_json1 = ReadJson(USER_INFO_FILE)
        all_users = my_json1.load_data().values()
        name = ''
        for i in all_users:
            if i.get(CUSTOMER_USER, '') == usr:
                name = i.get(NAME, '')
                user_contact = i.get(USER_CONTACT, '')
                user_address = i.get(USER_ADDRESS, '')
                # ###print('找到下单的姓名:{}'.format(name))
                break
        goods_name = obj.get(GOODS_NAME, '')
        goods_price = obj.get(GOODS_PRICE, '')
        goods_count = obj.get(BUY_COUNT, '-1')
        status = obj.get(STATUS, '')
        things.append((usr, name, user_contact, user_address, goods_name, goods_price, goods_count,
                       status))
    insert_data(things)
    s = tkinter.Scrollbar(frame)  # 滚动条
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

    screenwidth = window.winfo_screenwidth()  # 屏幕宽度
    screenheight = window.winfo_screenheight()  # 屏幕高度
    width = 1200
    height = 600
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    window.title(SHOP_APP_TITLE)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.mainloop()
