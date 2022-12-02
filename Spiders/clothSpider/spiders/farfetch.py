import scrapy

class farfetchSpider(scrapy.Spider):
    name = 'farfetch'   # indetifies the spider
    start_urls = [
        'https://www.farfetch.com/ch/shopping/men/jackets-2/items.aspx?page=1&view=90&sort=3&designer=3680277|18499883|2327807|18370|7199|619|1396825|91140|2038|1664',
        'https://www.farfetch.com/ch/shopping/men/sweaters-knitwear-2/items.aspx?page=1&view=90&sort=3&designer=3680277|18499883|2327807|18370|7199|619|1396825|91140|2038|1664',
        'https://www.farfetch.com/ch/shopping/men/trousers-2/items.aspx?page=1&view=90&sort=3&designer=3680277|18499883|2327807|18370|7199|619|1396825|91140|2038|1664'
        'https://www.farfetch.com/ch/shopping/men/t-shirts-vests-2/items.aspx?page=1&view=90&sort=3&designer=3680277|18499883|2327807|18370|7199|619|1396825|91140|2038|1664'
        'https://www.farfetch.com/ch/shopping/men/shirts-2/items.aspx?page=1&view=90&sort=3&designer=3680277|18499883|2327807|18370|7199|619|1396825|91140|2038|1664'
        'https://www.farfetch.com/ch/shopping/men/denim-2/items.aspx?page=1&view=90&sort=3&designer=3680277|18499883|2327807|18370|7199|619|1396825|91140|2038|1664'
    ]

    # function to generate requests to given urls
    # def start_requests(self):
    #     urls = [
    #         'https://www.supremenewyork.com/shop',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        
        for item in response.css('.ltr-wp3p8x.el4qh4n0 li a::attr(href)').getall():
            if item is not None:
                next_page = response.urljoin(item)
                category = response.url.split('https://www.farfetch.com/ch/shopping/men/')[1].split('-2')[0]
                yield scrapy.Request(next_page, callback=self.parse_item, meta={'category': category})


    def parse_item(self, response):

        # for colors in response.css('ul li button::attr(data-url)').getall():

        available = False
        sizes = []

        print(response.css('.ltr-jtdb6u-Body-Heading-HeadingBold::text'))

        # def isAvailable(x):
        #     if "OUT OF STOCK" or "Select Size" in x:
        #         return False
        #     else:
        #         return True

        # def size_cleaner(x):
        #     x = x.replace('\n', '')
        #     x = x.replace(" -  ONLY ONE LEFT", '')
        #     return x

        # if response.css('#add-to-cart.disabled').get() is None:
        #     available = True
        #     all_sizes = response.css('select#va-size option::text').getall()
        #     size = filter(isAvailable, all_sizes)
        #     sizes = list(map(size_cleaner, size))

        
        yield {
            'brand': "Amiri",
            'title': response.css('.ltr-i980jo.el610qn0 a::text').get() + " " + response.css('.ltr-13ze6d5-Body::text').get(),
            'price': response.css('p.ltr-194u1uv-Heading::text').get().strip(),
            'image': response.css('button img:nth-child(1)::attr(src)').get(),
            'link': response.url,
            'category': response.meta.category,
            'description': ' '.join(response.css('._fdc1e5 li::text').getall()).strip(),
            'color': response.css('li.ltr-4y8w0i-Body:nth-child(1)::text').get().strip(),
            'available': True,
            'sizes': ["S", "M", "L", "XL"]
        }


