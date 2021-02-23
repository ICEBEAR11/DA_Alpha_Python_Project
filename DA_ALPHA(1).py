import requests
import scrapy
r = requests.get('http://172.18.58.238/')

print("Status code:")
print("\t *", r.status_code)

h = requests.head('http://172.18.58.238/')
print("Header:")
print("**********")
# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")

headers = {
    'User-Agent': 'Mobile'
}
# Test it on an external site
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)





class ProjectSpider(scrapy.Spider):
    name = "new"

    start_urls = [
        'http://172.18.58.238']

    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
        }
            page_selector = '.next a ::attr(href)'
            next_page = response.css(page_selector).extract_first()
            if next_page:
                yield scrapy.Request(
                    response.urljoin(next_page),
                    callback=self.parse
                )