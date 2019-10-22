# class Config:
#     '''
#     general configuration parent class
#     '''
#     pass

# class ProdConfig(Config):
#     '''
#     production configuation child class
#     ''''
    
# class DevConfig(Config):
#     '''
#     development configuration  childclass
#     '''
#     pass

#     DEBUG = True



 import os

class Config:

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey=f9b3923ad99d4449b0e79a0241931c05'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}