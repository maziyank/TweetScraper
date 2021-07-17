import os, logging, json
from scrapy.utils.project import get_project_settings

from TweetScraper.items import Tweet, User
from TweetScraper.utils import mkdirs
from elasticsearch import Elasticsearch


logger = logging.getLogger(__name__)
SETTINGS = get_project_settings()

# For Future Used
class SaveToElasticPipeline(object):
    ''' pipeline that save data to elasticdb '''

    def __init__(self):
        self.es = Elasticsearch(port=SETTINGS['ELASTIC_PORT'])

    def process_item(self, item, spider):
        if isinstance(item, Tweet):             
            self.es.index(index=SETTINGS['ELASTIC_TWEET_COLLECTION'], id=item['id_'], body=dict(item))
            logger.debug("Add tweet:%s" %item['id_'])

        elif isinstance(item, User):                        
            self.es.index(index=SETTINGS['ELASTIC_USER_COLLECTION'], id=item['id_'], body=dict(item))
            logger.debug("Add user:%s" %item['id_'])

        else:
            logger.info("Item type is not recognized! type = %s" %type(item))            