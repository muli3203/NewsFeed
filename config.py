class Config:
    '''
    general configuration parent class
    '''
    pass

class ProdConfig(Config):
    '''
    production configuation child class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey=f9b3923ad99d4449b0e79a0241931c05'
    
class DevConfig(Config):
    '''
    development configuration  childclass
    '''
    pass

    DEBUG = True



