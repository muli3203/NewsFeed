import unittest
from models import news
News = news.News

class SourceTest(unittest.TestCase):
    '''
Test class to test the behaviour if the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_news = Sources()


    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

class ArticleTest(unittest.TestCase)
    



if __name__ == '__main__':
unittest.main()    