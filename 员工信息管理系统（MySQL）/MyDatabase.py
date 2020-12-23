# coding:utf-8
import pymysql


def connect_database(ip='localhost', username='admin', password='admin', database='datacenter'):
    my_db = None
    try:
        my_db = pymysql.connect(ip, username, password, database, charset='utf8')
        print('连接数据库成功:{}'.format(my_db))
    except Exception as e:
        print('连接数据库失败:{}'.format(e))
    return my_db


def close_database(my_db):
    try:
        my_db.close()
        print('关闭数据库成功')
    except Exception as e:
        print('关闭数据库失败:{}'.format(e))


def select_database(my_db, table, column_names, data_dict={}):
    data = list()
    info = ','.join(column_names)
    sql = 'select {} from {}'.format(info, table)
    if data_dict:
        option = []
        for key, value in data_dict.items():
            option.append('{}="{}"'.format(key, value))
        option = ' and '.join(option)
        sql += ' where ' + option
    print('查询sql语句:{}'.format(sql))
    try:
        cursor = my_db.cursor()

        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        print('查询完成:{}'.format(results))
        for result in results:
            one_data = dict()
            for index, column_name in enumerate(column_names):
                one_data[column_name] = result[index]
            data.append(one_data)
        # print(data)
        """
        [{'username': 'admin', 'password': 'admin'}, {'username': 'root', 'password': 'root'}]
        """
        my_db.commit()
    except Exception as e:
        my_db.rollback()
        print('查询异常:{}'.format(e))
    return data


def insert_database(my_db, table, data_list_dict):
    # 通过失败的信息来判断是否成功
    success = ''
    for data_dict in data_list_dict:
        key_info = ''
        value_info = ''
        for key, value in data_dict.items():
            key_info += key + ','
            value_info += '"{}",'.format(value)
        key_info = key_info[:len(key_info) - 1]
        value_info = value_info[:len(value_info) - 1]
        sql = 'insert into {}({}) values({})'.format(table, key_info, value_info)
        print('插入sql语句:{}'.format(sql))

        try:
            cursor = my_db.cursor()
            cursor.execute(sql)
            my_db.commit()
            print('插入数据成功')
        except Exception as e:
            my_db.rollback()
            print('插入数据失败:{}'.format(e))
            success += '失败|'
    return success


def update_database(my_db, table, id_name, id_value, data_dict):
    info = list()
    for key, value in data_dict.items():
        info.append('{}="{}"'.format(key, value))
    info = ','.join(info)
    sql = 'update {} set {} where {}="{}"'.format(table, info, id_name, id_value)
    print('修改sql语句:{}'.format(sql))
    try:
        cursor = my_db.cursor()

        cursor.execute(sql)

        my_db.commit()
        print('修改数据成功')
    except Exception as e:

        my_db.rollback()
        print('修改数据失败:{}'.format(e))

    pass


def delete_database_by_keyname(my_db, table, key_name, key_values):
    print(key_values)
    key_values_info = ','.join(key_values)
    sql = 'delete from {} where {} in ({})'.format(table, key_name, key_values_info)
    print('删除sql语句:{}'.format(sql))
    try:
        cursor = my_db.cursor()

        cursor.execute(sql)

        my_db.commit()
        print('删除数据成功')
    except Exception as e:

        my_db.rollback()
        print('删除数据失败:{}'.format(e))


db = connect_database()
if __name__ == '__main__':

    select_database(db, 'user', ['username', 'password'])
    a = insert_database(db, 'user',
                        [{'username': "admin", 'password': 'admin'}, {'username': "admin2", 'password': 'admin2'}])

    close_database(db)
    select_database(db, 'employee', ['number', 'name', 'sex', 'hiredate', 'position', 'pay'])
    update_database(db, 'user', 'id', "32", {'username': "1", "password": "2"})
