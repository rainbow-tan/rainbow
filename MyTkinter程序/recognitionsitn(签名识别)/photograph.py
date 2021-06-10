import datetime
import os

import cv2


def take_a_picture():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    flag = cap.isOpened()
    name = None
    while flag:
        ret, frame = cap.read()
        cv2.imshow("take a picture", frame)
        k = cv2.waitKey(1) & 0xFF
        if k in [ord('s'), ord('S')]:  # 按下s键，进入下面的保存图片操作
            now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            name = "images/image{}.jpg".format(now)
            name = os.path.abspath(name)
            if not os.path.exists(os.path.dirname(name)):
                os.makedirs(os.path.dirname(name))
            cv2.imwrite(name, frame)
            print('save path:{}'.format(name))
            print('patho width:{}'.format(cap.get(3)))
            print('photo height:{}'.format(cap.get(4)))
            break
        elif k in [ord('q'), ord('Q')]:  # 按下q键，程序退出
            break
        else:
            pass
    cap.release()
    cv2.destroyAllWindows()
    return name


if __name__ == '__main__':
    print(take_a_picture())
