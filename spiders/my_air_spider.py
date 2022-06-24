# -*- coding: utf-8 -*-
"""
Created on 2022-05-24 10:40:16
---------
@summary:
---------
@author: phper
"""

import feapder


class MyAirSpider(feapder.AirSpider):
    def start_requests(self):
        yield feapder.Request("https://spidertools.cn")

    def parse(self, request, response):
        # 提取网站title
        print(response.xpath("//title/text()").extract_first())
        # 提取网站描述
        print(response.xpath("//meta[@name='description']/@content").extract_first())
        print("网站地址: ", response.url)
