from django.db import models


class Stock(models.Model):
    ticker = models.Charfield(max_length=10, unique=True)

    def __str__(self):
        return self.ticker_symbol

class StockPrice(models.Model):
    stock = models.ForeignKey(Stock, related_name='prices')
    date = models.DateTimeField(db_index=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    
class Account(models.Model):
    name = models.Charfield(max_length=64)
    value = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.name

class StockAsset(models.Model):
    shares = models.DecimalField(max_digits=20, decimal_places=3)
    price = models.ForeignKey(StockPrice)
    account = models.ForeignKey(Account)
    
class AccountHistory(models.Model):
    account = models.ForeignKey(Account
    value = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.Datefield(default=date.today)
