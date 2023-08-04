import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from big_countries import big_countries

class TestBigCountries(unittest.TestCase):
    def test_big_contries(self):
        # arrange
        world = pd.DataFrame(
        {"name" : ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola"],
        "continent" : ["Asia", "Europe", "Africa", "Europe", "Africa"],
        "population" : [25500100, 2831741, 37100000, 78115, 20609294],
        "area" : [652230, 28748, 2381741, 468, 1246700],
        "gdp" : [20343000000, 12960000000, 188681000000, 3712000000, 100990000000]})

        expected = pd.DataFrame(
        {"name" : ["Afghanistan", "Algeria"],
        "population" : [25500100, 37100000],
        "area" : [652230, 2381741]})

        #act
        actual = big_countries(world)

        #assert
        assert_frame_equal(expected, actual)