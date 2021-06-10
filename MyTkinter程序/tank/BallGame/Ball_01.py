import random
import time
from tkinter import *


#下面定义一个球的类，有canvas和color两个对象
class Ball:      #定义一个Ball类的函数
    def __init__(self,canvas,color):#这是Ball类的属性函数，Ball类下的函数都有这些性质
        self.canvas=canvas
        self.color = color
        #self.id=canvas.create_oval(10,10,25,25,fill=color)#返回所绘小球的调用值放入对象self.id
        self.postion =[245,100,280,135]
        self.id=canvas.create_oval(10,10,41,41,fill=color,tags= 'Ball')#返回所绘小球的调用值放入对象self.id
        self.canvas.move(self.id,self.postion[0],self.postion[1])   #移动小球到（245，100）坐标处，

        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]       #使得小球左右方向运动随机
        self.y=-3              #默认开始的小球向上方运动
        
        self.canvas_height=self.canvas.winfo_height()#画布高度函数winfo_height()返回值放入canvas_height对象中
        self.canvas_width=self.canvas.winfo_width()  #winfo_width()返回画布宽度放入canvas_width对象中

    def draw(self):    #声明draw函数，
        #self.canvas.move(self.id,self.x,self.y)   #移动小球，移动速度为（self.x,self.y），在init中的属性可以直接用
        #pos=self.canvas.coords(self.id)#把小球的左上角和右下角的坐标以列表形式（可能元组）放入pos对象中
        self.canvas.delete('Ball')#返回所绘小球的调用值放入对象self.id

        print (self.postion) 
        if self.postion[1]<=0:     #如果小球碰到画布上方
            self.y=3      #则改变移动方向向下方
        if self.postion[3]>=self.canvas_height: #如果小球碰到画布底端 则返回hit_bottom为True
            self.y=-3
            #self.hit_bottom=True

        if self.postion[0]<=0:    #如果小球碰到了画布左边，则把X轴速度改成每次向右3个像素
            self.x=3
        if self.postion[2]>=self.canvas_width:   #如果小球碰到了画布右边，则把速度改成每次向左3个像素
            self.x=-3
    
        self.postion[0] += self.x
        self.postion[1] += self.y
        self.postion[2] = self.postion[0] + 35
        self.postion[3] = self.postion[1] + 35

        self.id =self.canvas.create_oval(self.postion[0],self.postion[1],self.postion[2],self.postion[3],fill=self.color,tags= 'Ball')#返回所绘小球的调用值放入对象self.id
        

#创建框架并且命名和固定，然后创建该框架的画布
tk=Tk()  #创建框架对象tk
tk.title('Ball Game')   #框架对象tk显示的名字为'game'
tk.resizable(0,0)   #固定框架
tk.wm_attributes('-topmost',1)  #显示在最外层
canvas=Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)  #创建画布canvas，属于tk框架对象，
canvas.pack()  #显示画布的变化

w =canvas.winfo_width()
h=canvas.winfo_height()
print ("win [%s,%s]"%(canvas.winfo_width(),canvas.winfo_height()) )
print ("win [%s,%s]"%(tk.winfo_width(),tk.winfo_height()) )
tk.update()    #显示框架的变化
print ("win [%s,%s]"%(tk.winfo_width(),tk.winfo_height()) )

#把类赋值给对象ball，如果调用了ball就可以实现该类的作用
ball=Ball(canvas,'green') #调用球的类给对象ball用

while True:   #要注意while语句以防止死循环，先设置为真
    ball.draw()   #调用ball对象的函数draw（）
    tk.update_idletasks()
    tk.update()    #更新框架
    time.sleep(0.02) #睡眠0.01秒
'''
while True:   #要注意while语句以防止死循环，先设置为真
    if ball.hit_bottom==False:  #没有碰到底部的话执行下面的语句
        ball.draw()   #调用ball对象的函数draw（）
        tk.update_idletasks()
        tk.update()    #更新框架
        time.sleep(0.01) #睡眠0.01秒
    
    elif ball.hit_bottom==True:  #要是小球接触了底部
        canvas.create_text(200,100,text='Aha,you lose it,\nHow about try again?',font=('Times',22)) #在（200，100）坐标处创建文本‘...’，字号22号
        tk.update()  #更新内容
'''