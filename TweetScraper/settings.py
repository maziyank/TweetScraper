# !!! # Crawl responsibly by identifying yourself (and your website/e-mail) on the user-agent
USER_AGENT = 'xxx@xxx.id'

# settings for spiders
BOT_NAME = 'TweetScraper'
LOG_LEVEL = 'INFO'

SPIDER_MODULES = ['TweetScraper.spiders']
NEWSPIDER_MODULE = 'TweetScraper.spiders'
ITEM_PIPELINES = {
    'crawlab.pipelines.CrawlabMongoPipeline': 888,
    # 'TweetScraper.pipelines.SaveToElasticPipeline':100,
}

DOWNLOAD_DELAY = 1.0

# settings for selenium
from shutil import which
SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_BROWSER_EXECUTABLE_PATH = which('chrome')
SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver')
SELENIUM_DRIVER_ARGUMENTS=['-headless']  # '--headless' if using chrome instead of firefox
DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800
}

# elastic
ELASTIC_TWEET_COLLECTION = 'tweet'
ELASTIC_USER_COLLECTION = 'user'
ELASTIC_PORT = 9200