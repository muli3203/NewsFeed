from app import app 
import urllib.request,json
from .models import news

Articles = news.Articles
Sources= news.Sources

api_key= app.config['NEWS_API_KEY']
# Getting the movie base url
base_url = app.config['NEWS_API_BASE_URL']

def get_sources(category):
    '''
    a function that get responses from the api
    '''
    get_source_url = base_url.format(category,api_key)
    
    with urllib.request.urlopen(get_source_url) as url:
        source_data = url.read()
        get_source_response = json.loads(source_data)

        sources_outcome = None

        if get_source_response['sources']:
            sources_outcome_list = get_source_response['sources']
            sources_outcome = process_new_sources(sources_outcome_list)

    return sources_outcome

def process_new_sources(sources_list):
    sources_outcome = []


    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')


        new_sources = Sources(id,name,description,url,category,country)
        sources_outcome.append(new_sources)

    return sources_outcome
