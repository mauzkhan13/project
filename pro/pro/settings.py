import re
from twisted.internet import asyncioreactor
BOT_NAME = "pro"

SPIDER_MODULES = ["pro.spiders"]
NEWSPIDER_MODULE = "pro.spiders"

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 0.1

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
# DOWNLOAD_HANDLERS = {
#     "http": "scrapy_impersonate.ImpersonateDownloadHandler",
#     "https": "scrapy_impersonate.ImpersonateDownloadHandler",
# }


# SCRAPEOPS_API_KEY = '39a0ddec-c220-487e-a50a-d962fecd95aa'
# SCRAPEOPS_PROXY_ENABLED = True
#
# DOWNLOADER_MIDDLEWARES = {
#     'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
# }
# CONCURRENT_REQUESTS = 1
#
# DOWNLOAD_HANDLERS = {
#     "http": "scrapy_impersonate.ImpersonateDownloadHandler",
#     "https": "scrapy_impersonate.ImpersonateDownloadHandler",
# }
#
# TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
# #
# ROTATING_PROXY_LIST = [
#     'http://fpssllc:a67594-445607-e0a01b-25f9ed-3081fd@usa.rotating.proxyrack.net:9000',
# ]
#
# DOWNLOADER_MIDDLEWARES = {
#     'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
#     'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
# }
#

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"




# # Splash Server Endpoint
# SPLASH_URL = 'http://localhost:8050'
#
#
# # Enable Splash downloader middleware and change HttpCompressionMiddleware priority
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy_splash.SplashCookiesMiddleware': 723,
#     'scrapy_splash.SplashMiddleware': 725,
#     'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
# }
#
# # Enable Splash Deduplicate Args Filter
# SPIDER_MIDDLEWARES = {
#     'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
# }
#
# # Define the Splash DupeFilter
# DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
