# -*- encoding=utf-8 -*-

import pymysql


def connect(host='127.0.0.1',  # 机器IP
            port=3306,  # 端口
            user='admin',  # 用户名
            password='admin',  # 密码
            database='mydatabase1',  # 数据库名称
            charset='utf8'  # 数据库编码
            ):
    conn = None
    try:
        conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database, charset=charset)
        print('Successful connect database, host({}), port({}), database({})'.format(host, port, database))
    except Exception as e:
        msg = 'Failed to connect database, host({}), port({}), user({}), database({}), ' \
              'charset({}), exception({})'.format(host, port, user, database, charset, e)
        print(msg)
    return conn


def close(conn):
    try:
        conn.close()
        print('Successful close connection')
    except Exception as e:
        msg = 'Failed to close connection, exception({})'.format(e)
        print(msg)


def select(conn, table_name, select_fields, select_conditions, typeof=pymysql.cursors.DictCursor):
    """
    :param conn:
    :param table_name:表名
    :param select_fields: 列表 ['name','age']
    :param select_conditions: 字典 dict(name='盖聂',age='23')
    :param typeof: 返回形式 Cursor | DictCursor
    :return:
    """
    results = []
    msg = ''
    fields = ','.join(select_fields)
    sql = 'SELECT {} FROM {}'.format(fields, table_name)
    keys = list(select_conditions.keys())
    values = list(select_conditions.values())
    sql += where_conditions(keys)
    print('sql语句:{}'.format(sql))
    try:
        with conn.cursor(typeof) as cursor:
            cursor.execute(sql, values)
            results = cursor.fetchall()
    except Exception as e:
        msg = 'Failed to query database, exception({})'.format(e)
        print(msg)
    return results, msg


def join_keys(keys, placeholder=None, separator=','):
    keys = list(map(lambda x: str(x), keys))
    new = ''
    for key in keys:
        if placeholder:
            new += placeholder
        else:
            new += str(key)
        if not key == keys[-1]:
            new += separator
    return new


def insert(conn, table_name, insert_data):
    """
    :param conn:
    :param table_name:
    :param insert_data: dict(name='盖聂',age='22')
    :return:
    """
    success = True
    msg = ''
    keys = list(insert_data.keys())
    values = list(insert_data.values())
    fields = join_keys(keys, None, ',')
    placeholder = join_keys(keys, '%s', ',')
    sql = 'INSERT INTO {}({}) VALUES({})'.format(table_name, fields, placeholder)
    print('sql语句:{}'.format(sql))
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, values)
        conn.commit()
        print('Successful insert,table({}), data({})'.format(table_name, insert_data))
    except Exception as e:
        conn.rollback()
        success = False
        msg = 'Failed to insert data, exception({})'.format(e)
        print(msg)
    return success, msg


def where_conditions(keys):
    conditions = ''
    string = ''
    if keys:
        for key in keys:
            string += str(key) + '=%s and '
        if string.endswith('and '):
            string = string[0:len(string) - 5]
        conditions = ' WHERE {}'.format(string)
    return conditions


def delete(conn, table_name, delete_conditions):
    success = True
    msg = ''
    sql = 'DELETE FROM {}'.format(table_name)
    keys = list(delete_conditions.keys())
    values = list(delete_conditions.values())
    sql += where_conditions(keys)
    print('sql语句:{}'.format(sql))
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, values)
        conn.commit()
        print('Successful delete, table({}), conditions({})'.format(table_name, delete_conditions))
    except Exception as e:
        conn.rollback()
        success = False
        msg = 'Failed to delete, exception({})'.format(e)
        print(msg)
    return success, msg


def update(conn, table_name, update_data, update_conditions):
    """
    :param conn:
    :param table_name: 
    :param update_data: 字典
    :param update_conditions: 字典
    :return: 
    """
    success = True
    msg = ''
    keys = list(update_data.keys())
    values = list(update_data.values()) + list(update_conditions.values())
    string = ''
    for key in keys:
        string += str(key) + '=%s,'
    if string.endswith(','):
        string = string[0:len(string) - 1]
    sql = 'UPDATE {} SET {}'.format(table_name, string)
    sql += where_conditions(list(update_conditions.keys()))
    print('sql语句:{}'.format(sql))
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql, values)
        conn.commit()
        print(
            'Successful update,table({}), data({}), conditions({})'.format(table_name, update_data, update_conditions))
    except Exception as e:
        conn.rollback()
        success = False
        msg = 'Failed to update, exception({})'.format(e)
        print(msg)
    return success, msg


if __name__ == '__main__':
    db = connect()
    insert(db, 'demo', dict(name='盖聂', age=20))
    print(select(db, 'demo', ['name', 'age'], dict(name='盖聂')))
    delete(db, 'demo', dict())
    update(db, 'demo', {'name': '小红', 'age': '100'}, {'age': '23'})
    close(db)
