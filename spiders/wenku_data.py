# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 10:12

import scrapy
from ..items import WenkuxiazaiItem
from lxml import etree
import requests
import re
from pymongo import MongoClient
import urllib.parse
import time
import random
from ..get_user_agent import User_Agent
import hashlib

con=MongoClient("192.168.8.211",27017)
db=con.Runoob
download_set=db.wenkuxiazaiwang_data#下载这里
# keyword_set=db.Runoob#从这里取出url（测试关键字）
keyword_set=db.key_cn#从这里取出url
coll_ip=db.coll_ip


def get_url_data(index_url,keyword,page):
    url=index_url+str(urllib.parse.quote(keyword,encoding="gb2312"))+"-"+str(page)+".html"
    # print("url@@@@@@@@@@@@",url)
    return url

def get_keyword():
    # while True:
        data = keyword_set.find_one_and_update({"status": 0}, {"$set": {"status": 1}})
        print(data["_id"])
        if not data:
            return
        return data["_id"]

class WenkuDataSpider(scrapy.Spider):
    name = 'wenku_data'
    allowed_domains = ['www.wenkuxiazai.com']
    index_url = 'https://www.wenkuxiazai.com/search/'
    # keyword="python"
    page=0
    keyword = get_keyword()
    # keyword = "抗渣侵蚀"
    url = get_url_data(index_url,keyword,page)
    start_urls = [url]

    # // 添加的请求头(方法一)
    custom_settings = {
                          # 'LOG_LEVEL': 'DEBUG',
                          # 'LOG_FILE': '5688_log_%s.txt' % time.time(),
    "DEFAULT_REQUEST_HEADERS": {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
        # "Cookie": "ASP.NET_SessionId=swciagkmit0wgon1optvezol; UM_distinctid=167e377fe96227-02ebec8327d1c7-671b1b7c-1fa400-167e377fe97ff; Hm_lvt_1cb6d926d0e483d882157f92a7640d52=1545709552,1545709555,1545709557,1545709570; Hm_lpvt_1cb6d926d0e483d882157f92a7640d52=1545716426; CNZZDATA1253566994=1799924477-1545709207-%7C1545714908",
        "Host": "www.wenkuxiazai.com",
        "Referer": "https://www.wenkuxiazai.com/",
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'User-Agent':random.choice(User_Agent),
        # 'Cache - Control': 'max - age = 0'

    }
    }

    def start_requests(self):
        # if len(self.start_urls) == 0:
        #     self.page = 0
        #     self.keyword = get_keyword()
        #     url = get_url_data(self.index_url, self.keyword, self.page)
        #     self.start_urls.append(url)
        #     print("1",self.start_urls)

        for url in self.start_urls:
        #     url= self.start_urls[0]
        #     self.start_urls.remove(url)
            print("2",self.start_urls)
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        # print("------------",response.text)
        html = etree.HTML(response.text)
        # html=response
        # test=html.xpath("//html")
        url_list = html.xpath("//div[@class='lista']/div/p/a/@href")
        title_list = html.xpath("//div[@class='lista']/div/p/a/@title")
        summary_list = html.xpath("//div[@class='lista']/div/p[2]")
        index=0
        for url in url_list:
            MD5_url = hashlib.md5()
            MD5_url.update(url.encode())

            item = WenkuxiazaiItem()
            item['title'] = title_list[index].strip()
            item['url'] = "https://www.wenkuxiazai.com/word"+url[4:-5]+"-1.doc"
            item['summary'] = summary_list[index].xpath('string(.)').strip()
            item['MD5_url'] = MD5_url.hexdigest()
            item['status'] = 0
            item['status_test'] = 0

            index+=1
            yield item

        next = html.xpath("//p[@class='pages']/a[@class='next']/text()")# next = response.xpath("//nav/ul/li/a/@href")  # 下一页的链接
        print(next)
        if next:
            # url = response.urljoin(next)
            self.page+=10
            url = get_url_data(self.index_url,self.keyword,self.page)
            print("url------next",url)
            yield scrapy.Request(url=url, callback=self.parse,dont_filter=True)
        else:
            self.page=0
            self.keyword = get_keyword()
            url = get_url_data(self.index_url, self.keyword, self.page)
        #     global start_urls
        #     start_urls= [url]
        #     print(self.keyword)
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)
