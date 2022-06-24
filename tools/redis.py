# -*- coding: utf-8 -*-
"""
@Time           :2022/5/24
@author         :XDS
@Description    :
"""
from feapder.utils.tools import *

redisDb = None

redisDataType = {
    # 0-列表 1-集合 2-有序集合 3-哈希
    'count': ['lget_count', 'sget_count', 'zget_count', 'hget_count']
}


def redis_get_connect(link=None, refresh=False):
    global redisDb
    """
    redis 链接
    :param link: redis://@192.168.0.224:6379/10  [redis://[[username]:[password]]@[host]:[port]/[db]]
    :return:redis
    """
    if not redisDb or refresh is True:
        if link:
            redisDb = RedisDB().from_url(link)
        else:
            redisDb = RedisDB()
    return redisDb


def redis_count(key, redis_type=0, link=None):
    """
    数量查询
    :param key:
    :param redis_type:存储类型 0-列表 1-集合 2-有序集合 3-哈希
    :param link:
    :return:
    """
    global redisDataType
    return getattr(redis_get_connect(link), redisDataType['count'][redis_type])(key)
