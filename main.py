# -*- coding: utf-8 -*-
"""
Created on 2022-05-24 10:24:34
---------
@summary: 爬虫入口
---------
@author: phper
"""

from spiders import *
from feapder import ArgumentParser


def first_spider():
    """
    AirSpider爬虫
    """
    my_air_spider.MyAirSpider().start()
    pass


def second_spider():
    """
    Spider爬虫
    """
    my_spider.MySpider(redis_key="xxx:xxx").start()
    pass


def third_spider(args):
    """
    BatchSpider爬虫
    """
    spider = my_batch_spider.MyBatchSpider(
        task_table="",  # mysql中的任务表
        batch_record_table="",  # mysql中的批次记录表
        batch_name="xxx(周全)",  # 批次名字
        batch_interval=7,  # 批次时间 天为单位 若为小时 可写 1 / 24
        task_keys=["id", "xxx"],  # 需要获取任务表里的字段名，可添加多个
        redis_key="xxx:xxxx",  # redis中存放request等信息的根key
        task_state="state",  # mysql中任务状态字段
    )

    if args == 1:
        spider.start_monitor_task()
    elif args == 2:
        spider.start()
    elif args == 3:
        spider.init_task()


def example_get_pid(args):
    """
    通过公司名称到爱企查列表页查询pid
    :param args:
    :return:
    """
    spider = temp_task.TempTask(
        task_table="test_temp",  # mysql中的任务表
        batch_record_table="test_temp_batch_record",  # mysql中的批次记录表
        batch_name="test_temp_batch",  # 批次名字
        batch_interval=7,  # 批次时间 天为单位 若为小时 可写 1 / 24
        task_keys=["id", "name", "pid"],  # 需要获取任务表里的字段名，可添加多个
        redis_key="getPid",  # redis中存放request等信息的根key
        task_state="pid_state",  # mysql中任务状态字段
        min_task_count=50,  # redis 中最少任务数, 少于这个数量会从mysql的任务表取任务
        task_limit=50,  # 从数据库中取任务的数量
    )

    if args == 1:
        spider.start_monitor_task()
    elif args == 2:
        spider.start()
    pass


if __name__ == "__main__":
    parser = ArgumentParser(description="xxx爬虫")

    parser.add_argument(
        "--first_spider", action="store_true", help="number 1 轻量级爬虫", function=first_spider
    )
    parser.add_argument(
        "--second_spider", action="store_true", help="number 2 分布式爬虫", function=second_spider
    )
    parser.add_argument(
        "--third_spider",
        type=int,
        nargs=1,
        help="number 3 批次爬虫",
        choices=[1, 2, 3],
        function=third_spider,
    )

    parser.add_argument(
        "--example_get_pid",
        type=int,
        nargs=1,
        help="获取公司pid",
        choices=[1, 2, 3],
        function=example_get_pid,
    )

    parser.start()

    # main.py作为爬虫启动的统一入口，提供命令行的方式启动多个爬虫，若只有一个爬虫，可不编写main.py
    # 将上面的xxx修改为自己实际的爬虫名
    # 查看运行命令 python main.py --help
    # AirSpider与Spider爬虫运行方式 python main.py --crawl_xxx
    # BatchSpider运行方式
    # 1. 下发任务：python main.py --crawl_xxx 1
    # 2. 采集：python main.py --crawl_xxx 2
    # 3. 重置任务：python main.py --crawl_xxx 3
