1Using pip, type in your command-line prompt

pip install scrapy-sqlite
Or clone the repo and inside the scrapy-sqlite directory, type

python setup.py install

2: Add SQLiteMixin to Spider.
Example: multidomain_spider.py
from scrapy.contrib.spiders import CrawlSpider
from scrapy_sqlite.spiders import SQLiteMixin

class MultiDomainSpider(SQLiteMixin, CrawlSpider):
    name = 'multidomain'

    def parse(self, response):
        # parse all the things
        pass




3 Push URLs to SQLite
Example: push_web_page_to_queue.py
#TODO: reprogramm to sqlite

#!/usr/bin/env python
import sqlite3
import settings

connection = sqlite3.connect('db.sqlite3'))

connection.close()
