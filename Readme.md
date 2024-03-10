# Demo crawl data to MongoDB

### Spider
```python
class testSpider(scrapy.Spider):
    name = "test"
    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self,response):
        books = response.css(".quote")
        items = QuotetutorialItem()
        for book in books:
            items["title"]= book.css(".text::text").get()
            items["author"] = book.css(".author::text").get()
            items["tags"] = book.css(".tag::text").extract()

            yield items
```

### Pipeline data
```python

import pymongo

class QuotetutorialPipeline:
    def __init__(self):
        self.myClient = pymongo.MongoClient("mongodb://localhost:27017")
        db = self.myClient["DataCrawl"]
        self.myCollection = db["Book"]
    def process_item(self, item, spider):
        self.myCollection.insert_one(dict(item))
        return item
```
# Thank you !!!