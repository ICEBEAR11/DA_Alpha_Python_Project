import scrapy
import requests
import os
import unittest

# Set the target webpage
url = 'http://172.18.58.238'
r = requests.get(url)
headers = {
    'User-Agent': 'Mobile'
}
# Display Output Get and Ok
print("Status code:", )
print("\t *",'Ok!', r.status_code,headers)

# Display Website Header
h = requests.head(url)
for x in h.headers:
    print("\t", x, '.', h.headers[x])

# Modify the headers user-agent
headers = {
    'User-Agent': 'Mobile'
}
url2 = 'http://172.18.58.238/headers.php'
rh = requests.get(url2, headers=headers)
print(rh.text)

# Display Reference Webpage
class WebReference(scrapy.Spider):
    name = "web_reference"
    start_urls = ['http://172.18.58.238/']
    open("\\Users\\share\\PycharmProjects\\pythonProjects",'w').close()
    def parse(self, response):
       test = open("Output\\reference.json",'a')
       for link in response.css('a'):
           link_results = link.css('a::attr(href)').get()
           test.write(str({'web_reference': link_results})+"\n")
       test.close()

#image extraction links
class NewSpider(scrapy.Spider):
    name ="new_spider"
    start_urls = ['http://172.18.58.238']
    def parse(self, response):
                css_selector = 'img'
                for x in response.css(css_selector):
                            newsel = '@src'
                            yield {
                                'Image Link': x.xpath(newsel).extract_first(),
                            }


                Page_selector = '.next a ::attr(href)'
                next_page = response.css(Page_selector).extract_first()
                if next_page:
                        yield scrapy.Request(
                                response.urljoin(next_page),
                                callback=self.parse
                )

#unit-testing
class TestMyProgram(unittest.TestCase):
    def test(self):
        os.system("C:\\Users\\share\\PycharmProjects\\pythonProject\\recon.py")
        os.system("C:\\Users\\share\\PycharmProjects\\pythonProject\\webcrawling.py")
        os.system("C:\\Users\\share\\PycharmProjects\\pythonProject\\Imagelinks.py")

    if __name__ == "__main__":
        unittest.main()