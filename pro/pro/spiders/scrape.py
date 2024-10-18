import scrapy
import pandas as pd
import datetime
from urllib.parse import urljoin
import re
import os
import json
import csv
from selenium.webdriver import Chrome, ChromeOptions
from scrapy_selenium import SeleniumRequest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import (NoSuchElementException, StaleElementReferenceException, TimeoutException)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import datetime
import logging
from urllib.parse import urljoin
import re
from lxml import etree
from lxml import html
import pandas as pd
import csv
import os
import json
from bs4 import BeautifulSoup
from time import sleep
import time
import logging
from scrapy import Request

from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse, parse_qs

url = 'https://www.tripadvisor.com/Attractions-g187070-Activities-oa0-a_sort.TRAVELER__5F__FAVORITE__5F__V2-France.html'

class ScrapeSpider(scrapy.Spider):
    name = "scrape"
    current_page_number = 0
    # custom_settings = {
    #     "DOWNLOAD_HANDLERS": {
    #         "http": "scrapy_impersonate.ImpersonateDownloadHandler",
    #         "https": "scrapy_impersonate.ImpersonateDownloadHandler",
    #     },
    #     "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
    # }

    def start_requests(self):
        for browser in ["chrome120"]:
            url = "https://www.tripadvisor.com/Attractions-g187070-Activities-oa0-a_sort.TRAVELER__5F__FAVORITE__5F__V2-France.html"
            yield scrapy.Request(
                "https://www.tripadvisor.com/Attractions-g187070-Activities-oa0-a_sort.TRAVELER__5F__FAVORITE__5F__V2-France.html",
                callback=self.parse,
                meta={'url': url,
                    "impersonate": browser,
                    "impersonate_args": {
                        "verify": False,
                    },
                },
            )
    def __init__(self, *args, **kwargs):
        super(ScrapeSpider, self).__init__(*args, **kwargs)
        self.process_count = 0
    def parse(self, response):
        # pass

        retries = 25
        results = set()
        place_url = []
        base_url = response.meta['url']
        join_url = "https://www.tripadvisor.com"
        html_content = response.body.decode('utf-8')
        tree = etree.HTML(html_content)
        main_cards = tree.xpath('//div[@data-automation="cardWrapper"]')
        for main_card in main_cards:
            rank_nos = main_card.xpath('.//h3/div/span/div/span/text()')
            rank_no = [rank_.replace('.', '').strip() for rank_ in rank_nos]
            main_url = main_card.xpath('.//a[starts-with (@href, "/Attraction_Review-g")]/@href')
            if rank_no and main_url:
                rank_no = rank_no[0]
                main_url = main_url[0]
                results.add((rank_no, main_url))
        for rank_no, main_url in results:
            url = join_url + main_url
            place_url.append(url)
        print("Total Link No:", len(place_url))

        self.current_page_number += 30
        next_page_relative_url = re.sub(r'oa\d+', f'oa{self.current_page_number}', base_url)
        print("Next Pagination:", next_page_relative_url)
        self.process_count += 1

        if self.process_count < 10:  #
            yield scrapy.Request(next_page_relative_url, callback=self.parse, meta={'url': base_url, },
                                 dont_filter=True)
        else:
            print(" ")
    # def start_requests(self):
    #     yield Request(
    #         url="https://tls.browserleaks.com/json",
    #         dont_filter=True,
    #         meta={
    #             "impersonate": "chrome110",
    #             "impersonate_args": {
    #                 "verify": False,
    #             },
    #         },
    #         callback=self.parse
    #     )