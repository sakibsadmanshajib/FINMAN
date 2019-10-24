from django.shortcuts import render, redirect
from .models import Transaction, Account
from .forms import AddAccount, AddTransaction
# This decorator is used to make a view accessible by logged in users only.
from django.contrib.auth.decorators import login_required
# Importing Predefined User model from Django
from django.contrib.auth.models import User
# User Authication packages
from django.contrib.auth import authenticate, login, logout
# Importing Messages package i.e. for error messages
from django.contrib import messages
# Importing Predefined Signup Form
from django.contrib.auth.forms import UserCreationForm

""" 
    USER Authentication 
        user_login is used for login. It was copied from another code.
        user_register is used for registering new user. Probably doesn't work.
        user_logout is used for logging out user from session.
"""

# Start of User Authentication


def user_login(request):
    context = {}
    next = request.GET.get('next')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if next:
                return redirect(next)
            else:
                messages.success(request, "You have successfully logged in!")
                return redirect('backend:account')
        else:
            messages.error(request, "Provide valid credentials.")
            return render(request, 'auth/login.html')

    else:
        return render(request, 'auth/login.html', context)


def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('backend:profile')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})


def user_logout(request):
    messages.success(request, "You have been logged out!")
    logout(request)
    return redirect('auth:login')

# End of User Authentication


"""
    USER Profile
        - Usual informations such as name, email
        - Contains User Accounts
        - Contains User Transactions
"""


def profile(request, username):
    profile = User.objects.get(username=username)
    all_transaction_list = Transaction.objects.all()
    user_transaction = []
    for transaction in all_transaction_list:
        if transaction.user == profile.username:
            user_transaction.append(transaction)

    if user_transaction is None:
        messages.error(request, "No transaction exists in the system.")
        return render(request, 'user/profile.html', {'profile': profile, 'user_transaction': None})
    else:
        return render(request, 'user/profile.html', {'profile': profile, 'user_transaction': user_transaction})


"""
    Accounts:
        - Cash, Bank Account, Online Wallet, Blockchain Wallet.
        - A single account can have a single currency.
"""


def account(request):
    all_account_list = Account.objects.all()

    if all_account_list is None:
        messages.error(request, "No account exists in the system.")
        return render(request, 'account/account.html', {'account_list': None})
    else:
        return render(request, 'account/account.html', {'account_list': all_account_list})

# Account Profile Details: IT shows the account profile, amount it has, and all the transactions assosiated with it.


def account_details(request, account_id):
    acc = Account.objects.get(id=account_id)
    accnm = acc.name
    transaction_list = Transaction.objects.filter(account__icontains=accnm)
    USER = User.objects.all()

    if transaction_list is None:
        messages.error(request, "No transaction exists in the system.")
        return render(request, 'account/account_details.html', {'account': acc, 'account_transaction': None, 'users': USER})
    else:
        return render(request, 'account/account_details.html', {'account': acc, 'account_transaction': transaction_list, 'users': USER})

# Add a new account


def add_account(request):
    if request.method == 'POST':

        form = AddAccount(request.POST)
        if form.is_valid():
            account = Account(
                name=form.cleaned_data['name'],
                balance=form.cleaned_data['balance'],
                currency=form.cleaned_data['currency'],
                description=form.cleaned_data['description'],
            )
            account.save()
            messages.success(request, "Successfully added a new account!")
            return redirect('backend:account')
        else:
            messages.warning(request, "Couldn't add new account")
            return redirect('backend:account')

    else:
        form = AddAccount()
        return render(request, 'account/add_account.html', {'form': form})


"""
    Transactions:
        - Income, Expenditure and Transfers.
        * Add Transfers from one account to another, if the currency is different automatically calculate it.
"""


def transaction(request):
    all_transaction_list = Transaction.objects.all()
    USER = User.objects.all()

    if all_transaction_list is None:
        messages.error(request, "No transaction exists in the system.")
        return render(request, 'transaction/transaction.html', {'transaction_list': None, 'users': USER})
    else:
        return render(request, 'transaction/transaction.html', {'transaction_list': all_transaction_list, 'users': USER})

# Add a new transaction


def add_transaction(request):
    all_account_list = Account.objects.all()

    if request.method == 'POST':

        form = AddTransaction(request.POST)
        if form.is_valid():
            account = Account.objects.get(id=form.cleaned_data['accountID'])
            usernm = request.user.username
            user = User.objects.get(username=usernm)
            print(account)
            print(user)
            transaction = Transaction(
                timestamp=form.cleaned_data['timestamp'],
                account=account.name,
                user=form.cleaned_data['user'],
                type=form.cleaned_data['type'],
                amount=form.cleaned_data['amount'],
                remark=form.cleaned_data['remark'],
            )
            if form.cleaned_data['type'] == 'Debit':
                account.balance -= form.cleaned_data['amount']
                user.extended.total_debit += form.cleaned_data['amount']
            elif form.cleaned_data['type'] == 'Credit':
                account.balance += form.cleaned_data['amount']
                user.extended.total_credit += form.cleaned_data['amount']
            account.save()
            transaction.save()
            user.save()
            messages.success(request, "Successfully added a new transaction!")
            return redirect('backend:transaction')
        else:
            messages.warning(request, "Couldn't add new transaction")
            return redirect('backend:transaction')

    else:
        form = AddTransaction()
        return render(request, 'transaction/add_transaction.html', {'form': form, 'account_list': all_account_list})
