from django.urls import path
from . import views


app_name = 'finance_app'
urlpatterns = [
        path('', views.finance_dashboard, name='finance_dashboard'),
        path('account/new', views.add_account, name='new_account'),
        path('account/<int:account_id>/', views.account_detail, name='account-detail'),
        path('account/<int:account_id>/new_asset/', views.new_asset, name='asset_new'),
        ]
