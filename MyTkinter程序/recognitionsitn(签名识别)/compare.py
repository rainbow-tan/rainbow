# 系统环境搭建配置参考文件【python + opencv的安装及配置】
# 思路：计算A图特征；计算B[i]图特征；计算A<-B[i]的特征匹配,匹配数为A的特征数；
#      计算A<-B[i]所有特征点距离总数，距离最小者即为最佳匹配
# 将A图、B[i]图全部放同一目录，用户输入其中一个，用这个与其它进行匹配
import os

import cv2


def function1(imgPath='images', imag='b.jpg'):
    imgPath = os.path.abspath(imgPath)
    name_list = os.listdir(imgPath)  # 获取所有图片名（不含路径，但含后缀名）
    print("全部签名图片:")
    for n in name_list:
        print(n, end=",  ")
    name_list.remove(imag)  # 文件列表中删除用户输入的要签订文件名，剩下全部为待匹配的文件名

    # 循环体内变量外置，以提高运行效率
    bf = cv2.BFMatcher()  # 生成匹配器实例
    sift = cv2.xfeatures2d.SIFT_create()  # 生成SIFT算法实例

    # 读入目标图像并计算关键点和描述符
    imgname1 = imgPath + '/' + imag  # 需要查询的目标图像
    img1 = cv2.imread(imgname1)
    kp1, des1 = sift.detectAndCompute(img1, None)  # 求查询图关键点和关键点描述符

    # 开始循环处理目录下所有图片
    allMatchDist = []  # 存放每个待检图像的匹配距离总和
    for sname in name_list:
        imgname2 = imgPath + '/' + sname
        img2 = cv2.imread(imgname2)
        kp2, des2 = sift.detectAndCompute(img2, None)  # 求待检图关键点和关键点描述符
        match = bf.knnMatch(des1, des2, k=1)  # 对每个des1返回des2中最符合的1个匹配描述符，总数等于des1总数
        distSum = 0
        for m in match:
            distSum = distSum + m[0].distance  # 因为K=1，返回一个值，所以m[0]
        allMatchDist.append([sname, round(distSum, 2)])  # distSum保留2位小数

    allMatchDist = sorted(allMatchDist, key=lambda x: x[1])  # 列表按照distSum排序,最小在前
    string = ''
    for m in allMatchDist:
        print("[", m[0], ":", m[1], end="]")
        string += '"[", m[0], ":", m[1], end="]"'
    print("\n经匹配：", imag, "与", allMatchDist[0][0], "笔迹较吻合！（数字越小越吻合）")
    string += '"\n经匹配：", imag, "与", allMatchDist[0][0], "笔迹较吻合！（数字越小越吻合）"'
    return string


def function2(imgPath='images', imag='b.jpg'):
    imgPath = os.path.abspath(imgPath)
    name_list = os.listdir(imgPath)  # 获取所有图片名（不含路径，但含后缀名）
    print("全部签名图片:")
    for n in name_list:
        print(n, end=",  ")
    name_list.remove(imag)  # 文件列表中删除用户输入的要签订文件名，剩下全部为待匹配的文件名

    # 循环体内变量外置，以提高运行效率
    bf = cv2.BFMatcher()  # 生成匹配器实例
    sift = cv2.SIFT_create()  # 生成SIFT算法实例

    # 读入目标图像并计算关键点和描述符
    imgname1 = imgPath + '/' + imag  # 需要查询的目标图像
    img1 = cv2.imread(imgname1)
    kp1, des1 = sift.detectAndCompute(img1, None)  # 求查询图关键点和关键点描述符

    # 开始循环处理目录下所有图片
    allMatchDist = []  # 存放每个待检图像的匹配距离总和
    for sname in name_list:
        imgname2 = imgPath + '/' + sname
        img2 = cv2.imread(imgname2)
        kp2, des2 = sift.detectAndCompute(img2, None)  # 求待检图关键点和关键点描述符
        match = bf.knnMatch(des1, des2, k=1)  # 对每个des1返回des2中最符合的1个匹配描述符，总数等于des1总数
        distSum = 0
        for m in match:
            distSum = distSum + m[0].distance  # 因为K=1，返回一个值，所以m[0]
        allMatchDist.append([sname, round(distSum, 2)])  # distSum保留2位小数

    allMatchDist = sorted(allMatchDist, key=lambda x: x[1])  # 列表按照distSum排序,最小在前
    string = ''
    for i, m in enumerate(allMatchDist):
        msg = '[{}:{}]'.format(m[0], m[1])
        print(msg)
        string += msg
    msg1 = '\n匹配结果为:{}与{}笔迹较吻合,(数字越小越吻合)'.format(imag, allMatchDist[0][0])
    print("\n经匹配：", imag, "与", allMatchDist[0][0], "笔迹较吻合！（数字越小越吻合）")
    string += msg1
    return string


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    function2()
