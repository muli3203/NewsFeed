from flask import render_template
from app import app
from .request import get_sources


@app.route('/')
def index():
    '''
    Views thats renders news sources to the home page
    '''
    general_news = get_sources('general')
    business_news = get_sources('business')
    sport_news = get_sources('sports')
    
    return render_template('index.html',general = general_news,business=business_news,sports=sport_news)
