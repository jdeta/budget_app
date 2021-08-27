from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Expense, Transaction
from .forms import NewTransactionForm, NewExpenseForm, UpdateAllocationForm, NewCategoryForm
from datetime import date, timedelta
from decimal import Decimal as dc
from .utils import update_expense, latest_months_expenses, new_month

def budget_dashboard(request):
    expenses = latest_months_expenses()
    total_transactions = Transaction.objects.all().aggregate(Sum('inflow'))['inflow__sum'] or dc(0.00)
    total_allocations = expenses.aggregate(Sum('allocated'))['allocated__sum'] or dc(0.00)
    unbudgeted = total_transactions - total_allocations
    context = {
            'expenses':expenses,
            'unbudgeted':unbudgeted,
    }

    return render(request, 'budget_app/dashboard.html', context)


def new_transaction(request):
    if request.method == 'POST':
        transaction_form = NewTransactionForm(request.POST)


        if transaction_form.is_valid():
            transaction_added = transaction_form.save(commit=False)
            update_expense(transaction_added)
            transaction_added.save()
            return redirect('/')

    else:
        transaction_form = NewTransactionForm()
        category_form = NewCategoryForm()
        context = {
            'transaction_form': transaction_form,
            'category_form': category_form
            }
        return render(request, 'budget_app/transaction_new.html', context)


def new_expense(request):
    if request.method == 'POST':
        expense_form = NewExpenseForm(request.POST)

        if expense_form.is_valid():
            expense = expense_form.save(commit=False)
            expense.allocated = 0.00
            expense.disbursed = 0.00
            expense.remaining = 0.00
            expense.month = expense.month.replace(day=1)
            expense.save()
            return redirect('/')

    else:
        category_form = NewCategoryForm()
        expense_form = NewExpenseForm()
        return render(request, 'budget_app/expense_new.html', {'expense_form': expense_form, 'category_form':category_form})


def expense_detail(request, expense_id):
    specific_expense = get_object_or_404(Expense, pk=expense_id)

    if request.method == 'POST':
        allocated_form = UpdateAllocationForm(request.POST)

        if allocated_form.is_valid():
            specific_expense.allocated = specific_expense.allocated + allocated_form.cleaned_data['allocate']
            specific_expense.remaining = specific_expense.allocated - specific_expense.disbursed
            specific_expense.save()
            return redirect('/')
    else:
        allocated_form = UpdateAllocationForm()
        related_transactions = Transaction.objects.filter(category=specific_expense.category)
        context = {
                'specific_expense':specific_expense,
                'allocated_form':allocated_form,
                'related_transactions':related_transactions
                }
        return render(request, 'budget_app/expense_detail.html', context)

def new_category_transaction(request):
    if request.method == 'POST':
        category_form = NewCategoryForm(request.POST)

        if category_form.is_valid():
            category_form.save()
            return redirect('budget_app:new_transaction')

    else:
        category_form = NewCategoryForm()
        return render(request, 'budget_app/category_new.html', {'category_form':category_form})

def new_category_expense(request):
    if request.method == 'POST':
        category_form = NewCategoryForm(request.POST)

        if category_form.is_valid():
            category_form.save()
            return redirect('budget_app:new_expense')

    else:
        category_form = NewCategoryForm()
        return render(request, 'budget_app/category_new.html', {'category_form':category_form})

def transaction_detail(request):
    monthly_transactions = Transaction.objects.all()
    return render(request, 'budget_app/transaction_detail.html', {'monthly_transactions':monthly_transactions})

def del_expense(request, expense_id):#needs DELETE method added
    to_delete = get_object_or_404(Expense, pk=expense_id).delete()
    return redirect('/')

def add_next_month(request):
    if request.method == "POST":
        new_month()
        return redirect('/')
    else:
        return redirect('/')
