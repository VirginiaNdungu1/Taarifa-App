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

    def __init__(self, source_id, author, title, description, logo, publishedAt):
        self.source_id = source_id
        self.author = author
        self.title = title
        self.description = title
        self.logo = 'https://cdn0.tnwcdn.com/wp-content/blogs.dir/1/files/2017/10/' + logo
        self.publishedAt = publishedAt
