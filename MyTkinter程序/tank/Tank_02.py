import tkinter as tk
import time

class Tank():
    def __init__(self, canvas, zoom,points):
        self.canvas = canvas
        self.zoom = zoom
        self.points = points
        
    def draw(self, x=0, y=0):
        # 删除所有标注为tank 的对象

        self.canvas.delete('tank')
        for point in self.points:
            l = point['points']
            pp = [
                self.zoom*l[0] + x,
                self.zoom*l[1]+y,
                self.zoom*l[2]+x,
                self.zoom*l[3]+y
            ]
            # 每一个矩形都标注为tank的对象
            self.canvas.create_rectangle(pp, fill=point['color'], tags='tank')


win = tk.Tk()

canvas = tk.Canvas(win, width=600, height=400, bg='grey')
canvas.pack(fill='both')
'''
zoom = 5
points = [
    [1, 2, 6, 23],
    [6, 3, 18, 22],
    [18, 2, 23, 23],
    [7, 10, 16, 20],
    [10, 1, 14, 10]
]

for point in points :
    pp =[]
    for i in point:
        pp.append(zoom*i)

    canvas.create_rectangle(pp)
'''

TankUp = [
    {'color': 'red','points': [1, 2, 6, 23]},
    {'color': 'pink','points': [6, 3, 18, 22]},
    {'color': 'red','points': [18, 2, 23, 23]},
    {'color': 'yellow','points': [7, 10, 16, 20]},
    {'color': 'blue','points': [10, 1, 14, 10]}
]

tankUp = Tank(canvas, zoom=5, points=TankUp)

X = 100
Y = 200
tankUp.draw(x=X, y=Y)
while True:  # 要注意while语句以防止死循环，先设置为真
    X -= 0
    Y -= 2
    tankUp.draw(x=X, y=Y)
    win.update()  # 更新框架
    time.sleep(0.05)  # 睡眠0.01秒

win.mainloop()
