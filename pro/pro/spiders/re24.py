
import requests
import random
import scrapy
import os
import re
import pandas as pd
import datetime
import json
import re
import csv
from openpyxl import Workbook

class ScrapeSpider(scrapy.Spider):
    name = "re24"
    start_urls = ['https://www.bol.com/']
    scraped_data = []
    file_name = 'All URLs.csv'


    # def start_requests(self):
    #     # proxies = self.get_proxies()
    #     for url in self.start_urls:
    #         # proxy = random.choice(proxy_list)
    #         yield scrapy.Request(url, callback=self.main_link)

    def start_requests(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_file_path = os.path.join(current_dir, self.file_name)
        with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                if row:
                    url = row['Link']
                    yield scrapy.Request(url,callback=self.parse,meta={'url': url,},dont_filter= True)
    # def main_link(self, response):
    #
    #     main_links = [
    #                     # 'https://www.bol.com/nl/nl/w/huishouden-happycostumer/1819712+12001/?page=1',
    #                   # 'https://www.bol.com/nl/nl/w/tuinspullen-happycostumer/1819712+12974/?page=1',
    #                   'https://www.bol.com/nl/nl/w/woonaccessoires-happycostumer/1819712+14124/',
    #                   'https://www.bol.com/nl/nl/w/meubels-happycostumer/1819712+25152/',
    #                   'https://www.bol.com/nl/nl/w/beddengoed-happycostumer/1819712+14193/'
    #                 ]
    #     for main_link in main_links:
    #         yield scrapy.Request(main_link, callback=self.parse_link, dont_filter=True)

    # def parse_link(self, response):
    #     urls = response.xpath(
    #         '//a[@class="product-title px_list_page_product_click list_page_product_tracking_target"]/@href | //a[@data-test="product-title"]/@href').getall()
    #     for url in urls:
    #         absolute_url = response.urljoin(url) 
    #         yield scrapy.Request(url=absolute_url, callback=self.parse, meta={'url': absolute_url},dont_filter= True)

    #     next_page = response.xpath('//ul[@class="pagination"]/li/a[@class="js_pagination_item"]/@href').get()
    #     if next_page:
    #         next_page_url = response.urljoin(next_page)
    #         yield scrapy.Request(url=next_page_url, callback=self.parse_link)

    #     page_links = response.xpath('//ul[@class="pagination"]/li/a[@class="js_pagination_item"]/@href').getall()
    #     for page_link in page_links:
    #         absolute_page_url = response.urljoin(page_link)
    #         yield scrapy.Request(url=absolute_page_url, callback=self.parse_link)  # Follow all pagination links

    def parse(self, response):
        url = response.meta.get('url')
        name = response.xpath('//span[@data-test="title"]/text()').get()

        price_text = response.xpath('//span[@data-test="price-info-srt-text"]//following-sibling::*/text()').get()
        price = price_text.strip() if price_text else None

        friction_text = response.xpath('//sup[@data-test="price-fraction"]/text()').get()
        if friction_text:
            friction = friction_text.replace('-','')
        else:
            friction = ''
        # fp = price + "." + friction if price and friction else price
        if price and friction:
            fp = price + "." + friction
        else:
            fp = price


        if fp:
            try:
                if '.' in fp:
                    fp = float(fp)  
                else:
                    fp = int(fp)  
            except ValueError:
                fp = 'N/A'
        ean_text = response.xpath('//dt[contains(., "EAN")]/following-sibling::dd[1]//text()').get()
        if ean_text:
            ean_element = ean_text.strip() if ean_text else None
            ean = int(ean_element)

        self.scraped_data.append({
            'Reference': '',
            'EAN': ean,
            'Condition': 'Nieuw',
            'Stock': '5',
            'Price': fp,
            'Deliverycode': '1-8d',
            'Fulfillment by': 'Verkoper',
            'Offer description': '',
            'For sale': 'Ja',
            'Title': name,
            'Product URL': url
        })


    def closed(self, reason):
        df = pd.DataFrame(self.scraped_data)
        df.to_excel('Seven Shop.xlsx', index=False, engine='openpyxl')
        self.log('Data saved to Seven Shop 1.xlsx')

    
