import scrapy
import pandas as pd

class TripAdvisorSpider(scrapy.Spider):
    name = 'trip_advisor'
    allowed_domains = ['www.tripadvisor.jp']
    start_urls = ['https://www.tripadvisor.jp/Restaurants-g1066461-Taito_Tokyo_Tokyo_Prefecture_Kanto.html']

    def parse(self, response):
