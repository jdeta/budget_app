from django.db.models import Sum
from decimal import Decimal as dc

def get_account_value(selected_account, all_assets):
    account_value = all_assets.aggregate(Sum('value'))['value__sum'] or dc(0.00)
    selected_account.value = account_value
    selected_account.save()

    return account_value


