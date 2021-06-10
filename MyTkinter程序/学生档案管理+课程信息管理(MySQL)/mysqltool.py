# -*- encoding=utf-8 -*-

import pymysql


def connect(host,  # 机器IP
            port,  # 端口
            user,  # 用户名
            password,  # 密码
            database,  # 数据库名称
            charset  # 数据库编码
            ):
    conn = None
    try:
        conn = pymysql.connect(host=host, port=port, user=user, password=password,
                               database=database, charset=charset)
        print('Successful connect database, host({}), port({}), database({})'.format(host, port,
                                                                                     database))
    except Exception as e:
        msg = 'Failed to connect database, host({}), port({}), user({}), database({}), ' \
              'charset({}), exception({})'.format(host, port, user, database, charset, e)
        print(msg)
    return conn


def disconnect(conn):
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
        if conn:
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
        if conn:
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
        print('Successful update,table({}), data({}), conditions({})'.format(table_name,
                                                                             update_data,
                                                                             update_conditions))
    except Exception as e:
        if conn:
            conn.rollback()
        success = False
        msg = 'Failed to update, exception({})'.format(e)
        print(msg)
    return success, msg


def create_table_useraccount(conn):  # 创建用户账号表
    table_name = 'useraccount'
    drop_table_sql = f'drop table if exists {table_name}'
    create_table_sql = f"""
    CREATE TABLE IF NOT EXISTS `{table_name}` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account` varchar(16) DEFAULT NULL,
  `password` varchar(16) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `ip` varchar(15) DEFAULT NULL,
  `visitdate` datetime DEFAULT NULL,
  `exitdate` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """
    cursor = conn.cursor()
    cursor.execute(drop_table_sql)
    cursor.execute(create_table_sql)
    cursor.close()


def create_table_userhistory(conn):  # 创建用户访问历史表
    table_name = 'userhistory'
    drop_table_sql = f'drop table if exists {table_name}'
    create_table_sql = f"""
   CREATE TABLE IF NOT EXISTS `{table_name}` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account` varchar(16) DEFAULT NULL,
  `ip` varchar(15) DEFAULT NULL,
  `visitdate` datetime DEFAULT NULL,
  `exitdate` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """
    cursor = conn.cursor()
    cursor.execute(drop_table_sql)
    cursor.execute(create_table_sql)
    cursor.close()


def create_table_studentrecord(conn):  # 创建学生档案表
    table_name = 'studentrecord'
    drop_table_sql = f'drop table if exists {table_name}'
    create_table_sql = f"""
  CREATE TABLE IF NOT EXISTS `{table_name}` (
  `id` int(11) NOT NULL,
  `name` varchar(10) NOT NULL,
  `sex` varchar(2) DEFAULT NULL,
  `classcode` int(11) DEFAULT NULL,
  `idcard` varchar(20) DEFAULT NULL,
  `birthday` varchar(20) DEFAULT NULL,
  `ethnic` varchar(20) DEFAULT NULL,
  `native` varchar(30) DEFAULT NULL,
  `politicsstatus` varchar(30) DEFAULT NULL,
  `culturelevel` varchar(20) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `postcode` varchar(10) DEFAULT NULL,
  `hometelephone` varchar(20) DEFAULT NULL,
  `height` varchar(10) DEFAULT NULL,
  `weight` varchar(10) DEFAULT NULL,
  `bloodtype` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """
    cursor = conn.cursor()
    cursor.execute(drop_table_sql)
    cursor.execute(create_table_sql)
    cursor.close()


def create_table_studentphoto(conn):  # 创建学生图片表
    table_name = 'studentphoto'
    drop_table_sql = f'drop table if exists {table_name}'
    create_table_sql = f"""
 CREATE TABLE IF NOT EXISTS `{table_name}` (
  `id` int(11) NOT NULL,
  `image` mediumblob,
  `updatetime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """
    cursor = conn.cursor()
    cursor.execute(drop_table_sql)
    cursor.execute(create_table_sql)
    cursor.close()


def create_table_course(conn):  # 创建课程表
    table_name = 'course'
    drop_table_sql = f'drop table if exists {table_name}'
    create_table_sql = f"""
 CREATE TABLE IF NOT EXISTS `{table_name}` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `courseunits` varchar(20) DEFAULT NULL,
  `coursename` varchar(40) DEFAULT NULL,
  `coursecode` varchar(20) NOT NULL,
  `coursenature` varchar(10) DEFAULT NULL,
  `coursecredit` float DEFAULT NULL,
  `courseabstract` varchar(38) DEFAULT NULL,
  `courseguide` varchar(100) DEFAULT NULL,
  `appraisalcategory` varchar(10) DEFAULT NULL,
  `classhour` int(11) DEFAULT NULL,
  `teachtype` varchar(20) DEFAULT NULL,
  `evaluationmode` varchar(10) DEFAULT NULL,
  `englishname` varchar(50) DEFAULT NULL,
  `computerhour` int(11) DEFAULT NULL,
  `practicehour` int(11) DEFAULT NULL,
  `theoryhout` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """
    cursor = conn.cursor()
    cursor.execute(drop_table_sql)
    cursor.execute(create_table_sql)
    cursor.close()


def create_tables():  # 创建所有的表
    global conn_db
    create_table_useraccount(conn_db)
    create_table_userhistory(conn_db)
    create_table_studentrecord(conn_db)
    create_table_studentphoto(conn_db)
    create_table_course(conn_db)


conn_db = connect('127.0.0.1', 3306, 'admin', 'admin', 'mydata', 'utf8')
if __name__ == '__main__':
    create_tables()
