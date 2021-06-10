# -*- encoding=utf-8 -*-
from PIL import Image

#切割图片
im = Image.open("image/enemyTank/enemy_1_1.png")
'''
print(im.size) ## 打印出尺寸信息
print(im.mode)   ## 打印出模式信息
print(im.format) ## 打印出格式信息
print(im.palette)
print(im.info)
'''

fix = 'Green_'
Dir = ['Up','Down','Left','Right']

for row in range(4):
    for col in range(2):
        box = (col*48, row*48, (col+1)*48-1, (row+1)*48-1)              ##确定拷贝区域大小
        region = im.crop(box)                   ##将im表示的图片对象拷贝到region中，大小
        filename = fix +Dir[row] +'_'+str(col) + '.png'
        print (filename)
        region.save(filename)