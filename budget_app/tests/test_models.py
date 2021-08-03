from django.test import TestCase
from datetime import date

from budget_app.models import Expense, Transaction, Category


class ExpenseModelTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        #sample data for running tests
        test_category = Category.objects.create(name='mortgage')
        Expense.objects.create(month ='2021-04-01', category=test_category, allocated=600, disbursed=0, remaining=600)

    def test_month_label(self):
        expense_item = Expense.objects.get(pk=1)
        month_label = expense_item._meta.get_field('month').verbose_name
        self.assertEqual(month_label, 'month')

    def test_category_label(self):
        expense_item = Expense.objects.get(pk=1)
        category_label = expense_item._meta.get_field('category').verbose_name
        self.assertEqual(category_label, 'category')

    def test_allocated_label(self):
        expense_item = Expense.objects.get(pk=1)
        allocated_label = expense_item._meta.get_field('allocated').verbose_name
        self.assertEqual(allocated_label, 'allocated')

    def test_disbursed_label(self):
        expense_item = Expense.objects.get(pk=1)
        disbursed_label = expense_item._meta.get_field('disbursed').verbose_name
        self.assertEqual(disbursed_label, 'disbursed')

    def test_remaining_label(self):
        expense_item = Expense.objects.get(pk=1)
        remaining_label = expense_item._meta.get_field('remaining').verbose_name
        self.assertEqual(remaining_label, 'remaining')

    def test_allocated_max_digits(self):
         expense_item = Expense.objects.get(pk=1)
         allocated_digits = expense_item._meta.get_field('allocated').max_digits
         self.assertEqual(allocated_digits, 8)

    def test_disbursed_max_digits(self):
         expense_item = Expense.objects.get(pk=1)
         disbursed_digits = expense_item._meta.get_field('disbursed').max_digits
         self.assertEqual(disbursed_digits, 8)

    def test_remaining_max_digits(self):
         expense_item = Expense.objects.get(pk=1)
         remaining_digits = expense_item._meta.get_field('remaining').max_digits
         self.assertEqual(remaining_digits, 8)


class TransactionModelsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        #sample data for running tests
        test_category = Category.objects.create(name='paycheck')
        Transaction.objects.create(
                date='2021-04-01',
                category=test_category,
                recipient='me',
                inflow=2000,
                outflow=0,
                note='bi-weekly paycheck'
                )

    def test_date_label(self):
        fake_transaction = Transaction.objects.geto(pk=1)
        date_label = fake_transaction._meta.get_field('date').verbose_name
        self.assertEqual(date_label, 'date')

    def test_recipient_label(self):
        fake_transaction = Transaction.objects.get(pk=1)
        recipient_label = fake_transaction._meta.get_field('recipient').verbose_name
        self.assertEqual(recipient_label, 'recipient')

    def test_category_label(self):
        fake_transaction = Transaction.objects.get(pk=1)
        category_label = fake_transaction._meta.get_field('category').verbose_name
        self.assertEqual(category_label, 'category')

    def test_inflow_label(self):
        fake_transaction = Transaction.objects.get(pk=1)
        inflow_label = fake_transaction._meta.get_field('inflow').verbose_name
        self.assertEqual(inflow_label, 'inflow')

    def test_outflow_label(self):
        fake_transaction = Transaction.objects.get(pk=1)
        outflow_label = fake_transaction._meta.get_field('outflow').verbose_name
        self.assertEqual(outflow_label, 'outflow')

    def test_note_label(self):
        fake_transaction = Transaction.objects.get(pk=1)
        note_label = fake_transaction._meta.get_field('note').verbose_name
        self.assertEqual(note_label, 'note')

    def test_inflow_max_digits(self):
         fake_transaction = Transaction.objects.get(pk=1)
         inflow_digits = fake_transaction._meta.get_field('inflow').max_digits
         self.assertEqual(inflow_digits, 8)

    def test_outflow_max_digits(self):
         fake_transaction = Transaction.objects.get(pk=1)
         outflow_digits = fake_transaction._meta.get_field('outflow').max_digits
         self.assertEqual(outflow_digits, 8)

    def test_recipient_max_length(self):
        fake_transaction = Transaction.objects.get(pk=1)
        recipient_length = fake_transaction._meta.get_field('recipient').max_length
        self.assertEqual(recipient_length, 64)

    def test_recipient_str_output(self):
        fake_transaction = Transaction.objects.get(pk=1)
        self.assertEqual(fake_transaction.recipient, str(fake_transaction.recipient))

    def test_note_string_output(self):
        fake_transaction = Transaction.objects.get(pk=1)
        self.assertEqual(fake_transaction.note, str(fake_transaction.note))

class CategoryModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='mortgage')

    def test_category_label(self):
        test_category = Category.objects.get(pk=1)
        category_label = test_category._meta.get_field('name').verbose_name
        self.assertEqual(category_label, 'name')

    def test_category_length(self):
        test_category = Category.objects.get(pk=1)
        category_length = test_category._meta.get_field('name').max_length
        self.assertEqual(category_length, 64)

    def test_category_string_output(self):
        test_category = Category.objects.get(pk=1)
        self.assertEqual(test_category.name, str(test_category.name))

