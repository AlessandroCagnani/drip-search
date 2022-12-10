import scrapy

class DrippySpider(scrapy.Spider):
    name = 'drip'   # indetifies the spider
    start_urls = [
        'https://www.supremenewyork.com/shop/all',
    ]

    # function to generate requests to given urls
    # def start_requests(self):
    #     urls = [
    #         'https://www.supremenewyork.com/shop',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for item in response.css('div#container article a::attr(href)').getall():
            if item is not None:
                next_page = response.urljoin(item)
                yield scrapy.Request(next_page, callback=self.parse_item)


    def parse_item(self, response):

        for colors in response.css('ul li button::attr(data-url)').getall():
            if colors is not None:
                next_page = response.urljoin(colors)
                yield scrapy.Request(next_page, callback=self.parse_item)

        available = False
        sizes = []
        if response.css('b.button.sold-out').get() is None:
            available = True
            sizes = response.css('select#size option::text').getall()

        yield {
            'brand': "supreme",
            'title': response.css('h1.protect::text').get(),
            'price': response.css('p.price span::text').get(),
            'image': response.urljoin(response.css('img#img-main::attr(src)').get()),
            'link': response.url,
            'category': response.url.split("https://www.supremenewyork.com/shop/")[1].split('/')[0],
            'description': response.css('p.description::text').get(),
            'color': response.css('p.style.protect::text').get(),
            'available': available,
            'sizes': sizes
        }


