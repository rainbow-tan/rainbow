from tkinter import *
import random
import time

CColors ={
    '浅粉红':'#FFB6C1',
    '粉红':'#FFC0CB',      
    '深红':'#DC143C',      
    '淡紫红':'#FFF0F5',    
    '弱紫罗兰红':'#DB7093',
    '热情的粉红':'#FF69B4',
    '深粉红':'#FF1493',
    '中紫罗兰红':'#C71585',
    '暗紫色':'#DA70D6',
    '蓟色':'#D8BFD8',
    '洋李色':'#DDA0DD',
    '紫罗兰':'#EE82EE',
    '洋红':'#FF00FF',
    '紫红':'#FF00FF',
    '深洋红':'#8B008B',
    '紫色':'#800080',
    '中兰花紫':'#BA55D3',
    '暗紫罗兰':'#9400D3',
    '暗兰花紫':'#9932CC',
    '靛青':'#4B0082',
    '蓝紫罗兰':'#8A2BE2',
    '中紫色':'#9370DB',
    '中暗蓝色':'#7B68EE',
    '石蓝色':'#6A5ACD',
    '暗灰蓝色':'#483D8B',
    '淡紫色':'#E6E6FA',
    '幽灵白':'#F8F8FF',
    '纯蓝':'#0000FF',
    '中蓝色':'#0000CD',
    '午夜蓝':'#191970',
    '暗蓝色':'#00008B',
    '海军蓝':'#000080',
    '皇家蓝':'#4169E1',
    '矢车菊蓝':'#6495ED',
    '亮钢蓝':'#B0C4DE',
    '亮蓝灰':'#778899',
    '灰石色':'#708090',
    '闪兰色':'#1E90FF',
    '爱丽丝蓝':'#F0F8FF',
    '钢蓝':'#4682B4',
    '亮天蓝色':'#87CEFA',
    '天蓝色':'#87CEEB',
    '深天蓝':'#00BFFF',
    '亮蓝':'#ADD8E6',
    '粉蓝色':'#B0E0E6',
    '军兰色':'#5F9EA0',
    '蔚蓝色':'#F0FFFF',
    '淡青色':'#E0FFFF',
    '弱绿宝石':'#AFEEEE',
    '青色':'#00FFFF',
    '浅绿色':'#00FFFF',
    '暗绿宝石':'#00CED1',
    '暗瓦灰色':'#2F4F4F',
    '暗青色':'#008B8B',
    '水鸭色':'#008080',
    '中绿宝石':'#48D1CC',
    '浅海洋绿':'#20B2AA',
    '绿宝石':'#40E0D0',
    '宝石碧绿':'#7FFFD4',
    '中宝石碧绿':'#66CDAA',
    '中春绿色':'#00FA9A',
    '薄荷奶油':'#F5FFFA',
    '春绿色':'#00FF7F',
    '中海洋绿':'#3CB371',
    '海洋绿':'#2E8B57',
    '蜜色':'#F0FFF0',
    '淡绿色':'#90EE90',
    '弱绿色':'#98FB98',
    '暗海洋绿':'#8FBC8F',
    '闪光深绿':'#32CD32',
    '闪光绿':'#00FF00',
    '森林绿':'#228B22',
    '纯绿':'#008000',
    '暗绿色':'#006400',
    '黄绿色':'#7FFF00',
    '草绿色':'#7CFC00',
    '绿黄色':'#ADFF2F',
    '暗橄榄绿':'#556B2F',
    '黄绿色':'#9ACD32',
    '橄榄褐色':'#6B8E23',
    '米色':'#F5F5DC',
    '亮菊黄':'#FAFAD2',
    '象牙色':'#FFFFF0',
    '浅黄色':'#FFFFE0',
    '纯黄':'#FFFF00',
    '橄榄':'#808000',
    '暗黄褐色':'#BDB76B',
    '柠檬绸':'#FFFACD',
    '灰菊黄':'#EEE8AA',
    '黄褐色':'#F0E68C',
    '金色':'#FFD700',
    '玉米丝色':'#FFF8DC',
    '金菊黄':'#DAA520',
    '暗金菊黄':'#B8860B',
    '花的白色':'#FFFAF0',
    '老花色':'#FDF5E6',
    '浅黄色':'#F5DEB3',
    '鹿皮色':'#FFE4B5',
    '橙色':'#FFA500',
    '番木色':'#FFEFD5',
    '白杏色':'#FFEBCD',
    '纳瓦白':'#FFDEAD',
    '古董白':'#FAEBD7',
    '茶色':'#D2B48C',
    '硬木色':'#DEB887',
    '陶坯黄':'#FFE4C4',
    '深橙色':'#FF8C00',
    '亚麻布':'#FAF0E6',
    '秘鲁色':'#CD853F',
    '桃肉色':'#FFDAB9',
    '沙棕色':'#F4A460',
    '巧克力色':'#D2691E',
    '重褐色':'#8B4513',
    '海贝壳':'#FFF5EE',
    '黄土赭色':'#A0522D',
    '浅鲑鱼肉色':'#FFA07A',
    '珊瑚':'#FF7F50',
    '橙红色':'#FF4500',
    '深鲜肉':'#E9967A',
    '番茄红':'#FF6347',
    '浅玫瑰色':'#FFE4E1',
    '鲜肉':'#FA8072',
    '雪白色':'#FFFAFA',
    '淡珊瑚色':'#F08080',
    '玫瑰棕色':'#BC8F8F',
    '印度红':'#CD5C5C',
    '纯红':'#FF0000',
    '棕色':'#A52A2A',
    '火砖色':'#B22222',
    '深红色':'#8B0000',
    '栗色':'#800000',
    '纯白':'#FFFFFF',
    '白烟':'#F5F5F5',
    '淡灰色':'#DCDCDC',
    '浅灰色':'#D3D3D3',
    '银灰色':'#C0C0C0',
    '深灰色':'#A9A9A9',
    '灰色':'#808080',
    '暗淡灰':'#696969',
    '纯黑':'#000000'
    }

class Ball():
    '''
    定义小球
    '''
    def __init__(self,canvas,x= 100,y=250,r=30,color='blue'):
        '''
        参数说明:
        画布  canvas
        中心点[x,y] 
        半径 r
        小球颜色 color 
        '''
        # 保存画板
        self.canvas=canvas
        # 保存小球颜色
        self.color =color
        # 保存中心点坐标
        self._x= x
        self._y= y
        # 保存半径
        self._r= r
        # 随机生成XY方向的步长 _dx _dy
        ss = [-5,-3,-1,1,3,5]
        s = random.choices(ss,k=2)
        #print (s)
        self._dx=s[0]   #random.choice(ss) # random.randint(-5,5)
        self._dy=s[1] #random.choice(ss) # random.randint(-5,5)
        #print ('self._dx,self._dy',self._dx,self._dy)

        # 获取画布的宽高
        self.width =  self.canvas.winfo_width()
        self.height=  self.canvas.winfo_height()
        # 绘制小球
        self.id = self.canvas.create_oval(self._x-r,self._y-r
            ,self._x+r,self._y+r,fill= self.color)        

    def draw(self):
        self.canvas.moveto(self.id,self._x-self._r,self._y-self._r)
        
    def go(self):
        '''
        小球随机运动
        '''
        #计算新的中心点坐标 和  X Y方向的步长
        #计算新的中心点 X 坐标
        self._x += self._dx
        # 如果 已经到达 右边 
        if (self._x+self._r >self.width):
            self._x = self.width -self._r
            # X方向的步长值 为原值的相反  ？？思考
            self._dx =(-1)*self._dx
        # 如果 已经到达 左边 
        if (self._x-self._r <0):
            self._x = self._r
            self._dx =(-1)*self._dx    

        #计算新的中心点 Y 坐标
        self._y += self._dy
        # 如果 已经到达 底边 
        if (self._y+self._r >self.height):
            self._y = self.height -self._r
            # X方向的步长值 为原值的相反  ？？思考
            self._dy =(-1)*self._dy
        # 如果 已经到达 顶边 
        if (self._y-self._r <0):
            self._y = self._r
            self._dy =(-1)*self._dy    

        self.draw()        
        
win = Tk()
win.geometry('600x400+100+100')

mycanvas = Canvas(win,width = 300,height =200,bg = 'yellow')
mycanvas.pack(padx = 0,fill = 'both',expand = True)
win.update()

#从CColors随机选择十种颜色
#print (list(CColors.keys()))
colors = random.choices(list(CColors.keys()),k=10)
#print (colors)
#生成十种颜色的小球
balls = []
for color in colors:
    #print (i)
    #ball = Ball(mycanvas,x= 100,y=250,r=30,color = CColors[color] )
    #随机的中心位置和半径
    ball = Ball(mycanvas,x= random.randint (50,550) ,y=random.randint (50,350)
        , r=random.randint (20,50),color = CColors[color] )
    balls.append(ball)

#ball2 = Ball(mycanvas,x= 200,y=150,r=35,color = 'yellow')
win.update()

#让十个小球随机运动
while True:
    for ball in balls:
        ball.go()
    #测试 有没有 win.update() 语句 的不同效果
    win.update()
    time.sleep(0.05)

win.mainloop()
 