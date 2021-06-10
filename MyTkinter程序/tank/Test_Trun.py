from enum import Enum
import random


class Turn(Enum):
    '''
    转向
    '''
    Forward = 0
    Left = 1
    Right = 2
    Backward = 3

    # 实现静态方法 外部调用
    @staticmethod
    def RandTurn():
        '''
        随机转向
        例: RandTurn 
        Forward     向前  概率 75%
        Left        向左  概率 10%
        Right       向右  概率 10%
        Backward    向后  概率 5%
        '''

        rand = random.randint(0, 100)
        if (rand < 75):
            return Turn.Forward  # 向前  概率 75%
        elif (rand >= 75 and rand < 85):
            return Turn.Left  # 向左  概率 10%
        elif (rand >= 85 and rand < 95):
            return Turn.Right  # 向右  概率 10%
        elif (rand >= 95):
            return Turn.Backward  # 向后  概率 5%


class Direct(Enum):
    '''
    方向类
    重写了 __str__ 和 __add__
    通过 + 重载, 实现方向加法
    例: Up + Down = Down, Up+Up = Up 等等
    '''
    '''
    00  -1  00
    -1  me   1
    00   1  00
    '''

    Up = (0, -1)
    Right = (1, 0)
    Down = (0, 1)
    Left = (-1, 0)

    # 实现静态方法 外部调用

    @staticmethod
    def RandDirect():
        '''
        个性化初始化方法  随机获取一个方向
        '''

        d = random.randint(0, 100)
        lst = [x for x in Direct]
        #print (lst[d%4])
        return lst[d % 4]

    # value 可能的数据类型为 Direction、字符串、整形
    def __add__(self, value):
        #print (type(self),type(value))
        if (type(self) == type(value)):
            return value

        if (type(value) == Turn):
            # 向前
            if (value == Turn.Forward):
                return self
            # 左转
            elif (value == Turn.Left):
                if (self == Direct.Up):
                    return Direct.Left
                elif (self == Direct.Right):
                    return Direct.Up
                elif (self == Direct.Down):
                    return Direct.Right
                elif (self == Direct.Left):
                    return Direct.Down
            # 右转
            elif (value == Turn.Right):
                if (self == Direct.Up):
                    return Direct.Right
                elif (self == Direct.Right):
                    return Direct.Down
                elif (self == Direct.Down):
                    return Direct.Left
                elif (self == Direct.Left):
                    return Direct.Up
            # 后转
            elif (value == Turn.Backward):
                if (self == Direct.Up):
                    return Direct.Down
                elif (self == Direct.Right):
                    return Direct.Left
                elif (self == Direct.Down):
                    return Direct.Up
                elif (self == Direct.Left):
                    return Direct.Right


# 转向测试代码
if __name__ == '__main__':
    '''
    dir = Direct.RandDirect()
    index =0
    for turn in Turn:
        for dir in Direct:
        #turn = Turn.RandTurn()
        print('%2d %s + %s = %s '%(index,turn,dir, (turn +dir).name)
        index +=1
    '''

    
    #随机转向测试
    dir = Direct.RandDirect()
    for i in range( 0,100): #  Turn:
        turn = Turn.RandTurn()
        print('%2d %s + %s = %s '%(i,dir, turn,dir+turn))
    

    print ('*'*50)
    for dir in Direct:
        # print (dir.name)
        i = 1
        for turn in Turn:
            print('%d %s + %s = %s '%(i,dir.name, turn.name,(dir+turn).name))
            dir_new =  dir+turn
            print (dir_new)
            i +=1
