# 爬虫文档

## 调研

## 数据库设计

```
CREATE TABLE `test_temp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_croatian_ci DEFAULT NULL,
  `pid_state` tinyint(4) NOT NULL DEFAULT '0' COMMENT '0 待抓取，1抓取完毕，2抓取中，-1抓取失败',
  `pid` varchar(255) COLLATE utf8mb4_croatian_ci DEFAULT NULL,
  `content_state` tinyint(4) NOT NULL DEFAULT '0',
  `content` varchar(255) COLLATE utf8mb4_croatian_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=1441 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_croatian_ci;
```

## 爬虫逻辑

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