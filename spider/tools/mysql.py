# -*- coding: utf-8 -*-
"""
@Time           :2022/5/24
@author         :XDS
@Description    :
"""
from feapder.utils.tools import *
from feapder.db.mysqldb import MysqlDB

mysqlDb = None


def mysql_get_detail(table, where=None, field='*', limit=0, link=None):
    """
    数据查询
    :param link:
    :param limit:查询条数，默认全部
    :param field:查询字段，默认全部
    :param where:查询条件，默认无条件
    :param table:查询表名
    :return:dict|list
    """
    sql = f"SELECT {field} FROM `{table}`"

    if where:
        sql += f" WHERE {where}"

    lists = mysql_get_connect(link).find(sql, limit)
    return mysql_data_format(lists, table)


def mysql_get_connect(link=None, refresh=False):
    global mysqlDb
    """
    mysql 链接
    :param link: mysql://root:mysql@127.0.0.1:3306/my_db?charset=utf8mb4 [mysql://username:password@ip:port/db?charset=utf8mb4]
    :return:mysql
    """
    if not mysqlDb or refresh is True:
        if link:
            mysqlDb = MysqlDB().from_url(link)
        else:
            mysqlDb = MysqlDB()

    return mysqlDb


def mysql_get_field_name(table, link=None) -> list:
    """
    查询表字段
    :param link:
    :param table: 表名
    :return: list
    """
    table_field = []

    sql = f"SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE table_name = '{table}'"
    data = mysql_get_connect(link).find(sql)
    for value in data:
        table_field.append(value[0])

    return table_field


def mysql_data_format(lists, table):
    """
    数据格式化
    :param lists: [('value1','value2'...)] or  ('value1','value2'...)
    :param table: 表名
    :return: [{'field_name1':'value1','field_name2':'value2'...}] or {'field_name1':'value1','field_name2':'value2'...}
    """
    lists_format = []
    dicta = dict()
    if lists:

        table_field = mysql_get_field_name(table)
        if isinstance(lists, list):

            for value in lists:
                dicta = dict()

                for i in range(0, len(table_field)):
                    dicta[table_field[i]] = value[i]

        elif isinstance(lists, tuple):

            for i in range(0, len(table_field)):
                dicta[table_field[i]] = lists[i]

        lists_format.append(dicta)
    return lists_format
