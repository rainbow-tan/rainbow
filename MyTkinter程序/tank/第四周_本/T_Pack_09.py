#from tkinter import *
#pack()方法使用
from tkinter import *
#主窗口
win = Tk()
#第一个窗体
frame1 = Frame (win, bg= 'gray',relief=RAISED, borderwidth=2)
frame1 .pack(side=TOP, fill=BOTH, ipadx=13, ipady=13, expand=0)
Button(frame1,text="Button 1") .pack(side=LEFT, padx=13, pady=13)
Button(frame1, text="Button 2") .pack(side=LEFT, padx=13, pady=13)
Button(frame1, text="Button 3") .pack (side=LEFT, padx=13, pady=13)
	
#第二个窗体
frame2 = Frame (win,bg= 'green', relief=RAISED, borderwidth=2)
frame2 . pack (side=BOTTOM, fill=NONE, ipadx="1c", ipady="1c", expand=1)
Button (frame2, text="Button 4") .pack (side=RIGHT, padx="1c", pady="1c")
Button (frame2,text="Button 5") .pack (side=RIGHT, padx="1c", pady="1c")
Button (frame2,text="Button 6") .pack (side=RIGHT, padx="1c", pady="1c")
	
#第三个窗体
frame3 = Frame (win,bg= 'blue', relief=RAISED, borderwidth=2)
frame3. pack (side=LEFT, fill=X, ipadx="0.1i", ipady="0.1i", expand=1)
Button (frame3, text="Button 7") .pack(side=TOP, padx="0.1i", pady="0.1i")
Button (frame3, text="Button 8") .pack(side=TOP, padx="0.1i", pady="0.1i")
Button(frame3, text="Button 9") .pack(side=TOP, padx="0.1i", pady="0.1i")
	
#第四个窗体
frame4 = Frame (win,bg= 'yellow', relief=RAISED, borderwidth=2)
frame4. pack (side=RIGHT, fill=Y, ipadx="13p", ipady="13p", expand=1)
Button(frame4, text="Button 13") . pack (side=BOTTOM, padx="13p",pady="13p")
Button (frame4, text="Button 11") .pack (side=BOTTOM, padx="13p" ,pady="13p")
Button (frame4, text="Button 12") .pack (side=BOTTOM, padx="13p",pady="13p")

#开始窗口的事件循环
win.mainloop()
