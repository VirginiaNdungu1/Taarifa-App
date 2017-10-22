class news_source:
    '''
    News Source Class to define News Source Objects
    '''

    def __init__(self, id, name, homepage_url, description):
        self.id = id
        self.name = name
        self.homepage_url = homepage_url
        self.description = description
        # self.logo = logo


class Articles:
    '''
    Articles class to define Source's Articles Objects
    '''

    def __init__(self, author, title, description, article_url, logo, publishedAt):
        # self.source_id = source
        self.author = author
        self.title = title
        self.description = description
        self.article_url = article_url
        self.logo = logo
        self.publishedAt = publishedAt
