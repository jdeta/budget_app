from django.test import TestCase
from finance_app.models import Account, Stock, StockPrice, AccountHistory, StockAsset

class AccountTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.obj_id = Account.objects.create(name='401k',value='1000.00').pk

    def test_name_label(self):
        test_account = Account.objects.get(pk=self.obj_id)
        name_label = test_account._meta.get_field('name').verbose_name
        self.assertEqual(name_label, 'name')

    def test_value_label(self):
        test_account = Account.objects.get(pk=self.obj_id)
        value_label = test_account._meta.get_field('value').verbose_name
        self.assertEqual(value_label, 'value')

    def test_value_max_digits(self):
        test_account = Account.objects.get(pk=self.obj_id)
        value_digits = test_account._meta.get_field('value').max_digits
        self.assertEqual(value_digits, 20)

    def test_name_string_output(self):
        test_account = Account.objects.get(pk=self.obj_id)
        self.assertEqual(test_account.name, str(test_account.name))

class AccountHistoryTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_account = Account.objects.create(name='401k',value='1000.00')
        cls.obj_id = AccountHistory.objects.create(account=test_account, value='1000.00',date='2021-04-20').pk

    def test_account_label(self):
        test_history = AccountHistory.objects.get(pk=self.obj_id)
        account_label = test_history._meta.get_field('account').verbose_name
        self.assertEqual(account_label, 'account')

    def test_value_label(self):
        test_history = AccountHistory.objects.get(pk=self.obj_id)
        value_label = test_history._meta.get_field('value').verbose_name
        self.assertEqual(value_label, 'value')

    def test_date_label(self):
        test_history = AccountHistory.objects.get(pk=self.obj_id)
        date_label = test_history._meta.get_field('date').verbose_name
        self.assertEqual(date_label, 'date')

    def test_value_max_digits(self):
        test_history = AccountHistory.objects.get(pk=self.obj_id)
        value_digits = test_history._meta.get_field('value').max_digits
        self.assertEqual(value_digits, 20)

class StockAssetTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_account = Account.objects.create(name='401k',value='1000.00')
        test_stock = Stock.objects.create(ticker='csco')
        test_price = StockPrice.objects.create(stock=test_stock,price=100.00,date='2021-04-20')
        cls.obj_id = StockAsset.objects.create(shares=1.001,account=test_account,price=test_price).pk

    def test_shares_label(self):
        test_asset = StockAsset.objects.get(pk=self.obj_id)
        shares_label = test_asset._meta.get_field('shares').verbose_name
        self.assertEqual(shares_label, 'shares')

    def test_price_label(self):
        test_asset = StockAsset.objects.get(pk=self.obj_id)
        price_label = test_asset._meta.get_field('price').verbose_name
        self.assertEqual(price_label, 'price')

    def test_account_label(self):
        test_asset = StockAsset.objects.get(pk=self.obj_id)
        account_label = test_asset._meta.get_field('account').verbose_name
        self.assertEqual(account_label, 'account')

    def test_shares_max_digits(self):
        test_asset = StockAsset.objects.get(pk=self.obj_id)
        shares_digits = test_asset._meta.get_field('shares').max_digits
        self.assertEqual(shares_digits, 20)

class StockPriceTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cisco = Stock.objects.create(ticker='csco')
        cls.obj_id = StockPrice.objects.create(stock=cisco,date='2021-04-20', price='40.00').pk

    def test_date_label(self):
        test_stock = StockPrice.objects.get(pk=self.obj_id)
        date_label = test_stock._meta.get_field('date').verbose_name
        self.assertEqual(date_label, 'date')

    def test_stock_label(self):
        test_stock = StockPrice.objects.get(pk=self.obj_id)
        stock_label = test_stock._meta.get_field('stock').verbose_name
        self.assertEqual(stock_label, 'stock')

    def test_price_label(self):
        test_stock = StockPrice.objects.get(pk=self.obj_id)
        price_label = test_stock._meta.get_field('price').verbose_name
        self.assertEqual(price_label, 'price')

    def test_price_max_digits(self):
        test_stock = StockPrice.objects.get(pk=self.obj_id)
        price_digits = test_stock._meta.get_field('price').max_digits
        self.assertEqual(price_digits, 20)


class StockTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.obj_id = Stock.objects.create(ticker='msft').pk

    def test_ticker_label(self):
        fake_stock = Stock.objects.get(pk=self.obj_id)
        ticker_label = fake_stock._meta.get_field('ticker').verbose_name
        self.assertEqual(ticker_label, 'ticker')

    def test_ticker_string_output(self):
        fake_stock = Stock.objects.get(pk=self.obj_id)
        self.assertEqual(fake_stock.ticker, str(fake_stock.ticker))
