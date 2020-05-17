import scrapy
from ..items import AmazonItem


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.in/s?i=computers&bbn=976392031&rh=n%3A1388963031&qid=1589689335&ref=sr_pg_1'
    ]

    def parse(self, response):
        items = AmazonItem()
        for tablet in response.css('.s-include-content-margin'):
            product_name = tablet.css('.a-color-base.a-text-normal').css(
                '::text').extract()
            # company = tablet.css('.a-color-secondary+ .a-color-secondary').css('::text').extract()
            price = tablet.css('.a-price-whole').css('::text').extract()
            i_link = tablet.css('.s-image::attr(src)').extract()

            items['product_name'] = product_name
            # items['company'] = company
            items['price'] = price
            items['i_link'] = i_link

            yield items
