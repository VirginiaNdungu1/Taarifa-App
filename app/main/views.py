from flask import render_template, request, url_for
from . import main
from ..request import get_sources

# views
# get sources view Function


@main.route("/")
def index():
    '''
    View Root Page Function returns index page and it's data
    '''
    politics_sources = get_sources('en', 'politics', 'us')
    technology_sources = get_sources('en', 'technology', 'us')
    business_sources = get_sources('en', 'business', 'us')
    entertainment_sources = get_sources('en', 'entertainment', 'us')
    science_sources = get_sources('en', 'science-and-nature', 'us')
    music_sources = get_sources('fr', 'music', 'us')
    sport_sources = get_sources('en', 'sport', 'us')

    title = 'Welcome to Global News Source Site'
