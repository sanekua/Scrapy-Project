import scrapy


class ItemscraperItem(scrapy.Item):
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    product_reviews = scrapy.Field()
    product_available = scrapy.Field()
    product_image = scrapy.Field()
    pass
