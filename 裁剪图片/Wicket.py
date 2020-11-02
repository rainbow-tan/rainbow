# -*- encoding=utf-8 -*-
import tkinter


class Wicket:
    def __init__(self):
        self.win = None

    def create_window(self):
        if self.win is None:
            tk = tkinter.Tk()
            self.win = tk
        else:
            print('已经存在窗口,无需再次创建')

    def set_window_title(self, title):
        if self.win is not None:
            self.win.title(title)
        else:
            print('请先创建窗口')

    def show_window(self):
        if self.win is not None:
            self.win.mainloop()
        else:
            print('请先创建窗口')

    def set_window_size(self, size):
        """
        :param size: '500x500+0+0'
        :return: None
        """
        if self.win is not None:
            screenwidth, screenheight = self.get_screen()
            if size.lower() == 'max':
                self.win.geometry('{}x{}+0+0'.format(screenwidth, screenheight))
            else:
                try:
                    self.win.geometry(size)
                except Exception as e:
                    print('尺寸设置有误:{}'.format(e))
                    multiple = 3 / 4
                    win_width = int(multiple * screenwidth)
                    win_height = int(multiple * screenheight)
                    x = int((screenwidth - win_width) / 2)
                    y = int((screenheight - win_height) / 2)
                    self.win.geometry('{}x{}+{}+{}'.format(win_width, win_height, x, y))
        else:
            print('请先创建窗口')

    @staticmethod
    def get_screen():
        screen_tk = tkinter.Tk()
        screenwidth = screen_tk.winfo_screenwidth()
        screenheight = screen_tk.winfo_screenheight()
        screen_tk.destroy()
        return screenwidth, screenheight

    def get_size(self):
        self.win.update()  # 获取size之前需要先刷新
        window_width = self.win.winfo_width()
        window_height = self.win.winfo_height()
        print(window_width, window_height)
        return window_width, window_height


if __name__ == '__main__':
    pass
    wicket = Wicket()
    wicket.create_window()
    wicket.set_window_title('窗口名称')
    wicket.set_window_size('500x500+0+0')
    wicket.get_size()
    wicket.show_window()
