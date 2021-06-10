from tkinter import *
import threading
import random
import time
from Tcolor import *


class Base(threading.Thread):
    '''
    定义坦克 子弹 爆炸等的基类
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
        self._canvas = canvas

        # 保存小球颜色
        self._color = color
        # 保存中心点坐标
        self._x = x
        self._y = y
        # 保存移动步长
        self._dx = 0
        self._dy = 0
        #对象ID
        self._id = None

        #运行停止条件
        self._stop = False

    # 获取画布的宽高
    @property
    def Can_width(self):
        return self._canvas.winfo_width()

    @property
    def Can_Height(self):
        return self._canvas.winfo_height()

    def draw(self):
        # 绘制自己
        print('Base.draw')
        pass

    def move(self):
        # 移动自己
        self._canvas.move(self._id, self._dx, self._dy)

    def next(self):
        # 重新定位 自己的XY 坐标
        pass

    def run(self):
        while not self._stop:
            self.next()
            time.sleep(0.05)

class Hero(Base):
    '''
    定义坦克
    '''
    def __init__(self, canvas, x=100, y=250, color='blue'):
        super().__init__(canvas, x=x, y=y, color=color)

        # 坦克宽度
        self._size = 24
        #X方向的步长
        self._step = 10
        self._dx = self._step

        self.draw()
        # self.id = self.canvas.create_rectangle(
        #    self._x, self._y, self._x+self.PaddleWidth, self._y+self.PaddleHeight, fill=self.color)
        # 画板绑定键盘的任何事件
        self._canvas.bind_all('<Key>', self.AnyKey)

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
            self._dx = self._step
            # 如果 已经到达 右边
            if (self._x+self._size > self.Can_width):
                self._x = self.Can_width -self._size 
                #不动
                self._dx = 0

        elif event.keysym == 'Left' :
            print ('event.keysym == Left',self._dx ,self._step)
            self._dx = (-1) *self._step
            # 如果 已经到达 左边
            if (self._x < 0):
                self._x = 0
                #不动
                self._dx = 0

        #print (event.keysym,self._x ,self._dx)
        self._x += self._dx     
        self.move()    
 

    def draw(self):
        self._id = self._canvas.create_rectangle(
            self._x-self._size, self._y-self._size, 
            self._x+self._size, self._y+self._size, outline=self._color)

class Enemy(Base):
    '''
    定义小球
    '''

    def __init__(self, canvas, x=100, y=250, r=30, color='blue'):
        '''
        参数说明:
        画布  canvas
        中心点[x,y] 
        半径 r
        小球颜色 color 
        '''
        super().__init__(canvas, x=x, y=y, color=color)

        # 坦克大小
        self._size = 24

        # 随机生成XY方向的步长 _dx _dy
        ss = [-5, -3, -1, 1, 3, 5]
        s = random.choices(ss, k=2)
        #print (s)
        self._dx = s[0]  # random.choice(ss) # random.randint(-5,5)
        self._dy = s[1]  # random.choice(ss) # random.randint(-5,5)
        #print ('self._dx,self._dy',self._dx,self._dy)
        
        # 绘制小球
        self.draw()

    def draw(self):
        print('Ball.draw')
        # 绘制小球
        self._id = self._canvas.create_rectangle(
            self._x-self._size, self._y-self._size, 
            self._x+self._size, self._y+self._size, outline=self._color)
    

    def next(self):
        '''
        坦克随机运动
        '''
        # 计算新的中心点坐标 和  X Y方向的步长
        # 计算新的中心点 X 坐标
        
        # 如果 已经到达 右边
        if (self._x+self._size > self.Can_width):
            self._x = self.Can_width - self._size
            # X方向的步长值 为原值的相反  ？？思考
            self._dx = (-1)*self._dx
        # 如果 已经到达 左边
        if (self._x-self._size < 0):
            self._x = self._size + 1
            self._dx = (-1)*self._dx

        self._x += self._dx

        # 计算新的中心点 Y 坐标

        # 如果 已经到达 底边
        if (self._y+self._size > self.Can_Height):
            self._y = self.Can_Height - self._size
            # X方向的步长值 为原值的相反  ？？思考
            self._dy = (-1)*self._dy

            # 如果小球碰到画布底端 则返回hit_bottom为True
            self.hit_bottom = True

        # 如果 已经到达 顶边
        if (self._y-self._size < 0):
            self._y = self._size + 1
            self._dy = (-1)*self._dy


        if self._y + self._size >= self.Can_Height:  
            # 如果小球碰到画布底端 则 self.Stop 为True
            # 小球停止 
            self._stop = True

        self._y += self._dy

        self.move()

# 测试小球
if __name__ == '__main__':
    win = Tk()
    win.geometry('600x400+100+100')

    mycanvas = Canvas(win, width=300, height=200, bg='white')
    mycanvas.pack(padx=0, fill='both', expand=True)
    win.update()

    hero = Hero(mycanvas, x=100, y=250, color='red')

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
        enemy = Enemy(mycanvas, x=random.randint(50, 550), y=random.randint(
            50, 350), r=random.randint(10, 60), color=CColors[color])
        balls.append(enemy)
        enemy.start()

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
