#from tkinter import *
import tkinter as tk

root = tk.Tk()

root.geometry ('300x400+150+150')

#第一
#tk.Label(root, text="Red", bg="red", fg="white").pack(fill="x")
#tk.Label(root, text="Red", bg="red", fg="white").pack(fill="both", expand=True)

'''
#第二 按行布局
tk.Label(root, text="Red", bg="red", fg="white").pack(fill="x")
tk.Label(root, text="Green", bg="green", fg="black").pack(fill="x")
#tk.Label(root, text="Blue", bg="blue", fg="white").pack(fill="x")
tk.Label(root, text="Blue", bg="blue", fg="white",width = 100,padx=50,justify = 'right').pack(fill="both", expand=True) #,padx=50)
''' 
#第三 横向一行放儿排放
tk.Label(root, text="Red", bg="red", fg="white",width = 100,padx = 50 ).pack(padx = 20,side="top")
tk.Label(root, text="Green", width = 100,bg="green", fg="black").pack(side="bottom")
#观察 加入,width = 100后的结果
tk.Label(root, text="Yellow", bg="blue", fg="yellow",padx = 10).pack(side="right")
tk.Label(root, text="Blue", bg="blue", fg="white",width = 100,padx = 100).pack(side="left")
#tk.Label(root, text="Blue", bg="blue", fg="white",width = 100,padx=50,justify = 'right').pack(fill="both", expand=True) #,padx=50)


root.mainloop()
