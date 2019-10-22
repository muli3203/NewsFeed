from flask import render_template,request,redirect,url_for
from . import main 
from ..request import get_source,get_article


@main.route('/')
def index():
    
    '''
    function returns indexpage and its data
    '''

    return render_template('index.html')

@main.route('/newssource')
def newssource():
    
    '''
    fuction returns index page and its data
    '''

    return render_template('newssource.html',sources = news_sources)

@main.route('/newsarticle')
def newsarticle():
    '''
    returns index page and its data
    '''

    return render_template('newsarticle.html', articles = news_articles)

