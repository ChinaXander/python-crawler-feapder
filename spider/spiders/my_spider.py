# -*- coding: utf-8 -*-
"""
Created on 2022-05-24 10:40:59
---------
@summary:
---------
@author: phper
"""

import feapder


class MySpider(feapder.Spider):
    # 自定义数据库，若项目中有setting.py文件，此自定义可删除
    __custom_setting__ = dict(
        REDISDB_IP_PORTS="localhost:6379", REDISDB_USER_PASS="", REDISDB_DB=0
    )

    def start_requests(self):
        yield feapder.Request("https://spidertools.cn")

    def parse(self, request, response):
        # 提取网站title
        print(response.xpath("//title/text()").extract_first())
        # 提取网站描述
        print(response.xpath("//meta[@name='description']/@content").extract_first())
        print("网站地址: ", response.url)
