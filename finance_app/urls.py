from django.urls import path
from . import views


app_name = 'finance_app'
urlpatterns = [
        path('', views.finance_dashboard, name='finance_dashboard'),
        path('finance/account/new', views.add_account, name='new_account'),
        ]
