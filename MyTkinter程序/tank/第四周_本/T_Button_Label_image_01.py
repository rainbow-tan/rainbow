from tkinter import *

root = Tk()  
 
photo = PhotoImage(file=r'Images\Boy\3.png')
but_img_OK = PhotoImage(file=r'Images\WinVista\Default_24.png')
img_label = Label(root, imag=photo)
img_label.pack()    #独立.pack出来！<=====================
count = 1

def start():
    #要改的label、替换的图片，缺一不可都要global引用！<======================
    global img_label,count,photo
    count += 1
    count %= 8
    photo = PhotoImage (file="Images\\Boy\\{}.png".format (count))
    img_label.configure(imag=photo)
 
button_img = Button(root,text = '开始',image =but_img_OK, compound="right", command=start).pack()
 
root.mainloop()
