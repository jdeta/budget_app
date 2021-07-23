from django import forms
from .models import Account

class NewAccountForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('name',)

