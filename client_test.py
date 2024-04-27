import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        stock, top_bid_price, top_ask_price, calculated_price = getDataPoint(quote)
        self.assertEqual(stock, quote['stock'])
        self.assertEqual(top_bid_price, quote['top_bid']['price'])
        self.assertEqual(top_ask_price, quote['top_ask']['price'])
        self.assertEqual(calculated_price, (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)
    # Test for ABC stock
    data_point_ABC = getDataPoint(quotes[0])
    self.assertEqual(data_point_ABC, ('ABC', 120.48, 121.2, 120.84))

    # Test for DEF stock
    data_point_DEF = getDataPoint(quotes[1])
    self.assertEqual(data_point_DEF, ('DEF', 117.87, 121.68, 119.775))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock, top_bid_price, top_ask_price, calculated_price = getDataPoint(quote)
      self.assertEqual(stock, quote['stock'])
      self.assertEqual(top_bid_price, quote['top_bid']['price'])
      self.assertEqual(top_ask_price, quote['top_ask']['price'])
      self.assertEqual(calculated_price, (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)
  """ ------------ Add more unit tests ------------ """
  def test_getRatio(self):
        # Test for ratio when price_b is not zero
        price_a = 100
        price_b = 50
        self.assertEqual(getRatio(price_a, price_b), 2.0)

        # Test for ratio when price_b is zero
        price_a = 100
        price_b = 0
        self.assertEqual(getRatio(price_a, price_b), None)  # Assert that it returns None
        
        # Test for ratio when price_a is zero
        price_a = 0
        price_b = 50
        self.assertEqual(getRatio(price_a, price_b), 0.0)

        # Test for ratio when price_a is negative
        price_a = -100
        price_b = 50
        self.assertEqual(getRatio(price_a, price_b), -2.0)

        # Test for ratio when both prices are negative
        price_a = -100
        price_b = -50
        self.assertEqual(getRatio(price_a, price_b), 2.0)

if __name__ == '__main__':
    unittest.main()
