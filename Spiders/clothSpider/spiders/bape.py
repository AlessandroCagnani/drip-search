import scrapy

class DrippySpider(scrapy.Spider):
    name = 'bape'   # indetifies the spider
    start_urls = [
        'https://int.bape.com/bape/men/',
    ]

    # function to generate requests to given urls
    # def start_requests(self):
    #     urls = [
    #         'https://www.supremenewyork.com/shop',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if "currenct-last" not in response.css('.current-page').xpath("@class").extract():
            current_page = response.css('.current-page::text').get().strip()
            next_page = response.css('.page-' + str(int(current_page)+1) + '::attr(href)').get()
            yield scrapy.Request(next_page, callback=self.parse)

        for item in response.css('#product-image-slider-0 a.thumb-link::attr(href)').getall():
            if item is not None:
                yield scrapy.Request(item, callback=self.parse_item)


    def parse_item(self, response):

        for colors in response.css('ul li button::attr(data-url)').getall():
            if colors is not None:
                next_page = response.urljoin(colors)
                yield scrapy.Request(next_page, callback=self.parse_item)

        available = False
        sizes = []

        def isAvailable(x):
            if "OUT OF STOCK" or "Select Size" in x:
                return False
            else:
                return True

        def size_cleaner(x):
            x = x.replace('\n', '')
            x = x.replace(" -  ONLY ONE LEFT", '')
            return x

        if response.css('#add-to-cart.disabled').get() is None:
            available = True
            all_sizes = response.css('select#va-size option::text').getall()
            size = filter(isAvailable, all_sizes)
            sizes = list(map(size_cleaner, size))

        yield {
            'brand': "bape",
            'title': response.css('.pdp-name > h1:nth-child(1)::text').get(),
            'price': response.css('.headline4::text').get().strip(),
            'image': response.css('#pdp-product-img-0 > img:nth-child(1)::attr(data-src)').get(),
            'link': response.url,
            'category': response.css('a.breadcrumb-element:nth-child(6)::text').get(),
            'description': ''.join(response.css('.panel-details p::text').getall()),
            'color': response.css('.pdp-color-value::text').get(),
            'available': available,
            'sizes': sizes
        }


