import current_login_user
import mysqltool
import mytool


def set_size_center(window, width, height):  # 设置窗口居中
    screenwidth = window.winfo_screenwidth()  # 屏幕宽度
    screenheight = window.winfo_screenheight()  # 屏幕高度
    x = int((screenwidth - width) / 2)  # 横坐标
    y = int((screenheight - height) / 2)  # 纵坐标
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # 布局窗口
    window.resizable(0, 0)  # 不可最大化
    window.update()  # 更新窗口


def clear_child(window):  # 清除父窗口所有的组件
    for child in window.children.values():  # 获取所有孩子
        try:
            child.pack_forget()  # 取消pack放置的组件
        except:
            pass
        try:
            child.grid_forget()  # 取消grid放置的组件
        except:
            pass
        try:
            child.place_forget()  # 取消place放置的组件
        except:
            pass


def set_exit_date():  # 设置退出时间

    account = current_login_user.CURRENT_LOGIN_ACCOUNT  # 读取当前登录的用户,每次退出时,设置退出时间
    print(f'current login user:{account}')
    if account:
        update_data = dict(exitdate=mytool.now('%Y-%m-%d %H:%M:%S'))
        update_conditions = dict(account=account)
        # 更新用户表的最新退出时间
        mysqltool.update(mysqltool.conn_db, 'useraccount', update_data, update_conditions)

        select_conditions = dict(account=account)
        # 查询用户登录历史记录表
        db_data, msg = mysqltool.select(mysqltool.conn_db, 'userhistory', ['id', 'exitdate'],
                                        select_conditions)
        update_id = None
        for one in db_data:
            if one.get('exitdate') is None:
                update_id = one.get('id')  # 获取退出时间是NULL的用户ID
                break
        if update_id:
            update_history_conditions = dict(id=update_id)
            # 修改用户登录历史记录表的最新退出时间
            mysqltool.update(mysqltool.conn_db, 'userhistory', update_data,
                             update_history_conditions)
        current_login_user.CURRENT_LOGIN_ACCOUNT = None  # 退出后设置当前登录的用户为None


def on_closing(win):  # 关闭窗口
    set_exit_date()  # 设置退出时间
    win.destroy()  # 销毁窗口
    mysqltool.disconnect(mysqltool.conn_db)  # 关闭连接
