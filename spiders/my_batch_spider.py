# -*- coding: utf-8 -*-
"""
Created on 2022-05-24 10:41:24
---------
@summary:
---------
@author: phper
"""

import feapder


class MyBatchSpider(feapder.BatchSpider):
    # 自定义数据库，若项目中有setting.py文件，此自定义可删除
    __custom_setting__ = dict(
        REDISDB_IP_PORTS="localhost:6379",
        REDISDB_USER_PASS="",
        REDISDB_DB=0,
        MYSQL_IP="localhost",
        MYSQL_PORT=3306,
        MYSQL_DB="feapder",
        MYSQL_USER_NAME="feapder",
        MYSQL_USER_PASS="feapder123",
    )

    def start_requests(self, task):
        yield feapder.Request("https://spidertools.cn")

    def parse(self, request, response):
        # 提取网站title
        print(response.xpath("//title/text()").extract_first())
        # 提取网站描述
        print(response.xpath("//meta[@name='description']/@content").extract_first())
        print("网站地址: ", response.url)
