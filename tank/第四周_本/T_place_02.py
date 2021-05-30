#place()方法
from tkinter import *
#主窗口
win = Tk()
#创建窗体
frame = Frame (win, relief=RAISED, borderwidth=2, width=400, height=300)
frame. pack (side=TOP, fill=BOTH,ipadx=5, ipady=5, expand=1)

ent_input = Entry(frame)
ent_input.place(x=10 ,y=10, anchor=NW, width=120, height=30 )
for i in range (3,0,-1):
    for j in range (3,0,-1):
        print (i,j,(i-1)*3+j)
        but = Button ( frame, text="%s"%((i-1)*3+j))        
        print ('[%d,%d]'%(10 + j*30,40+30*i))
        but.place (x=10 + (j-1)*30,y=40+30*(3-i), anchor=NW, width=30, height=30)

but = Button ( frame, text="0")        
but.place (x=10 ,y=40+90, anchor=NW, width=60, height=30)
but = Button ( frame, text=".")        
but.place (x=10+60 ,y=40+90, anchor=NW, width=30, height=30)

but = Button ( frame, text="+")        
but.place (x=10+90 ,y=40, anchor=NW, width=30, height=60)

#开始窗口的事件循环
win. mainloop()
