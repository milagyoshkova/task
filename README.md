Installation
Using pip, type in your command-line prompt

pip install scrapy-sqlite
Or clone the repo and inside the scrapy-sqlite directory, type

python setup.py install
Usage
Step 1: In your scrapy settings, add the following config values:
# Enables scheduling storing requests queue in sqlite.
SCHEDULER = "scrapy_sqlite.scheduler.Scheduler"

# Don't cleanup sqlite queues, allows to pause/resume crawls.
SCHEDULER_PERSIST = True

# Provide path to SQLite db file, this example creates imdb.sqlite3 filename for bot named imdb
SQLITE_DATABASE = '%(spider)s.sqlite3'

# Store scraped item in sqlite for post-processing.
ITEM_PIPELINES = {
    'scrapy_sqlite.pipelines.SQLitePipeline': 100
}

# Cache Storage class 
HTTPCACHE_STORAGE = 'scrapy_sqlite.httpcache.SQLiteCacheStorage'

# Enables gzip compression of responses. If response are already recieved compressed (recommended and very used feature by webservers), it compresses response second time
HTTPCACHE_GZIP = True

Step 2: Add SQLiteMixin to Spider.
Example: multidomain_spider.py
from scrapy.contrib.spiders import CrawlSpider
from scrapy_sqlite.spiders import SQLiteMixin

class MultiDomainSpider(SQLiteMixin, CrawlSpider):
    name = 'multidomain'

    def parse(self, response):
        # parse all the things
        pass

Step 3: Run spider using scrapy client
scrapy runspider multidomain_spider.py
Step 4: Push URLs to SQLite
Example: push_web_page_to_queue.py
#TODO: reprogramm to sqlite

#!/usr/bin/env python
import sqlite3
import settings

connection = sqlite3.connect('db.sqlite3'))

connection.close()
