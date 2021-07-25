from django.shortcuts import render, redirect, get_object_or_404
from .models import Account
from .forms import NewAccountForm

def finance_dashboard(request):
    accounts = Account.objects.all()
    context = {'accounts':accounts}
    return render(request, 'finance_app/finance_dashboard.html', context)

def add_account(request):
    if request.method == "POST":
        account_form = NewAccountForm(request.POST)

        if account_form.is_valid():
            account_added = account_form.save(commit=False)
            account_added.value = 0.00
            account_added.save()
            return redirect('/finance')

    else:
        account_form = NewAccountForm()
        return render(request, 'finance_app/account_new.html', {'account_form': account_form})

def account_detail(request, account_id):
    specific_account = get_object_or_404(Account, pk=account_id)
    context = {'specific_account':specific_account}

    return render(request, 'finance_app/account_detail.html', context)

