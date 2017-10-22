import unittest

from app.models import news_source


class SourceTest(unittest.TestCase):
    def setUp(self):
        self.new_source = news_source(
            "blues", "bluespage", "http://www.abc.net.au/news", "Because the skies are blue tonight")

    def test_source_instance(self):
        self.assertTrue(self.new_source, news_source)
