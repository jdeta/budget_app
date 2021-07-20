from django.contrib import admin
from .models import Stock, StockPrice, Account, StockAsset, AccountHistory

my_models = [Stock, StockPrice, Account, StockAsset, AccountHistory]
admin.site.register(my_models)

