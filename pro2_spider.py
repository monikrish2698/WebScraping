import scrapy

from ..items import Project2Item   #you will find it in the project folder "items.py"


class Quotes2Spider(scrapy.Spider):
    name = 'quotes2'          #two variables should be set as name and start_urls, no other names should be given in this case
    start_urls = [
        'https://www.brainyquote.com/topics/scrape-quotes'  #list which allows storing multiple sites
    ]

    def parse(self, response): #parse function iterates over self and stores the html content in response variable
        items = Project2Item()  #creating an instance to store the values in item
        subquotes = response.css('div.qll-bg')
        for s in subquotes:
            text = s.css('a.oncl_q::text').extract()
            author = s.css('.oncl_a::text').extract()
            tags = s.css('.qkw-btn::text').extract()

            items['text'] = text
            items['author'] = author
            items['tags'] = tags

            yield items   #yield the assigned values 
