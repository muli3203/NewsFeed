import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
Test class to test the behaviour if the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_news = 


    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if __name__ == '__main__':
unittest.main()    