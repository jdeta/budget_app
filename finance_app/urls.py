from django.urls import path
from . import views


app_name = 'finance_app'
urlpatterns = [
        path('', views.finance_dashboard, name='finance-dashboard'),
        path('update', views.update_all_accounts, name='update-all'),
        path('account/new', views.add_account, name='new_account'),
        path('account/newmonth/<int:account_id>', views.new_month, name='new-month'),
        path('account/delete/<int:account_id>', views.delete_account, name='delete-account'),
        path('account/<int:account_id>', views.account_detail, name='account-detail'),
        path('account/<int:account_id>/new_asset', views.new_asset, name='asset_new'),
        path('account/<int:account_id>/update', views.update_account, name='update-account'),
        path('account/<int:account_id>/asset/<int:asset_id>', views.delete_asset, name='delete-asset'),
        ]
