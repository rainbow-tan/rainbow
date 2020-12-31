# -*- encoding=utf-8 -*-
import os

NUMBER = 'number'
TITLE = 'title'
STATUS = 'status'
CLICK_COUNT = 'click_count'
MESSAGE = 'message'

news = {}
alert_info = '''1------->添加新闻
2------->浏览新闻
3------->发布新闻
4------->撤销已发布新闻
5------->删除新闻
0------->退出'''


def select_one(number):
    print('========具体新闻信息========')
    if number not in news:
        print('新闻编号错误')
    else:
        one_news = news[number]
        print('编号:{}'.format(one_news[NUMBER]))
        print('标题:{}'.format(one_news[TITLE]))
        print('状态:{}'.format(one_news[STATUS]))
        print('点击数:{}'.format(one_news[CLICK_COUNT]))
        print('内容:{}'.format(one_news[MESSAGE]))
        news[number][CLICK_COUNT] = int(news[number][CLICK_COUNT]) + 1
    print('========具体新闻信息========')


def writefile(filename='news.txt'):
    path = os.path.dirname(filename)
    if path != '' and not os.path.exists(path):
        os.makedirs(path)
    with open(filename, 'w') as f:
        for one_news in news.values():
            f.write(one_news[NUMBER] + '\n')
            f.write(one_news[TITLE] + '\n')
            f.write(one_news[STATUS] + '\n')
            f.write(one_news[CLICK_COUNT] + '\n')
            f.write(one_news[MESSAGE] + '\n')
            f.write('==================\n')
    print('保存数据成功！')
    print('数据文件目录:{}'.format(os.path.abspath(filename)))


def delete(number):
    print('========删除新闻========')
    if number not in news:
        print('新闻编号错误')
    else:
        news.pop(number)
        print('删除成功')
    print('========删除新闻========')


def publish(number):
    print('========发布新闻========')

    if number not in news:
        print('新闻编号错误')
    else:
        news[number][STATUS] = '发布'
        print('发布成功')
    print('========发布新闻========')


def unpublish(number):
    print('========撤销已发布新闻========')

    if number not in news:
        print('新闻编号错误')
    else:
        news[number][STATUS] = '未发布'
        print('撤销成功')

    print('========撤销已发布新闻========')


def select_news(scope='all'):
    if scope.lower() == 'all':
        print('========所有新闻信息========')

        for index, one_news in enumerate(news.values()):

            print('编号:{}'.format(one_news[NUMBER]))
            print('标题:{}'.format(one_news[TITLE]))
            print('状态:{}'.format(one_news[STATUS]))
            print('点击数:{}'.format(one_news[CLICK_COUNT]))
            print('内容:{}'.format(one_news[MESSAGE]))
            if index != len(news.values()) - 1:
                print('------------')
        print('========所有新闻信息========')
    elif scope.lower() == 'online':
        print('========已发布新闻========')
        for index, one_news in enumerate(news.values()):
            if one_news[STATUS] == '发布':
                print('编号:{}'.format(one_news[NUMBER]))
                print('标题:{}'.format(one_news[TITLE]))
                print('状态:{}'.format(one_news[STATUS]))
                print('点击数:{}'.format(one_news[CLICK_COUNT]))
                print('内容:{}'.format(one_news[MESSAGE]))
                print('------------')
        print('========已发布新闻========')

    elif scope.lower() == 'offline':
        print('========未发布新闻========')

        for index, one_news in enumerate(news.values()):
            if one_news[STATUS] == '未发布':
                print('编号:{}'.format(one_news[NUMBER]))
                print('标题:{}'.format(one_news[TITLE]))
                print('状态:{}'.format(one_news[STATUS]))
                print('点击数:{}'.format(one_news[CLICK_COUNT]))
                print('内容:{}'.format(one_news[MESSAGE]))
                print('------------')
        print('========未发布新闻========')

    else:
        print('参数scope应该为all或online或offline')


def add(number, title, message, status, click_count):
    print('========添加新闻========')

    one_news = {NUMBER: number, TITLE: title, MESSAGE: message, STATUS: status,
                CLICK_COUNT: click_count}
    can_add = True
    if number in news:
        can_add = False
        print('编号已经存在,添加失败')
    if status not in ['发布', '未发布']:
        print('状态需要为发布或未发布,添加失败')
        can_add = False
    if can_add:
        news[number] = one_news
        print('添加成功')
    print('========添加新闻========')
    return can_add


def manager():
    while True:
        print('=======欢迎使用新闻管理系统=======')
        print(alert_info)
        print('===============================')
        choose = input('请输入您的选择:')
        if choose == '1':
            while True:
                number = input('请输入新闻编号:')
                title = input('请输入新闻标题:')
                message = input('请输入新闻内容:')
                status = '未发布'
                click_count = '0'
                add(number, title, message, status, click_count)
                goon = input('是否继续添加？y/n:')
                if goon.lower() == 'n':
                    writefile('news.txt')
                    break
        elif choose == '2':
            scope = input('请输入查看的范围:1->所有,2->已发布,3->未发布,4->具体查看:')
            if scope == '1':
                select_news('all')
            elif scope == '2':
                select_news('online')
            elif scope == '3':
                select_news('offline')
            elif scope == '4':
                select_one(input('请输入想查看的编号:'))
            else:
                print('输入错误')
        elif choose == '3':
            select_news('offline')
            publish(input('请输入需要发布的新闻编号:'))
        elif choose == '4':
            select_news('online')
            unpublish(input('请输入需要撤销发布的新闻编号:'))
        elif choose == '5':
            select_news('all')
            delete(input('请输入需要删除的新闻编号:'))
        elif choose == '0':
            print('谢谢使用,下次再会')
            break
        else:
            print('输入错误，输入应该为0-5')


if __name__ == '__main__':
    manager()
