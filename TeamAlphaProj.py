import scrapy
import requests

url = 'http://www.ite.edu.sg/'
# http://172.18.58.238/index.html
r = requests.get(url)

print("status code:")
print("\t ", r.status_code)
h = requests.head(url)
print("Header:")
print("**")

for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**")

headers = {
    'User-Agent': "Mobile"
}
# Test it on an external site
url2 = 'http://www.ite.edu.sg/'
rh = requests.get(url2, headers=headers)
print(rh.text)


class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://www.ite.edu.sg/']

    def parse(self, response):
        xpath_selector = '//img'
        for x in response.xpath(xpath_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }
            # To recurse next page
            Page_selector = '.next a ::attr(href)'
            next_page = response.css(Page_selector).extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )
