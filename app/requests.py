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


def get_sources(language, category, country):
    '''
    Function that gets the json response to the ur request
    '''
    get_sources_url = base_url.format(language, category, country, apiKey)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None
        if get_sources_response['results']:
            sources_results_list = get_sources_response['results']
            sources_results = process_results(sources_results_list)

    return sources_results
