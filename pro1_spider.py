import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import Project1Item


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/login'
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username': 'Monish',
            'password': 'uptownfunk'
        }, callback=self.start_scraping)

    def start_scraping(self, response):
        open_in_browser(response)
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

        next_page = response.css('li.next > a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.start_scraping)
