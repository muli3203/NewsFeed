class Sources:
    '''
    a class that defines source class 
    '''
    def __init__ (self,id,name,description,url,category,country):
        self.id = id
        self.name = name
        self.description = description
        self.url= url
        self.category= category
        self.country = country


class Articles:
    '''
    a class that defines article object
    '''
    def __init__(self,id,author,description,url,urlToImage,publishedAt):
        self.id = id
        self.author= author
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
    

    
