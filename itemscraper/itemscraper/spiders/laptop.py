import scrapy
import re
from ..items import ItemscraperItem


class LaptopSpider(scrapy.Spider):
    name = "laptop"
    page_number = 2
    # Enter amount_of pages for extracting data
    amount_of_pages = 5
    start_urls = [
        "https://rozetka.com.ua/notebooks/c80004/page=1/"
    ]

    def parse(self, response):
        items = ItemscraperItem()
        all_item = response.css("li.catalog-grid__cell.catalog-grid__cell_type_slim")

        for item in all_item:
            product_name = item.css("span.goods-tile__title").css("::text").extract()
            product_price = item.css("span.goods-tile__price-value").css("::text").extract()
            product_available = item.css(".goods-tile__availability_type_available").css("::text").extract()
            product_limited = item.css(".goods-tile__availability_type_limited").css("::text").extract()
            product_reviews = item.css(".goods-tile__rating").css("::text").extract()
            product_image = item.css("a.goods-tile__picture").css("::attr(data-url)").extract()

            items['product_name'] = re.split(r'\(', product_name[0])[0].strip()
            items['product_price'] = product_price[0].strip()
            items['product_reviews'] = product_reviews[0].strip()
            items['product_available'] = product_available if product_available else ['Товар Заканчивается'] if product_limited else ['Нет в наличии']
            items['product_image'] = product_image[0]

            yield items

        next_page = 'https://rozetka.com.ua/notebooks/c80004/page=' + str(LaptopSpider.page_number) + '/'
        if LaptopSpider.page_number <= LaptopSpider.amount_of_pages:
            LaptopSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
