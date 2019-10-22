import os
import sys

class Config:

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_KEY= 'f9b3923ad99d4449b0e79a0241931c05'
    NEWS_API_BASE_URL2 = 'https://newsapi.org/v2/everything?sources=bbc-news,al-jazeera-english,cnn,independent,google-news,the-telegraph,mashable,the-lad-bible,buzzfeed,bloomberg,engadget,espn,fortune&sortBy=publishedAt&pageSize=100&apiKey={}'

    


class ProdConfig(Config):

    '''
    production configuration class
    '''

    pass

class DevConfig(Config):

    '''
    development configuration class
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}