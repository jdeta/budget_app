from django.test import TestCase
from finance_app.models import Stock, StockPrice


class StockTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Stock.objects.create(ticker='csco')

    def test_ticker_label(self):
        fake_stock = Stock.objects.get(pk=2)
        ticker_label = fake_stock._meta.get_field('ticker').verbose_name
        self.assertEqual(ticker_label, 'ticker')

    def test_ticker_string_output(self):
        fake_stock = Stock.objects.get(pk=2)
        self.assertEqual(fake_stock.ticker, str(fake_stock.ticker))

class StockPriceTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        msft = Stock.objects.create(ticker='msft')
        StockPrice.objects.create(stock=msft,price='50.00',date='2021-04-20')

    def test_stock_label(self):
        test_price = StockPrice.objects.get(pk=1)
        price_label = test_price._meta.get_field('price').verbose_name
        self.assertEqual(price_label, 'price')
