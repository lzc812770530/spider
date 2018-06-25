# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql


class MyfirstscrapyPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',user='root',
                                    passwd='123456',charset='utf8',
                                    db='maoyan',port=3306)
        self.cur = self.conn.cursor()
        self.l = []
        self.num = 0

    def process_item(self, item, spider):
        data = (str(item['title']),str(item['stars']),str(item['releasetime']))
        self.l.append(data)
        self.num += 1 
        sql = 'insert into maoyan values(%s,%s,%s)'
        if self.num > 10:
            self.cur.executemany(sql, self.l)
            self.conn.commit()
            self.num = 0
            self.l = []
        return item

    def close_spider(self, spider):
        sql = 'insert into maoyan values(%s,%s,%s)'
        if len(self.l) > 0:
            self.cur.executemany(sql, self.l)
            self.conn.commit()
        self.cur.close()
        self.conn.close()


