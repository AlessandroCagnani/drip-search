import scrapy
from scrapy_playwright.page import PageMethod


class DrippySpider(scrapy.Spider):
    name = 'stockX'
    start_urls = ['https://eu.stussy.com/collections/all']

    def start_requests(self):
        # GET request
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, meta=dict(
                playwright=True,
                playwright_include_page=True,
                playwright_page_methods=[
                    PageMethod('wait_for_selector', 'div'),
                    PageMethod("evaluate", "window.scrollBy(0, document.body.scrollHeight)"),
                    PageMethod("wait_for_selector", "li.collection__product:nth-child(48)"),
                ],
                errback=self.errback))

    async def errback(self, failure):
         page = failure.request.meta["playwright_page"]
         await page.close()

    async def parse(self, response):
        page = response.meta["playwright_page"]
        await page.close()

        # create a request for opening next page
        print(len(response.css('.slick-track a').getall()))

        # call the parse of the item

    async def parse_item(self, response):
        page = response.meta["playwright_page"]
        await page.close()

        # parse the item
        print(response.css('div').getall())


