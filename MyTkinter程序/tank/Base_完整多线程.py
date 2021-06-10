from tkinter import *
import threading
import random
import time
from Tcolor import *


class Base(threading.Thread):
    '''
    定义小球和球拍的基类
    '''

    def __init__(self, canvas,  x=100, y=250, color='blue'):
        '''
        参数说明:
        画布  canvas
        坐标 [x,y] 
        小球颜色 color 
        '''
        # super() 首先找到 Ball 的父类（就是类 threading.Thread），
        # 然后把类 Ball 的对象转换为类 threading.Thread 的对象
        super().__init__()  #重构run函数必须写 super().__init__()

        # 保存画板
        self.canvas = canvas

        # 保存小球颜色
        self.color = color
        # 保存中心点坐标
        self._x = x
        self._y = y

        # 获取画布的宽高
        self.Can_width = self.canvas.winfo_width()
        self.Can_height = self.canvas.winfo_height()
        
        self._dx = 0
        self._dy = 0
        self.id = None

        #停止条件
        self.Stop = False

    def draw(self):
        # 绘制自己
        print('Base.draw')
        pass

    def move(self):
        # 移动自己
        self.canvas.move(self.id, self._dx, self._dy)

    def next(self):
        # 重新定位 自己的XY 坐标
        pass

    def run(self):
        while not self.Stop:
            self.next()
            time.sleep(0.05)

class Paddle(Base):
    '''
    定义球拍
    '''
    def __init__(self, canvas, x=100, y=250, color='blue'):
        super().__init__(canvas, x=x, y=y, color=color)

        # 球拍宽度
        self.width = 100
        self.height = 15
        #X方向的步长
        self.Step = 10
        self._dx = self.Step
        
        

        self.draw()
        # self.id = self.canvas.create_rectangle(
        #    self._x, self._y, self._x+self.PaddleWidth, self._y+self.PaddleHeight, fill=self.color)
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
            if (self._x+self.width > self.Can_width):
                self._x = self.Can_width -self.width 
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
        self.move()    
 

    def draw(self):
        self.id = self.canvas.create_rectangle(
            self._x, self._y, self._x+self.width,
            self._y+self.height, fill=self.color)
    def ChangeSize(self):
        # 重新获取Canvas 的宽度
        self.width = self.canvas.winfo_width()


class Ball(Base):
    '''
    定义小球
    '''

    def __init__(self, canvas, paddle: Paddle, x=100, y=250, r=30, color='blue'):
        '''
        参数说明:
        画布  canvas
        中心点[x,y] 
        半径 r
        小球颜色 color 
        '''
        super().__init__(canvas, x=x, y=y, color=color)
        self.paddle = paddle

        # 保存半径
        self._r = r
        # 随机生成XY方向的步长 _dx _dy
        ss = [-5, -3, -1, 1, 3, 5]
        s = random.choices(ss, k=2)
        #print (s)
        self._dx = s[0]  # random.choice(ss) # random.randint(-5,5)
        self._dy = s[1]  # random.choice(ss) # random.randint(-5,5)
        #print ('self._dx,self._dy',self._dx,self._dy)
        
        # 绘制小球
        self.draw()

    
    def hit_paddle(self):  # 声明函数，以供调用
        # 园心的X坐标落在拍上
        if ((self._x >= self.paddle._x) and
                (self._x <= self.paddle._x+self.paddle.width)):
            # 园心的Y + 半径 坐标落在球拍上的 Y坐标 +self.paddle.height
            if ((self._y + self._r >= self.paddle._y) and (self._y + self._r <= self.paddle._y+self.paddle.height)):
                # 比较小球y轴是否在球拍y轴内    
                return True  # 表示小球碰到了球拍
        return False  # 表示小球没有碰到球拍

    def draw(self):
        print('Ball.draw')
        # 绘制小球
        self.id = self.canvas.create_oval(
            self._x-self._r, self._y-self._r, self._x+self._r, self._y+self._r, fill=self.color)
    

    def next(self):
        '''
        小球随机运动
        '''
        # 计算新的中心点坐标 和  X Y方向的步长
        # 计算新的中心点 X 坐标
        
        # 如果 已经到达 右边
        if (self._x+self._r > self.Can_width):
            self._x = self.Can_width - self._r
            # X方向的步长值 为原值的相反  ？？思考
            self._dx = (-1)*self._dx
        # 如果 已经到达 左边
        if (self._x-self._r < 0):
            self._x = self._r + 1
            self._dx = (-1)*self._dx

        self._x += self._dx

        # 计算新的中心点 Y 坐标

        # 如果 已经到达 底边
        if (self._y+self._r > self.Can_height):
            self._y = self.Can_height - self._r
            # X方向的步长值 为原值的相反  ？？思考
            self._dy = (-1)*self._dy

            # 如果小球碰到画布底端 则返回hit_bottom为True
            self.hit_bottom = True

        # 如果 已经到达 顶边
        if (self._y-self._r < 0):
            self._y = self._r + 1
            self._dy = (-1)*self._dy


        # 小球碰到了球拍，则改变Y轴方向向上运动
        if self.hit_paddle() == True:
            print ('hit_paddle() == True')  
            self._dy = -self._dy

        if self._y + self._r >= self.Can_height:  
            # 如果小球碰到画布底端 则 self.Stop 为True
            # 小球停止 
            self.Stop = True

        self._y += self._dy

        self.move()

# 测试小球
if __name__ == '__main__':

    def ChangeConfigure(event):
        paddle.ChangeSize()

    win = Tk()
    win.geometry('600x400+100+100')

    mycanvas = Canvas(win, width=300, height=200, bg='white')
    mycanvas.pack(padx=0, fill='both', expand=True)
    win.update()

    win.bind('<Configure>', ChangeConfigure)
    paddle = Paddle(mycanvas, x=100, y=250, color='red')

    # 从CColors随机选择十种颜色
    #print (list(CColors.keys()))
    colors = random.choices(list(CColors.keys()), k=3)
    #print (colors)
    # 生成十种颜色的小球
    balls = []
    for color in colors:
        #print (i)
        #ball = Ball(mycanvas,x= 100,y=250,r=30,color = CColors[color] )
        # 随机的中心位置和半径
        ball = Ball(mycanvas, paddle= paddle, x=random.randint(50, 550), y=random.randint(
            50, 350), r=random.randint(10, 60), color=CColors[color])
        balls.append(ball)
        ball.start()

    #ball2 = Ball(mycanvas,x= 200,y=150,r=35,color = 'yellow')
    win.update()
    '''
    # 让十个小球随机运动
    while True:
        for ball in balls:
            ball..next()
        # 测试 有没有 win.update() 语句 的不同效果
        win.update()
        time.sleep(0.05)
    '''
    win.mainloop()
