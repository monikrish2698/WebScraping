import scrapy
from ..items import Project1Item


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):

        items = Project1Item()

        subtags = response.css('div.quote')
        for q in subtags:
            text = q.css('span.text::text').extract()
            author = q.css('.author::text').extract()
            tags = q.css('.tag::text').extract()

            items['text'] = text
            items['author'] = author
            items['tags'] = tags

            yield items
