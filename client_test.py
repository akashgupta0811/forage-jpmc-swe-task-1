import unittest
from client3 import getDataPoint, getRatio  

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # Asserting the output of getDataPoint for each quote
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      self.assertEqual(stock, quote['stock'])
      self.assertEqual(bid_price, float(quote['top_bid']['price']))
      self.assertEqual(ask_price, float(quote['top_ask']['price']))
      self.assertEqual(price, (bid_price + ask_price) / 2)


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    # Asserting the output of getDataPoint for each quote
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      self.assertEqual(stock, quote['stock'])
      self.assertEqual(bid_price, float(quote['top_bid']['price']))
      self.assertEqual(ask_price, float(quote['top_ask']['price']))
      self.assertEqual(price, (bid_price + ask_price) / 2)


  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_handleZeroAskPrice(self):
    quotes = [
          {'top_ask': {'price': 0, 'size': 0}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'XYZ'},
          {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'PQR'}
    ]
    stock, bid_price, ask_price, price = getDataPoint(quotes[0])
    self.assertEqual(stock, 'XYZ')
    self.assertEqual(bid_price, 120.48)
    self.assertEqual(ask_price, 0)
    self.assertEqual(price, 0)

    stock, bid_price, ask_price, price = getDataPoint(quotes[1])
    self.assertEqual(stock, 'PQR')
    self.assertEqual(bid_price, 117.87)
    self.assertEqual(ask_price, 121.68)
    self.assertEqual(price, 119.775)

  def test_getRatio(self):
     # Test when price_b is zero
    ratio = getRatio(5, 0)
    self.assertEqual(ratio, 0)

    # Test when price_a is zero
    ratio = getRatio(0, 10)
    self.assertEqual(ratio, 0)

    # Test when both price_a and price_b are non-zero
    ratio = getRatio(8, 4)
    self.assertEqual(ratio, 2)


if __name__ == '__main__':
    unittest.main()
