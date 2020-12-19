# coding:utf-8
import MySQLdb

db = MySQLdb.connect("localhost", "admin", "admin", "storemanagement", charset='utf8')


def select_all(db, table):
    data = []
    sql = 'select * from {}'.format(table)
    cursor = db.cursor()
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        # print(row)
        data.append(row)
    # print(data)
    return data


def insert_user(db, user, pwd):
    flag = True
    cursor = db.cursor()

    # SQL 插入语句
    sql = "INSERT INTO user VALUES ('{}','{}')".format(user, pwd)
    # print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        # print('OK!!!!')
    except Exception as e:
        # 发生错误时回滚
        db.rollback()
        flag = False
        # print('Fail:{}'.format(e))
    return flag


def select_one(db, table, name):
    data = []
    sql = 'select {} from {}'.format(name, table)
    cursor = db.cursor()
    print(sql)
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        # print(row)
        data.append(row[0])
    print(data)
    return data


def delete_data(db, table, key, value):
    sql = 'delete from {} where {}={}'.format(table, key, value)
    print(sql)
    cursor = db.cursor()
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        db.commit()
        print('OK')
    except:
        # 发生错误时回滚
        print('Fali')
        db.rollback()


if __name__ == '__main__':
    select_one(db, 'cangku', 'mingchen')
    delete_data(db, 'cangku', 'bianhao', '3')
