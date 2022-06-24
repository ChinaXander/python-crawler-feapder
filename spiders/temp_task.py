# -*- coding: utf-8 -*-
"""
Created on 2022-05-25 09:33:58
---------
@summary:
---------
@author: phper
"""

import feapder
import re
from feapder.utils.log import log


class TempTask(feapder.BatchSpider):

    def start_requests(self, task):
        yield feapder.Request(
            f"https://aiqicha.baidu.com/s?q={task['name']}&t=0",
            render=True,
            meta=task,
            render_time=4,
            # proxies={"http": tools.get_proxies()},
        )

    def parse(self, request, response):
        task = request.meta
        title = task['name']
        try:
            pidArr = response.xpath(f'//a[@title="{title}"]//@href').get()

            if pidArr:
                pid = re.split('_', pidArr)[2]

                if pid:
                    log.info(f"url读取成功 ===>>> {title} ===>>> {pid}")
                    yield self.update_task_batch(task['id'], 1, pid=pid)
                    return

            raise Exception('pid获取失败')
        except Exception as e:
            log.error(f"url读取失败 ===>>> {title} ===>>> {e} ")
            yield self.update_task_batch(task['id'], 0)
