from django.db.models import Sum
from decimal import Decimal as dc
from .models import AssetAccount, Asset
import yfinance as yf
from decimal import Decimal as dc

def get_account_value(selected_account, all_assets):
    account_value = all_assets.aggregate(Sum('value'))['value__sum'] or dc(0.00)
    selected_account.value = account_value
    selected_account.save()

    return account_value


def update_stock_values(account_id):
    account_to_update = AssetAccount.objects.get(pk=account_id)
    account_assets = Asset.objects.filter(account=account_to_update)
    value_list = []

    for a in account_assets:
        s = yf.Ticker(a.ticker).info['currentPrice']
        a.price = s
        a.value = a.shares * dc(a.price)
        value_list.append(a.value)
        a.save()

    account_to_update.value = sum(value_list)
    account_to_update.save()
