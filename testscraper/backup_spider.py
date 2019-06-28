# -*- coding: utf-8 -*-

import json
import scrapy
import time
from items import WmpscraperItem

class WeMakePriceSpider(scrapy.Spider):
    handle_httpstatus_list = [400]
    name = 'wmp_spider'
    page_number = 2
    unix_time = str(time.time()).replace('.', '')
    unix = unix_time[:13]
    referer_url = ['https://www.wemakeprice.com/deal/adeal/3608900/']
    allowed_domains = ['wemakeprice.com']
    start_urls = [
        'http://www.wemakeprice.com/v1/pc/review/deal/3608900/list?page=1&outputType=1&sortCd=2&starSort=0&t='+unix
    ]

    custom_settings = {

        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'DEFAULT_REQUEST_HEADERS':{
    'Referer': referer_url
}
     }



    def parse(self, response):
        items = WmpscraperItem()
        review_data = json.loads(response.text)
        total_page = review_data['data']['reviewList']['paging']['totalPage']
        total_reviews = review_data['data']['reviewList']['paging']['totalCount']
        for review_info in review_data['data']['reviewList']['list']:
            review_rating = review_info['orderSatisfaction']
            review_time = review_info['regDate']
            review_id = review_info['reviewSeq']
            review_title = review_info['orderInfo']['optionValue']
            review_content = review_info['content']
            review_username = review_info['userId']
            review_total = total_reviews
            product_name = review_info['orderInfo']['dealName']
            product_id = review_info['orderInfo']['dealId']
            review_helpfulness = review_info['reviewLikeCount']

            items['review_rating'] = review_rating
            items['review_time'] = review_time
            items['product_name'] = product_name
            items['review_id'] = review_id
            items['review_title'] = review_title
            items['review_content'] = review_content
            items['review_username'] = review_username
            items['review_total'] = review_total
            items['product_id'] = product_id
            items['review_helpfulness'] = review_helpfulness

            yield items
        next_page = 'http://www.wemakeprice.com/v1/pc/review/deal/3608900/list?page='+ str(WeMakePriceSpider.page_number)+'&outputType=1&sortCd=2&starSort=0&t='+WeMakePriceSpider.unix
        if WeMakePriceSpider.page_number <= total_page:
            WeMakePriceSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)