from tkinter import *
import random
import time
import threading

class Base(threading.Thread):
    '''
    定义基类
    '''
    def __init__(self, canvas:Canvas,  x=100, y=250, color='blue'):
        '''
        参数说明:
        画布  canvas
        坐标点[x,y] 
        对象颜色 color 
        '''
        super().__init__()  # 重构run函数必须要写
        #print (x,y,r,color)
        # 保存画板
        self.canvas = canvas

        # 保存颜色
        self.color = color
        # 保存坐标
        self._x = x
        self._y = y

        # 获取画布的宽高
        self.width = self.canvas.winfo_width()
        self.height = self.canvas.winfo_height()

        self.id = None

    def draw(self):
        #绘制自己
        pass

    def move(self):
        #移动 dx,dy
        self.canvas.move(self.id, self._dx,self._dy)

    def Next(self):
        pass

    def run(self):
        while True:
            self.Next()
            time.sleep(0.1)
        
 
class Ball(Base):
    '''
    定义小球
    '''
    def __init__(self, canvas,  x=100, y=250, r=30, color='blue'):
        '''
        参数说明:
        画布  canvas
        中心点[x,y] 
        半径 r
        小球颜色 color 
        '''
        super().__init__(canvas,  x=x, y=y, color=color)
        # 保存半径
        self._r = r
        # 随机生成XY方向的步长 _dx _dy
        ss = [-5, -3, -1, 1, 3, 5]
        s = random.choices(ss, k=2)
        #print (s)
        self._dx = s[0]  # random.choice(ss) # random.randint(-5,5)
        self._dy = s[1]  # random.choice(ss) # random.randint(-5,5)
       
    def draw(self):
          # 绘制小球
        self.id = self.canvas.create_oval(
            self._x-self._r, self._y-self._r, self._x+self._r, self._y+self._r, fill=self.color)

    def Next(self):
        '''
        小球随机运动
        '''
        # 计算新的中心点坐标 和  X Y方向的步长
        # 计算新的中心点 X 坐标
        self._x += self._dx
        # 如果 已经到达 右边
        if (self._x+self._r > self.width):
            self._x = self.width - self._r
            # X方向的步长值 为原值的相反  ？？思考
            self._dx = (-1)*self._dx
        # 如果 已经到达 左边
        if (self._x-self._r < 0):
            self._x = self._r + 1
            self._dx = (-1)*self._dx

        # 计算新的中心点 Y 坐标
        self._y += self._dy
        # 如果 已经到达 底边
        if (self._y+self._r > self.height):
            self._y = self.height - self._r
            # X方向的步长值 为原值的相反  ？？思考
            self._dy = (-1)*self._dy
        # 如果 已经到达 顶边
        if (self._y-self._r < 0):
            self._y = self._r + 1
            self._dy = (-1)*self._dy

        self.move()

#测试
win = Tk()
win.geometry('600x400+100+100')

canvas = Canvas(win,bg = 'green')
canvas.pack(fill = 'both',expand = True)


balls = []
for i in range (0,10):
    ball = Ball(canvas,x=100,y=100,color = 'pink')
    ball.draw()
    win.update()
    ball.start()


'''


balls = []
for i in range (0,10):
    ball = Ball(canvas,x=100,y=100,color = 'pink')
    ball.draw()
    balls.append(ball)

while True:
    for ball in balls:
        ball.Next()

    win.update()
    time.sleep(0.1)
'''
win.mainloop()
