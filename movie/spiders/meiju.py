# -*- coding: utf-8 -*-
import scrapy

from movie.items import MovieItem


class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['http://meijutt.com/']

    def parse(self, response):

        # movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        movies = response.xpath('//div[@class="l week-hot layout-box"]/ul/li')
        for each_movie in movies:
            item = MovieItem()

            item['name'] = each_movie.xpath('./a/@title | ./p/a/@title').extract()[0]
            yield item
