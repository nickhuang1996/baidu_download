import scrapy, json
from scrapy.http import Request
from baidu_download.items import BaiduDownloadItem  # 导入item
from baidu_download.settings import key_word
from urllib.parse import quote


class PicSpider(scrapy.Spider):
    name = "pic_spider"
    allowed_domains = ["http://image.baidu.com/"]
    start_urls = ["http://image.baidu.com"]

    def parse(self, response):  # 定义解析函数

        # 将带关键词参数的url交给request函数解析，返回的response通过get_pic回调函数进一步分析
        data = {'queryWord': key_word, 'word': key_word}
        base_url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord='
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            data['pn'] = page * 30
            baidu_pic_url = base_url + quote(data['queryWord']) + '&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=' + \
                  quote(data['word']) + '&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&pn=' + \
                  quote(str(data['pn'])) + '&rn=30&gsm=' + str(hex(data['pn']))
            yield Request(baidu_pic_url, meta={"search_word": key_word}, callback=self.get_pic, dont_filter=True)


    def get_pic(self, response):  # 从图片list中获取每个pic的信息

        item = BaiduDownloadItem()  # 实例化item
        response_json = response.text  # 存储返回的json数据
        response_dict = json.loads(response_json)  # 转化为字典
        response_dict_data = response_dict['data']  # 图片的有效数据在data参数中

        for pic in response_dict_data:  # pic为每个图片的信息数据，dict类型
            if pic:
                item['search_word'] = response.meta['search_word']  # 搜索关键词赋值
                item['pic_url'] = [pic['middleURL']]  # 百度图片搜索结果url (setting中pic_url应该为数组形式)
                item['pic_name'] = pic['fromPageTitleEnc']  # 百度图片搜索结果对应的title
                yield item