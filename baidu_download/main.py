# _*_ coding: utf-8 _*_

from scrapy.cmdline import execute
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__))) #设置工程目录
print(os.path.dirname(os.path.abspath(__file__)))

execute(["scrapy", "crawl", "pic_spider"]).strip()