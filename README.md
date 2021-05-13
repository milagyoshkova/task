A SQLite Scheduler for Scrapy Framework.
Scrapy-sqlite is a tool that lets you feed and queue URLs from SQLite via Scrapy spiders, using the Scrapy framework.

Inspired by and modled after scrapy-rabbitmq which was inspired by and modled after scrapy-redis.

This classes use by default the same table for Scheduler, Dupefilter, Queue and Httpcache.

Installation
Using pip, type in your command-line prompt

pip install scrapy-sqlite
Or clone the repo and inside the scrapy-sqlite directory, type

python setup.py install
Usage
config values:
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
Updating Spyder
You can update Spyder by:

Updating Anaconda, WinPython or Python(x,y).

Or using this command (in case you don’t use any of those scientific distributions):

pip install --upgrade spyder
#!/usr/bin/env python
import sqlite3
import settings

connection = sqlite3.connect('db.sqlite3'))

connection.close()

