# -*- encoding=utf-8 -*-
import tkinter

import PublicMethod
from login import LoginFrame

if __name__ == '__main__':
    main_win = tkinter.Tk()
    login_window = LoginFrame(main_win)
    PublicMethod.set_title(login_window.window, '登录')
    PublicMethod.set_size_center(login_window.window, 300, 350)
    login_window.set_frame()
    main_win.mainloop()
