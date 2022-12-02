import scrapy
from scrapy_playwright.page import PageMethod


class bapeSpider(scrapy.Spider):
    name = 'stockX'
    # https://www.farfetch.com/ch/shopping/men/amiri-skull-print-silk-shirt-item-18621165.aspx?storeid=13537
    # https://www.farfetch.com/ch/shopping/men/clothing-2/items.aspx?page=1&view=90&sort=3&designer=3680277|18499883|2327807|18370|7199|619|1396825|91140|2038|1664
    start_urls = ['https://www.farfetch.com/ch/shopping/men/amiri-mx1-distressed-effect-skinny-jeans-item-16793632.aspx?storeid=13537']

    def start_requests(self):
        # GET request
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse_item, meta=dict(
                playwright=True,
                playwright_include_page=True,
                playwright_page_methods=[
                    PageMethod('wait_for_selector', '.ltr-wp3p8x.el4qh4n0'),
                    # PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)"),
                ],
                errback=self.errback))

    async def errback(self, failure):
         page = failure.request.meta["playwright_page"]
         await page.close()

    async def parse(self, response):
        page = response.meta["playwright_page"]
        await page.close()

        # create a request for opening next page
        # print('page loaded')
        # print("\nretrieved\n ", response.css('.ltr-x69rqn.e19e7out0 .ltr-1gxq4h9.e4l1wga0::attr(href)').getall(), "\n elements\n")

        # call the parse of the item
        for item in response.css('.ltr-x69rqn.e19e7out0 .ltr-1gxq4h9.e4l1wga0::attr(href)').getall():
            if item is not None:
                next_page = response.urljoin(item)
                yield scrapy.Request(next_page, callback=self.parse_item, meta=dict(
                    playwright=True,
                    playwright_include_page=True,
                    playwright_page_methods=[
                        PageMethod('wait_for_selector', '.ltr-i980jo.el610qn0'),
                        # PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)"),
                    ],
                    errback=self.errback))

    async def parse_item(self, response):
        page = response.meta["playwright_page"]
        await page.close()

        # parse the item
        print(response.css('.ltr-i980jo.el610qn0').get())


