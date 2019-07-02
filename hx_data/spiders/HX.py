# -*- coding: utf-8 -*-
import scrapy
import re

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from hx_data.items import HxDataItem


class HxSpider(CrawlSpider):
    name = 'HX'
    allowed_domains = ['huxiu.com']
    start_urls = ['http://huxiu.com/chuangye/']

    rules = (
        Rule(LinkExtractor(allow="(/chuangye/product/\d*?/\w*[\u4e00-\u9fa5]*)"), callback='parse_con'),
    )

    def parse_item(self, response):
        pass

    def parse_con(self, response):
        item = HxDataItem()
        item['name'] = response.xpath("//div[@class='cy-xq-warp']/h1/text()").extract_first()
        item['type'] = response.xpath("//div[@class='cy-tag-list']/ul/li/text()").extract_first()
        item['boss'] = response.xpath("//div[contains(@class,'box-moder') and contains(@class,'cy-box-moder') and contains(@class, 'company-info')]/ul/li/span/text()").extract_first()
        item['money'] = response.xpath("//div[contains(@class,'box-moder') and contains(@class,'cy-box-moder') and contains(@class, 'company-info')]/ul/li/span/text()").extract()[2]
        item['address'] =re.findall('地址：.*?<span>(.*?)<', response.text)[0]
        item['adven'] = response.xpath("//div[@class='cy-cp-advantage']/text()").extract_first().replace(' ', '')
        print(item)
        yield item
