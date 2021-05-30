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
        self.PaddleWidth = 100
        self.PaddleHeight = 15
        # 随机生成X方向的步长 _dx 使每次运行的速度不同
        ss = [-5, -3, -2,2, 3, 5]
        s = random.choice(ss)
        #print (s)
        self.Step = s  # random.choice(ss) # random.randint(-5,5)
        self._dx = self.Step
        # 获取画布的宽度
        self.width = self.canvas.winfo_width()
        self.id = self.canvas.create_rectangle(
            self._x, self._y, self._x+self.PaddleWidth, self._y+self.PaddleHeight, fill=self.color)

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
        print (event.keysym,self._x ,self._dx)
        # 如果 不是左右键 则不处理
        if (event.keysym not in ['Left', 'Right']):
            return

        self._x += self._dx
        
        # 计算新左上角坐标 和  X方向的步长
        if event.keysym == 'Left' :
            self._dx = self.Step
            # 如果 已经到达 左边
            if (self._x < 0):
                self._x = 0
                self._dx = (-1)*self.Step
            elif (self._x+self.PaddleWidth > self.width):
                self._x = self.width -self.PaddleWidth 
                #不动
                self._dx = 0
        elif event.keysym == 'Right' :
            self._dx = (-1) *self.Step
            # 如果 已经到达 右边
            if (self._x+self.PaddleWidth > self.width):
                self._x = self.width -self.PaddleWidth
                # X方向的步长值 为原值的相反  ？？思考
                self._dx = self.Step
            elif (self._x < 0):
                self._x = 0
                #不动
                self._dx = 0
        self.draw()

    '''
    def Trun_Right(self, event):
        self._x += 5
        if (self._x+100 > self.width):
            self._x = self.width - 100
        self.draw()

    def Trun_Left(self, event):
        self._x -= 5
        if (self._x < 0):
            self._x = 0
        self.draw()
    '''

    def draw(self):
        self.canvas.moveto(self.id, self._x, self._y)

win = Tk()
win.geometry('600x400+100+100')

mycanvas = Canvas(win, width=300, height=200, bg='yellow')
mycanvas.pack(fill='both', expand=True)
win.update()

paddle = Paddle(mycanvas, x=100, y=250,color ='red')

win.mainloop()
