# -*- coding: utf-8 -*-
import tkinter.font

if __name__ == '__main__':
    root = tkinter.Tk()
    families = tkinter.font.families(root)
    print(families)
    for family in set(families):
        print(family)
        with open('fonts.txt', 'a', encoding='utf-8') as f:
            f.write(family)
            f.write('\n')
