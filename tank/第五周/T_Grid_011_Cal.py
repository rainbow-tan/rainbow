from tkinter import *
import  tkinter.font   as  tkFont  #导入Tkinter字体模块

reset = True
def buttonCallBack(event):
    global label,reset
    showText = "1234567890.+-*/"
    num = event.widget['text']
    
    if label['text'] == '0' or reset == True:
        label['text'] = ""
        reset = False

    if num in showText:
        label['text'] = label['text'] + num
        return
    if num in "=":
        label['text'] = str(eval(label['text']))
        reset = True
        return
    if num == 'C':
        label['text'] = "0"
        return
    
'''
def buttonCallBack(event):
    global label,reset
    num = event.widget['text']
    if num == 'C':
        label['text'] = "0"
        return
    if num in "=":
        label['text'] = str(eval(label['text']))
        reset = True
        return
    s = label['text']
    if s == '0' or reset == True:
        s = ""
        reset = False
    label['text'] = s+num
'''

# 主窗口
root = Tk()
root.wm_title("计算器")
# 显示栏1
f = tkFont.Font(family="黑休", size=16, weight="bold",slant= "roman")
label = Label(root, text="0", background="darkgreen", fg = 'white',anchor="e",font =f )
label['width'] = 35
label['height'] = 2
label.grid(row=1, columnspan=4, sticky=W,padx = 20,pady = 5)
# 按钮
showText = "789/456*123-0.C+"
for i in range(4):
    for j in range(4):
        b = Button(root, text=showText[i*4+j], width=5,font =f ) 
        b.grid(row=i+2, column=j,padx = 0,pady = 5)
        b.bind("<Button-1>", buttonCallBack)
showText = "()"
for i in range(2):
    b = Button(root, text=showText[i], width=5,font =f )
    b.grid(row=6, column=2+i,padx = 0,pady = 5)
    #b.bind("<button-1>", buttonCallBack)
b = Button(root, text="=",font =f )
b.grid(row=6, columnspan=2, sticky="we",padx = 20,pady = 5)
b.bind("<Button-1>", buttonCallBack)
root.mainloop()
