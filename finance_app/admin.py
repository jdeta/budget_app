from django.contrib import admin
from .models import Asset, AssetAccount, AccountHistory

admin.site.register(AssetAccount)
admin.site.register(Asset)
admin.site.register(AccountHistory)
