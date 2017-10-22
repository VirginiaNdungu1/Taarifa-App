import unittest

from app.models import Articles


class SourceTest(unittest.TestCase):
    def setUp(self):
        self.new_article = Articles(
            "bluebird", "The Bluebird", "The Eastern Bluebird is a small thrush with a big, rounded head, large eye, plump body, and alert posture",  "https://techcrunch.com/2017/10/21/antisocial-media/", "https://tctechcrunch2011.files.wordpress.com/2017/10/img_6450.jpg", "2017-10-21T11:00:53Z")

    def test_article_instance(self):
        self.assertTrue(self.new_article, Articles)
