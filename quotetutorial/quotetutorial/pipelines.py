
import pymongo

class QuotetutorialPipeline:
    def __init__(self):
        self.myClient = pymongo.MongoClient("mongodb://localhost:27017")
        db = self.myClient["DataCrawl"]
        self.myCollection = db["Book"]
    def process_item(self, item, spider):
        self.myCollection.insert_one(dict(item))
        return item

