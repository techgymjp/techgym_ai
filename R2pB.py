import scrapy

class TripAdvisorSpider(scrapy.Spider):
  name = 'trip_advisor'
  allowed_domains = ['www.tripadvisor.jp']
  start_urls = ['https://www.tripadvisor.jp/']

  def parse(self, response):
    for name in response.css(".social-sections-HeaderSection__section--125AG::text").extract():
      print(name)
