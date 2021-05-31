# -*- coding: utf-8 -*-
import os
import tkinter
from tkinter import *
from tkinter import messagebox

sys.path.append('../')
from COMMON.ReadJson import ReadJson
from COMMON.pub import *
from COMMON import MyFile


def return_btn_event():
    window.destroy()
    os.system('python myself.py')
    pass


def update_btn_event():
    current_obj = ReadJson(CURRENT_USER_FILE)
    current_user = current_obj.load_data()
    old_account = current_user.get(CUSTOMER_USER)

    new_name = name_entry.get()
    new_sex = sex_entry.get()
    new_account = account_entry.get()
    new_pwd = pwd_entry.get()
    my_json2 = ReadJson(USER_INFO_FILE)
    users = list(my_json2.load_data().values())

    old_users = []
    for i in users:
        old_users.append(i.get(CUSTOMER_USER, ''))

    old_users.pop(old_users.index(old_account))
    for i in users:
        if i.get(CUSTOMER_USER, '') == old_account:
            users.pop(users.index(i))

    if new_account in old_users:
        messagebox.showinfo('提示', '该账号已存在')
        return

    new_info = dict()
    new_info[NAME] = new_name
    new_info[SEX] = new_sex
    new_info[CUSTOMER_USER] = new_account
    new_info[PWD] = new_pwd
    new_info[USER_CONTACT] = contact_entry.get()
    new_info[USER_ADDRESS] = address_entry.get()

    MyFile.write_file(CURRENT_USER_FILE, new_info)
    new_user = dict()
    users.append(new_info)
    for index, one_user in enumerate(users):
        new_user[str(index + 1)] = one_user

    MyFile.write_file(USER_INFO_FILE, new_user)

    return_btn_event()
    pass


if __name__ == '__main__':

    window = tkinter.Tk()
    frame = tkinter.Frame(window)
    myself_label = Label(window, text='个人信息', font=('', FONT_SIZE_24))
    name_label = tkinter.Label(frame, text='姓名', font=('', FONT_SIZE_16))
    sex_label = tkinter.Label(frame, text='性别', font=('', FONT_SIZE_16))
    contact_label = tkinter.Label(frame, text='联系方式', font=('', FONT_SIZE_16), )
    address_label = tkinter.Label(frame, text='地址', font=('', FONT_SIZE_16), )
    account_label = tkinter.Label(frame, text='账号', font=('', FONT_SIZE_16))
    pwd_label = tkinter.Label(frame, text='密码', font=('', FONT_SIZE_16))
    my_json = ReadJson(CURRENT_USER_FILE)
    current_user_info = my_json.load_data()

    current_account = current_user_info.get(CUSTOMER_USER)
    current_name = current_user_info.get(NAME, '未设置姓名')
    current_sex = current_user_info.get(SEX, '未设置性别')
    current_pwd = current_user_info.get(PWD, '未设置密码')
    current_contact = current_user_info.get(USER_CONTACT, '未设置联系方式')
    current_address = current_user_info.get(USER_ADDRESS, '未设置地址')
    default_name = tkinter.StringVar()
    default_name.set(current_name)
    default_sex = tkinter.StringVar()
    default_sex.set(current_sex)
    default_account = tkinter.StringVar()
    default_account.set(current_account)
    default_pwd = tkinter.StringVar()
    default_pwd.set(current_pwd)
    default_contact = tkinter.StringVar()
    default_contact.set(current_contact)
    default_address = tkinter.StringVar()
    default_address.set(current_address)
    name_entry = tkinter.Entry(frame, textvariable=default_name, font=('', FONT_SIZE_16))
    sex_entry = tkinter.Entry(frame, text=default_sex, font=('', FONT_SIZE_16))
    account_entry = tkinter.Entry(frame, text=default_account, font=('', FONT_SIZE_16),
                                  state='disable')
    pwd_entry = tkinter.Entry(frame, text=default_pwd, font=('', FONT_SIZE_16))
    contact_entry = tkinter.Entry(frame, text=default_contact, font=('', FONT_SIZE_16))
    address_entry = tkinter.Entry(frame, text=default_address, font=('', FONT_SIZE_16))
    return_btn = tkinter.Button(frame, text='返回', command=return_btn_event, font=('', FONT_SIZE_16))
    update_btn = tkinter.Button(frame, text='修改', command=update_btn_event, font=('', FONT_SIZE_16))

    myself_label.pack(side=tkinter.TOP, padx=10, pady=40)
    frame.pack()
    padx = 20
    pady = 20
    name_label.grid(row=0, column=0, padx=padx, pady=pady)
    sex_label.grid(row=1, column=0, padx=padx, pady=pady)
    account_label.grid(row=2, column=0, padx=padx, pady=pady)
    pwd_label.grid(row=3, column=0, padx=padx, pady=pady)
    contact_label.grid(row=4, column=0, padx=padx, pady=pady)
    address_label.grid(row=5, column=0, padx=padx, pady=pady)
    name_entry.grid(row=0, column=1, padx=padx, pady=pady)
    sex_entry.grid(row=1, column=1, padx=padx, pady=pady)
    account_entry.grid(row=2, column=1, padx=padx, pady=pady, )
    pwd_entry.grid(row=3, column=1, padx=padx, pady=pady)
    contact_entry.grid(row=4, column=1, padx=padx, pady=pady)
    address_entry.grid(row=5, column=1, padx=padx, pady=pady)
    update_btn.grid(row=6, column=0, padx=padx, pady=pady)
    return_btn.grid(row=6, column=1, padx=padx, pady=pady)

    window.title(CUSTOMER_APP_TITLE)

    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    width = 700
    height = 700
    x = int((screenwidth - width) / 2)
    y = int((screenheight - height) / 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    window.mainloop()
