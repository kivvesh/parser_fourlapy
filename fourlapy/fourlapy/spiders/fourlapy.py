import scrapy

class QuotesSpider(scrapy.Spider):
    name = "animal"
    start_urls = [
        'https://4lapy.ru/catalog/koshki/korm-koshki/sukhoy/?section_id=3&sort=popular&page=1',
        'https://4lapy.ru/catalog/koshki/korm-koshki/sukhoy/?section_id=3&sort=popular&page=2',
        'https://4lapy.ru/catalog/koshki/korm-koshki/sukhoy/?section_id=3&sort=popular&page=3',
        'https://4lapy.ru/catalog/koshki/korm-koshki/sukhoy/?section_id=3&sort=popular&page=4',
        'https://4lapy.ru/catalog/koshki/korm-koshki/sukhoy/?section_id=3&sort=popular&page=5',

    ]
    #href_page = response.xpath('//a[@class="b-pagination__link  js-pagination"]/@href').getall() получаем href pages
    def parse(self, response):
        href_tovar = response.xpath('//a[@class="b-common-item__image-link js-item-link"]/@href').getall()
        for href in href_tovar:
            yield response.follow(href,callback=self.tovar)

    def tovar(self,response):
        id = response.xpath('//div[@class="b-product-card"]/@data-productid').get()
        brand = response.xpath('//span[@itemprop="brand"]/text()').get()
        title = response.xpath('//h1/text()').get()
        massa = response.xpath('//div[@class="b-product-information__value"]/text()').getall()[0].strip()
        price = response.xpath('//span[@class="b-product-information__price js-price-product js-current-offer-price js-main-price"]/text()').get()
        old_price = response.xpath('//span[@class="b-product-information__old-price js-main-old-price js-current-offer-price-old"]/text()').get()
        if old_price is None:
            old_price=price
        url = response.url
        yield {
            'id':id,
            'brand': brand,
            'title':title,
            'massa':massa,
            'price':price,
            'old_price':old_price,
            'url':url
        }
