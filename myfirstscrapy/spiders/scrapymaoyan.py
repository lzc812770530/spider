# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule,CrawlSpider
from myfirstscrapy.items import MyfirstscrapyItem
import time
import random



class ScrapymaoyanSpider(CrawlSpider):
    name = 'scrapymaoyan'
    allowed_domains = ['maoyan.com/board/4']
    start_urls = ["http://maoyan.com/board/4"]
    for i in range(10):
         seed_urls = 'http://maoyan.com/board/4?offset={}'.format(str(i*10))
         start_urls.append(seed_urls)
    time.sleep(random.randint(1,3))
    pagelink = LinkExtractor(allow=("\?offset=\d+"))

    rules = [
        Rule(pagelink,callback='parse',follow=True)
    ]




    def parse(self, response):
        for each in response.xpath("//div[@class='content']"):
            for i in range(1,11):
                item = MyfirstscrapyItem()
                item['title'] = each.xpath("./div/div[1]/dl/dd[{}]/div/div/div[1]/p[1]/a/text()".format(str(i))).extract()[0]
                item['stars'] = each.xpath("./div/div[1]/dl/dd[{}]/div/div/div[1]/p[2]/text()".format(str(i))).extract()[0]
                item['releasetime'] = each.xpath("./div/div[1]/dl/dd[{}]/div/div/div[1]/p[3]/text()".format(str(i))).extract()[0]
                yield item
