# -*- encoding=utf-8 -*-
import os

news_titles = []
news_contents = []
news_states = []  # 1发布0未发布
news_hits = []


def save():
    filename = 'data.txt'
    with open(filename, 'w') as f:
        for index, title in enumerate(news_titles):
            f.write('编号:' + str(index) + '\n')
            f.write('标题:' + title + '\n')
            if news_states[index] == 0:
                f.write('状态:未发布\n')
            else:
                f.write('状态:已发布\n')
            f.write('访问量:' + str(news_hits[index]) + '\n')
            f.write('内容:' + news_contents[index] + '\n')
            f.write('------------------------\n')
    print('保存成功，文件为:{}'.format(os.path.abspath(filename)))


def delete():
    for i, j in enumerate(news_titles):
        print('编号:' + str(i))
        print('标题:' + news_titles[i])
        if news_states[i] == 0:
            print('状态:未发布')
        else:
            print('状态:已发布')
        print('访问量:' + str(news_hits[i]))
        print('内容:' + news_contents[i])
        print('------------------------')
    index = int(input('请选择需要删除的新闻编号:'))
    if 0 <= index < len(news_titles):
        news_titles.pop(index)
        news_contents.pop(index)
        news_states.pop(index)
        news_hits.pop(index)
        print('删除成功且自动调整编号成功')
    else:
        print('新闻编号错误')


def add():
    news_titles.append(input('请输入标题:'))
    news_contents.append(input('请输入内容:'))
    news_states.append(0)
    news_hits.append(0)


def release():
    indexs = []
    for index, state in enumerate(news_states):
        if state == 0:
            indexs.append(index)
            print('编号:' + str(index))
            print('标题:' + news_titles[index])
            print('状态:未发布')
            print('访问量:' + str(news_hits[index]))
            print('内容:' + news_contents[index])
            print('------------------------')
    if not indexs:
        print('所有新闻已发布')
        return
    need_index = int(input('请选择发布的新闻编号:'))
    if need_index in indexs:
        news_states[need_index] = 1
    else:
        print('新闻编号错误')


def backout():
    indexs = []
    for index, state in enumerate(news_states):
        if state == 1:
            indexs.append(index)
            print('编号:' + str(index))
            print('标题:' + news_titles[index])
            print('状态:发布')
            print('访问量:' + str(news_hits[index]))
            print('内容:' + news_contents[index])
            print('------------------------')
    if not indexs:
        print('还没有发布过新闻')
        return
    need_index = int(input('请选择撤销发布的新闻编号:'))
    if need_index in indexs:
        news_states[need_index] = 0
    else:
        print('新闻编号错误')


def see():  # -1查所有
    index = int(input('输入-1查看所有新闻信息,输入编号详细查看某条信息:'))
    if index == -1:
        for i, j in enumerate(news_titles):
            print('编号:' + str(i))
            print('标题:' + news_titles[i])
            if news_states[i] == 0:
                print('状态:未发布')
            else:
                print('状态:已发布')
            print('访问量:' + str(news_hits[i]))
            print('内容:' + news_contents[i])
            print('------------------------')
    else:  # 查详细某一条
        hit_new(index)


def hit_new(index):  # 查详细某一条
    if 0 <= index < len(news_titles):
        print('编号:' + str(index))
        print('标题:' + news_titles[index])
        if news_states[index] == 0:
            print('状态:未发布')
        else:
            print('状态:已发布')
        print('访问量:' + str(news_hits[index]))
        news_hits[index] = news_hits[index] + 1
        print('内容:' + news_contents[index])
    else:
        print('新闻编号错误')
        pass


def goodbye():
    print('谢谢使用,再会')
    exit(0)


do = {1: add, 2: see, 3: release, 4: backout, 5: delete, 6: save, 0: goodbye}
if __name__ == '__main__':
    while True:
        print('欢迎使用新闻管理系统')
        print('(1)添加新闻信息')
        print('(2)浏览新闻信息')
        print('(3)发布新闻信息')
        print('(4)撤销发布新闻信息')
        print('(5)删除新闻信息')
        print('(6)保存新闻信息')
        print('(0)退出新闻信息系统')
        print('------------------------')
        want = int(input('请输入选择:'))
        if want in do:
            do[want]()
        else:
            print('无此选项')
    pass
