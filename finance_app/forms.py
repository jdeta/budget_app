from django import forms
from .models import AssetAccount, Asset

class NewAccountForm(forms.ModelForm):

    class Meta:
        model = AssetAccount
        fields = ('name', 'category',)

class NewAssetForm(forms.ModelForm):

    class Meta:
        model = Asset
        fields = ('ticker',)
