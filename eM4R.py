import scrapy

class TripAdvisorSpider(scrapy.Spider):
  name = 'trip_advisor'
  allowed_domains = ['www.tripadvisor.jp']
  start_urls = ['https://www.tripadvisor.jp/Restaurants-g1066461-Taito_Tokyo_Tokyo_Prefecture_Kanto.html']

  def parse(self, response):
    for name in response.css(".shortSellDetails"):
      print("====shop====")
      print(name.css(".title a::text").extract()[0])
      print(name.css(".cuisines a::text").extract())
      print(name.css(".price::text").extract()[0])
