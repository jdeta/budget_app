from django.db import models
from django.urls import reverse
from datetime import date


class Value(models.Model):
    value = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        abstract = True


class AssetAccount(Value):
    class AccountTypes(models.IntegerChoices):
        brokerage = 1, 'Brokerage Account'
        trad_IRA = 2, 'Traditional IRA'
        roth_IRA = 3, 'Roth IRA'
        hsa = 4, 'Health Savings Account'
        trad_401 = 5, 'Traditional 401k'
        roth_401 = 6, 'Roth 401k'
        coll_529 = 7, '529 College Savings Account'


    name = models.CharField(max_length=64)
    category = models.PositiveSmallIntegerField(choices=AccountTypes.choices,
                                                default=AccountTypes.brokerage)
    

    def get_absolute_url(self):
        return reverse('finance_app:account-detail', kwargs={'account_id':self.id})

    def __str__(self):
        return f'{self.name} {self.category}'

class Asset(Value):
    ticker = models.CharField(max_length=5)
    shares = models.DecimalField(max_digits=20, decimal_places=3)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    account = models.ForeignKey(AssetAccount, on_delete=models.CASCADE)
    
class AccountHistory(Value):
    account = models.ForeignKey(AssetAccount, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    class Meta:
        get_latest_by = 'date'
