import scrapy
from ..items import Project3Item


class BookSpider(scrapy.Spider):
    name = 'book'
    start_urls = [
        'http://books.toscrape.com/'
    ]

    def parse(self, response):
        items = Project3Item()
        for article in response.css('article.product_pod'):
            title = article.css('h3 > a::attr(title)').extract()
            price = article.css('.price_color::text').extract()

            items['title'] = title
            items['price'] = price
            yield items

        # the below codes are used in navigating to next pages and scrape the data
        next1 = response.css('.next > a::attr(href)').extract_first()
        if 'catalogue/' not in next1:
            next1 = 'catalogue/' + next1
        next2 = "http://books.toscrape.com/" + next1
        if next2:
            yield scrapy.Request(next2, callback=self.parse)
