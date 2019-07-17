# bjzq
搭建分布式爬虫爬取北京证券网全站新闻数据

该项目使用我自己的电脑作为master主机，使用三台虚拟机作为slave从机，搭建分布式，主机只负责维护redis队列和分别配爬去任务，
从机负责爬取数据并保存到mongodb数据库，境内过较长时间运行，该爬虫总共抓取到99813条新闻数据，成功爬取该网站全站数据。

部分settings代码如下：

指定使用scrapy-redis的去重

DUPEFILTER_CLASS = "scrapy_redis.dupefilters.RFPDupeFilter"

指定使用scrapy-redis的调度器

SCHEDULER = "scrapy_redis.scheduler.Scheduler"

允许暂停

SCHEDULER_PERSIST = True

redis数据库连接，该处的redis_host使用自己本机的IP地址

REDIS_HOST = '192.168.0.117'

REDIS_PORT = 6379
