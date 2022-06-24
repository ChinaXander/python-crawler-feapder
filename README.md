# python-crawler-feapder

> feapder 框架 tools

> http://feapder.com/

#### 环境

> python = 3.10

#### 包

`pip install feapder==1.7.4`

`pip install webdriver-manager==3.5.4`

`pip install filetype`

#### feader常用命令

> 安装 通用版 `pip3 install feapder` 完整版 `pip3 install feapder[all]`

> 创建项目 `feapder create -p <project_name>`

- items： 文件夹存放与数据库表映射的item
- spiders： 文件夹存放爬虫脚本
- main.py： 运行入口
- setting.py： 爬虫配置文件

> 创建轻量爬虫 `feapder create -s <spider_name>`

> 创建分布式爬虫 `feapder create -s <spider_name> 2`

> 创建批次爬虫 `feapder create -s <spider_name> 3`

> 创建 item `feapder create -i <item_name>`

## 项目架构

- items： 文件夹存放与数据库表映射的item
- spiders： 文件夹存放爬虫脚本
-
    - my_air_spider 轻量爬虫——示例
    - my_spider 分布式爬虫——示例
    - my_batch_spider 批次爬虫——示例
    - temp_task 批次爬虫——实操 通过公司名称到爱企查查询对应pid
- tools： 文件夹存放常用工具类
- log： 文件夹存放日志
- download： 文件夹存下载文件
- main.py： 运行入口
- setting.py： 爬虫配置文件