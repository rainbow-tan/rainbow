from tkinter import *
import random

class Paddle():
    '''
    定义球拍
    '''

    def __init__(self, canvas, x=100, y=250, color='blue'):
        # 保存画板
        self.canvas = canvas
        # 保存小球颜色
        self.color = color
        # 保存左上角坐标
        self._x = x
        self._y = y
        # 球拍宽度
        self.width = 100
        self.height = 15
        
        #X方向的步长
        self.Step = 10
        self._dx = self.Step
        # 获取画布的宽度
        self.CancasWidth = self.canvas.winfo_width()
        self.id = self.canvas.create_rectangle(
            self._x, self._y, self._x+self.width, self._y+self.height, fill=self.color)

        # 画板绑定键盘的左右键事件
        # self.canvas.bind_all('<KeyPress-Right>',self.Trun_Right)
        # self.canvas.bind_all('<KeyPress-Left>',self.Trun_Left)

        # 画板绑定键盘的左右键事件
        # self.canvas.bind_all('<Right>',self.Trun_Right)
        # self.canvas.bind_all('<Left>',self.Trun_Left)

        # 画板绑定键盘的任何事件
        self.canvas.bind_all('<Key>', self.AnyKey)

    def AnyKey(self, event):
        '''
        键盘的任何事件
        '''
        
        # 如果 不是左右键 则不处理
        if (event.keysym not in ['Left', 'Right']):
            return

        #self._dx = self.Step
        # 计算新左上角坐标 和  X方向的步长
        if event.keysym == 'Right' : 
            self._dx = self.Step
            # 如果 已经到达 右边
            if (self._x+self.width > self.CancasWidth):
                self._x = self.CancasWidth -self.width 
                #不动
                self._dx = 0
        elif event.keysym == 'Left' :
            print ('event.keysym == Left',self._dx ,self.Step)
            self._dx = (-1) *self.Step
            # 如果 已经到达 左边
            if (self._x < 0):
                self._x = 0
                #不动
                self._dx = 0

        #print (event.keysym,self._x ,self._dx)
        self._x += self._dx                
        self.draw()

    '''
    def Trun_Right(self, event):
        self._x += 5
        if (self._x+100 > self.CancasWidth):
            self._x = self.CancasWidth - 100
        self.draw()

    def Trun_Left(self, event):
        self._x -= 5
        if (self._x < 0):
            self._x = 0
        self.draw()
    '''

    def draw(self):
        self.canvas.moveto(self.id, self._x, self._y)

print  ('__name__ = ',__name__)

if __name__ == '__main__':      
    win = Tk()
    win.geometry('600x400+100+100')

    mycanvas = Canvas(win, width=300, height=200, bg='yellow')
    mycanvas.pack(fill='both', expand=True)
    win.update()

    paddle = Paddle(mycanvas, x=100, y=250,color ='red')

    win.mainloop()
