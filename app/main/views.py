from flask import render_template, request, url_for
from . import main
from ..requests import get_sources

# views
# get sources view Function


@main.route("/")
def index():
    '''
    View Root Page Function returns index page and it's data
    '''
    # print("Sources")
    politics_sources = get_sources('politics')
    print(politics_sources)
    technology_sources = get_sources('technology')
    business_sources = get_sources('business')
    entertainment_sources = get_sources('entertainment')
    science_sources = get_sources('science-and-nature')
    music_sources = get_sources('music')
    sport_sources = get_sources('sport')

    title = 'Welcome to Global News Source Site'
    return render_template('index.html', title=title, politics=politics_sources, technology=get_sources, business=business_sources, entertainment=entertainment_sources, science=science_sources, music=music_sources, sport=sport_sources)
