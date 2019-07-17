# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
#from bjzq_spider.items import BjzqSpiderItem


class BjzqSpider(CrawlSpider):
    name = 'bjzq'
    allowed_domains = ['bjzq.com.cn']
    start_urls = ['http://www.bjzq.com.cn/']

    rules = (
        Rule(LinkExtractor(allow=r'[a-z]+/ShowClass.asp\?ClassID=\d+'),follow=True),
        Rule(LinkExtractor(allow=r'\?classid=\d+&page=\d+'), follow=True),
        Rule(LinkExtractor(allow=r'[A-Za-z]+/\d{6}/.+.html'), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        #item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        title = response.xpath('//div[@class="article_title"]/text() | //div[@class="titlediv"]/text()').extract_first()
        content = "".join(response.xpath('//div[@class="article_content"]/p/text() | //div[@id="content1"]/p/text() | //div[@id="content2"]/p/text()').extract())
        if response.xpath('//font[@color="#d04935"]/text()').extract():
            author = response.xpath('//font[@color="#d04935"][1]/text()').extract_first()
            time = response.xpath('//font[@color="#d04935"][2]/text()').extract_first()
        else:
            two_msg = response.xpath('//div[@class="article_inf"]/text()').extract_first()
            author = re.search(r'作者：.+',two_msg)[0]
            time = two_msg.split(' ',2)[0]

        yield{
            "title":title,
            "author":author,
            "time":time,
            "content":content
        }
