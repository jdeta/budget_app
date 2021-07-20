from django.test import TestCase
from finance_app.models import Stock, StockPrice, Account, StockAsset, AccountHistory

class StockTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Stock.objects.create(ticker='csco')

    def test_ticker_label(self):
        test_stock = Stock.objects.get(pk=1)
        ticker_label = test_stock._meta.get_field('ticker').verbose_name
        self.assertEqual(ticker_label, 'ticker')

class StockPriceTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cisco = Stock.objects.create(ticker='csco')
        StockPrice.objects.create(stock=cisco,date='2021-04-20', price='40.00')

    def test_date_label(self):
        test_stock = StockPrices.objects.get(pk=1)
        date_label = test_stock._meta.get_field('date').verbose_name
        self.assertEqual(date_label, 'date')

    def test_stock_label(self):
        test_stock = StockPrices.objects.get(pk=1)
        stock_label = test_stock._meta.get_field('stock').verbose_name
        self.assertEqual(stock_label, 'stock')

    def test_price_label(self):
        test_stock = StockPrices.objects.get(pk=1)
        price_label = test_stock._meta.get_field('price').verbose_name
        self.assertEqual(price_label, 'price')

    def test_price_max_digits(self):
        test_stock = StockPrices.objects.get(pk=1)
        price_digits = test_stock._meta.get_field('price').max_digits
        self.assertEqual(price_digits, 20)

class AccountTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Account.objects.create(name='401k',value='1000.00')

    def test_name_label(self):
        test_account = Account.objects.get(pk=1)
        name_label = test_account._meta.get_field('name').verbose_name
        self.assertEqual(name_label, 'name')

    def test_value_label(self):
        test_account = Account.objects.get(pk=1)
        value_label = test_account._meta.get_field('value').verbose_name
        self.assertEqual(value_label, 'value')

    def test_value_max_digits(self):
        test_account = Account.objects.get(pk=1)
        value_digits = value_stock._meta.get_field('value').max_digits
        self.assertEqual(value_digits, 20)
