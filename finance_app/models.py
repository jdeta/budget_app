from django.db import models
from datetime import date


class Stock(models.Model):
    ticker = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.ticker

class StockPrice(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='prices')
    date = models.DateField(default=date.today, db_index=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    
class Account(models.Model):
    name = models.CharField(max_length=64)
    value = models.DecimalField(max_digits=20, decimal_places=2)

    def get_absolute_url(self):
        return reverse('account-detail', kwargs={'id':self.id})

    def __str__(self):
        return self.name

class StockAsset(models.Model):
    shares = models.DecimalField(max_digits=20, decimal_places=3)
    price = models.ForeignKey(StockPrice, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    
class AccountHistory(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateField(default=date.today)
