import scrapy


class YadTwoSpider(scrapy.Spider):
    name = "yad"

    def __init__(self, urls=None):
        self.urls = urls

    def start_requests(self):
        # for url in self.urls:
        BASE_URL = "https://www.yad2.co.il/realestate/forsale"
        yield scrapy.Request(url=BASE_URL, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
