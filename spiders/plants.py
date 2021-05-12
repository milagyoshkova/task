import scrapy


class PlantsSpider(scrapy.Spider):
    name = 'plants'
    allowed_domains = ['https://gplay.bg/']
    start_urls = ['http://https://gplay.bg//']

    def parse(self, response):
        from link in response.css('div.caption a::attr(herf)'):
            yield response.follow(link.get(), callable=self.parse_cotegories))


    def parse_cotegories (self, response):
        product = response.css('product-item')
        for product in products:
            yield {
                
                subcategory : product.css('h2.product-subtitle::text').get().strip(),
                title : product.css('h1.large-title::text').get().strip(),
                subtitle : product.css('h2.product-subtitle::text' ).get().strip(),
                product numer : ('div.col-md-6 product-ref-number::text').get().strip(),
                price : product.css('div.price::text').get(),


            }

