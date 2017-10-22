import urllib.request
import json
from .models import news_source, Articles

# Get the api key
apiKey = None
# Get the source base url
source_base_url = None

articles_base_url = None


def configure_request(app):
    '''
    Function that takes in the application instance
    And Replaces the values of the None variables
    to application configuration objects
    '''
    global apiKey, source_base_url, articles_base_url

    apiKey = app.config['NEWS_API_KEY']
    '''
    get the api key from the config object
    '''

    source_base_url = app.config['SOURCES_API_BASE_URL']
    '''
    get the News Sources Url from the config Object
    '''

    articles_base_url = app.config['ARTICLES_API_BASE_URL']
    '''
    get the source's article url from the config object
    '''


def get_sources(category):
    '''
    Function that gets the json response to the url request
    '''
    get_sources_url = source_base_url.format(category, apiKey)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)

    return sources_results


def process_results(sources_list):
    '''
    Function that processes the sources result and transform them to a list of Objects

    Args:
    sources_list: a list of dictionaries that contain source details

    Returns:
    sources_results: A list of source Objects
    '''
    sources_results = []
    for source_item in sources_list:
        id = source_item.get("id")
        name = source_item.get("name")
        url = source_item.get("url")
        description = source_item.get("description")

        sources_object = news_source(id, name, url, description)
        sources_results.append(sources_object)

    return sources_results


def get_sources_articles(id):
    '''
    Function that get's the json response to the url request
    '''
    get_articles_url = articles_base_url.format(id, apiKey)
    with urllib.request.urlopen(get_articles_url) as url:
        get_article_data = url.read()
        get_articles_response = json.loads(get_article_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_article_results(articles_results_list)

    return articles_results


def process_article_results(articles_list):
    articles_results = []
    for article_item in articles_list:
        # source = article_item.get("source")
        author = article_item.get("author")
        title = article_item.get("title")
        description = article_item.get("description")
        article_url = article_item.get("url")
        logo = article_item.get("urlToImage")
        publishedAt = article_item.get("publishedAt")
        articles_object = Articles(
            author, title, description, article_url, logo, publishedAt)
        articles_results.append(articles_object)

    return articles_results
