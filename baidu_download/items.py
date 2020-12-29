# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduDownloadItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    search_word = scrapy.Field()  # 搜索关键字
    pic_name = scrapy.Field()  # 图片标题
    pic_url = scrapy.Field()  # 图片url
    pass
