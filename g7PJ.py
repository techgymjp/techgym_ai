import scrapy
import pandas as pd

class TripAdvisorSpider(scrapy.Spider):
  name = 'trip_advisor'
  allowed_domains = ['www.tripadvisor.jp']
  start_urls = ['https://www.tripadvisor.jp/Restaurants-g1066461-Taito_Tokyo_Tokyo_Prefecture_Kanto.html']

  def parse(self, response):
    cols      = ["Shop", "Tags", "Price"]
    shop_list = pd.DataFrame(index=[], columns=cols)
    for name in response.css(".shortSellDetails"):
      shop   = name.css(".title a::text").extract()[0].replace('\n','')
      tags   = ",".join(name.css(".cuisines a::text").extract())
      price  = name.css(".price::text").extract()[0]
      record = pd.Series([shop, tags, price], index=shop_list.columns)
      shop_list = shop_list.append(record, ignore_index=True)

    shop_list.to_csv("shop_list.csv",index=False)
