import scrapy


class WmpscraperItem(scrapy.Item):
    product_name = scrapy.Field()
    product_id = scrapy.Field()
    product_price = scrapy.Field()
    product_rating = scrapy.Field()
    review_total = scrapy.Field()
    review_count = scrapy.Field()
    review_id = scrapy.Field()
    review_title = scrapy.Field()
    review_content = scrapy.Field()
    review_rating = scrapy.Field()
    review_time = scrapy.Field()
    review_username = scrapy.Field()
    review_helpfulness = scrapy.Field()
