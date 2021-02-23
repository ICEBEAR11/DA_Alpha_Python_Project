import scrapy
import requests
import os
import unittest

# Set the target webpage
url = 'http://www.ite.edu.sg'
r = requests.get(url)
headers = {
    'User-Agent': 'Mobile'
}
# Display Output Get and Ok
print("Status code:")
print("\t *", r.status_code,headers)

# Display Website Header
h = requests.head(url)
for x in h.headers:
    print("\t", x, '.', h.headers[x])

# Modify the headers user-agent
headers = {
    'User-Agent': 'Mobile'
}
url2 = 'http://www.ite.edu.sg'
rh = requests.get(url2, headers=headers)
print(rh.text)

# Display Reference Webpage
class WebReference(scrapy.Spider):
    name = "web_reference"
    start_urls = ['http://www.ite.edu.sg']
    open("Output\\reference.json",'w').close()
    def parse(self, response):
       test = open("Output\\reference.json",'a')
       for link in response.css('a'):
           link_results = link.css('a::attr(href)').get()
           test.write(str({'web_reference': link_results})+"\n")
       test.close()

#image extraction links
class NewSpider(scrapy.Spider):
    name ="new_spider"
    start_urls = ['http://www.ite.edu.sg']
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
        os.system("C:\\Users\\heng_\\PycharmProjects\\DA_Team3\\recon.py")
        os.system("C:\\Users\\heng_\\PycharmProjects\\DA_Team3\\webcrawling.py")
        os.system("C:\\Users\\heng_\\PycharmProjects\\DA_Team3\\Imagelinks.py")

    if __name__ == "__main__":
        unittest.main()
