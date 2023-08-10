import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from customers_who_never_order import customers_who_never_order

class TestCustomersWhoNeverOrder(unittest.TestCase):
    def test_customers_who_never_order(self):
        # arrange
        customer_data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
        Customers = pd.DataFrame(customer_data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
        order_data = [[1, 3], [2, 1]]
        Orders = pd.DataFrame(order_data, columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})

        expected = pd.DataFrame(
        {"Customers" : ["Henry", "Max"]})

        #act
        actual = customers_who_never_order(Customers, Orders)

        #assert
        assert_frame_equal(expected, actual)