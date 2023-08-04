import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from recyclable_and_low_fat_products import find_products



class TestRecyclableAndLowFatProducts(unittest.TestCase):
    def test_find_products(self):
        # arrange

        products_table = pd.DataFrame(
        {"product_id" : [0, 1, 2, 3, 4],
        "low_fats" : ["Y", "Y", "N", "Y", "N"],
        "recyclable" : ["N", "Y", "Y", "Y", "N"]})

        expected = pd.DataFrame(
        {"product_id" : [1, 3]})

        #act
        actual = find_products(products_table)

        #assert
        assert_frame_equal(expected, actual)
