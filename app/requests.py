import urllib.request
import json
from .models import newsSource

# Get the api key
apiKey = None
# Get the source base url
source_base_url = None


def configure_request(app):
    global apiKey, source_base_url
    apiKey = app.config['NEWS_API_KEY']
    source_base_url = app.config['SOURCES_API_BASE_URL']
