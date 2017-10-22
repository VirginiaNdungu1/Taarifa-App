import os


class Config:
    SOURCES_API_BASE_URL = 'https://newsapi.org/v1/sources?language=en&country=us&category={}&apiKey={}'
    ARTICLES_API_BASE_URL = 'https://newsapi.org/v1/articles?sortBy=top&source={}&apiKey={}'

    # set environment variables
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


# Create a dictionary to help us access different configuration option classes
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
