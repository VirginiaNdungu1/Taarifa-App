import urllib.request
import json
from .models import newsSource

# Get the api key
apiKey = None
# Get the source base url
source_base_url = None


def configure_request(app):
    '''
    Function that takes in the application instance
    And Replaces the values of the None variables
    to application configuration objects
    '''
    global apiKey, source_base_url

    apiKey = app.config['NEWS_API_KEY']
    '''
    get the api key from the config object
    '''

    source_base_url = app.config['SOURCES_API_BASE_URL']
    '''
    get the News Sources Url from the config Object
    '''


def get_sources(category):
    '''
    Function that gets the json response to the ur request
    '''
    get_sources_url = source_base_url.format(category, apiKey)
    with urllib.request.urlopen(get_sources_url) as base_url:
        get_sources_data = base_url.read()
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
    for source in sources_list:
        id = source.get("id")
        name = source.get("name")
        url = source.get("url")
        description = source.get("description")

        if url:
            sources_object = newsSource(id, name, url, description)
            sources_results.append(sources_object)
    return sources_results
