# -*- coding: utf-8 -*-
import scrapy
import datetime
from scrapy.spider import CrawlSpider
from scrapy.selector import Selector
import re
from scrape_emails.items import ScrapeEmailsItem
from scrapy.http import Request

class ScrpEmailsSpider(scrapy.Spider):
    name = 'scrp_emails'

    f = open("url_emails.csv")
    start_urls = [url.strip() for url in f.readlines()]
    allowed_domains = [start_urls]
    f.close()

    def parse(self, response):
        selector = Selector(response)
        # emails = re.findall(r'[\w\.-]+@[\w\.-]+', response.body)
        emails = selector.xpath('//body').re('([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)')

        emailitems = []

        for email in zip(emails):
            emailitem=ScrapeEmailsItem()
            emailitem['email'] = emails
            emailitem['source']=response.url
            emailitems.append(emailitem)
            return emailitems

