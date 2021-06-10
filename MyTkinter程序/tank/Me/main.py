# -*- encoding=utf-8 -*-

from Base import Base
from Brick import Brick
from Enemy import Enemy
from Hero import *
from Home import Home
from Iron import Iron
from Tree import Tree


class Main(Base):
    def __init__(self, canvas, x=100, y=250):
        super().__init__(canvas, x, y)

    def random_enemy(self):
        # 敌人安排
        enemy = Enemy(canvas, x=24, y=24, step=24, direction='right')
        enemy.start()
        enemy = Enemy(canvas, x=24 + 48 * 1, y=24, step=24, direction='right')
        enemy.start()
        enemy = Enemy(canvas, x=24 + 48 * 3, y=24, step=24, direction='right')
        enemy.start()
        enemy = Enemy(canvas, x=24 + 48 * 5, y=24, step=24, direction='right')
        enemy.start()
        enemy = Enemy(canvas, x=24 + 48 * 7, y=24, step=24, direction='right')
        enemy.start()
        enemy = Enemy(canvas, x=24 + 48 * 9, y=24, step=24, direction='right')
        enemy.start()

    def main(self):
        # 部署情景与英雄
        tree = Tree(canvas, 0, 0, path='image/scene/tree.png')
        brick = Brick(canvas, 0, 0, )
        iron = Iron(canvas, 0, 0, )
        tank = Hero(canvas)
        home = Home(canvas)
        self.random_enemy()


if __name__ == '__main__':
    win = Tk()
    win.title('坦克大战')
    win.geometry('624x624+500+10')
    win.resizable(0, 0)
    canvas = Canvas(win, bg='white')
    canvas.pack(fill='both', expand=True)
    win.update()
    main = Main(canvas)
    main.main()
    win.mainloop()
