from tkinter import *

root = Tk()  
root.geometry('300x200+150+150')

lab_text = Label(root, text = '点击次数= 0')
lab_text.pack()    #独立.pack出来！<=====================
count = 0
'''
def start():
    #要改的label、替换的图片，缺一不可都要global引用！<======================
    global lab_text,count
    count += 1
    lab_text.configure(text='点击次数= %d'%count)
''' 
def start(event):
    #要改的label、替换的图片，缺一不可都要global引用！<======================
    global lab_text,count
    count += 1
    #获取事件源的方式
    ss = '事件源:%s \n 事件源的文本:%s   ' %(event.widget,event.widget['text'])
    lab_text.configure(text= ss +'点击次数= %d'%count)
    #lab_text.configure(text= event.widget['text'] + '点击我 \n' +'点击次数= %d'%count)

but_OK = Button(root,text = '开始')
but_OK.bind('<Button-1>',start)
but_OK.pack(side= 'right')

but_Cancel = Button(root,text = '取消')
but_Cancel.bind('<Button-1>',start)
but_Cancel.pack(side = 'left')

root.mainloop()
