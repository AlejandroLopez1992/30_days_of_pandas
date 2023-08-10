import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from article_views_1 import article_views

class TestArticleViews1(unittest.TestCase):
    def test_article_views(self):
        # arrange
        data = [[1, 3, 5, '2019-08-01'], [1, 3, 6, '2019-08-02'], [2, 7, 7, '2019-08-01'], [2, 7, 6, '2019-08-02'], [4, 7, 1, '2019-07-22'], [3, 4, 4, '2019-07-21'], [3, 4, 4, '2019-07-21']]
        Views = pd.DataFrame(data, columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype({'article_id':'Int64', 'author_id':'Int64', 'viewer_id':'Int64', 'view_date':'datetime64[ns]'})


        expected = pd.DataFrame(
        {"id" : [4, 7]}).astype({'id':'Int64'})

        #act
        actual = article_views(Views)

        #assert
        assert_frame_equal(expected, actual)