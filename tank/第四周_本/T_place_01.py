#place()方法
#体验 Button 的  x,y 位置 和 width=80, height
#体验 Frame 的relief=RAISED, borderwidth=2, width=400, height 
from tkinter import *
#主窗口
win = Tk()
#创建窗体
#relief 表示边框样式，可选的参数有：flat(平的)，sunken (沉没的, 凹下去的)，raised (提高，凸出来的)，ridge(脊，中键凸的)
frame = Frame (win, relief='sunken', borderwidth=4, width=400, height=300)
frame. pack (side=TOP, fill=BOTH,ipadx=5, ipady=5, expand=1)
#第一个按钮的位置在距离窗体左上角的(40，40)坐标处
button1 = Button ( frame, text="Button 1")
button1.place (x=40,y=40, anchor=W, width=80, height=40)
#第二个按钮的位置在距离窗体左.上角的(140，80) 坐标处
button2 = Button (frame, text="Button 2")
button2 .place(x=140,y=20, anchor=W, width=80, height=60)
#开始窗口的事件循环
win. mainloop()
