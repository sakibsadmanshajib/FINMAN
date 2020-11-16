# FINMAN

An app developed to keep record of the income and expenditure of someone.

- The plan is to create an android app which will help keep record of all your transactions and give you a daily, weekly, bi-weekly or monthly report.

- Future plan is to add data-minig capabilties to seemlessly adding transactions without the interaction of the user.

# Technologies used

- Django - python web framework

# Disclaimer

I haven't tested the api after writing it.

# How to Run this API

1. Install `python` and `virtualenv` on linux system or `anaconda` on your windows system.
2. Create an environment and install the requirements using `pip install -r requirements.txt`.
3. Migrate using `python manage.py makemigrations` and `python manage.py migrate`
4. Create a superuser using `python manage.py createsuperuser`.
5. Run this command to start the server. `python manage.py runserver` adn the API will be available at http://localhost:8000/.
6. Get a token from http://localhost:8000/get-token/.
    ```
    {
        "username": "your_superuser_username",
        "password": "your_superuser_password"
    }
    ```
7. For Authentication, use the token as a Header
    Key: Value
    Authorization: Token user_token_collected_from_get-token


# Variables in Models
- Account
    - user: Put the request.user.id
    - name: Name to identify the account
    - type: 
    ```
            {
                'Bank' : 'Ask the user if they want to fillup the BankAccount Model and pass the Account.id to account.',
                'Digital Wallet' : Ask the user if they want to fillup DigitalWallet Model and pass the Account.id to account.'
            }
    ```
    - balance: opening balance
    - currency: 
    ```
            {
                'BDT',
                'USD'
            }
    ```
- BankAccount
    - account: Put an account.id depending on what the user has selected in Account.type
    - bankName: Bank Name
    - bankBranch: Bank Branch
    - bankAccountType: 
    ```
            {
                'Current',
                'Savings',
            }
    ```
    - bankAccountName: Bank Account Name
    - bankAccountNumber: Bank Account Number

- DigitalWallet
    - account: Put an account.id depending on what the user has selected in Account.type
    - serviceName: 
    ```
            {
                'bKash',
                'UCash',
                'Rocket',
                'Nagad'
            }
    ```
    - serviceID: Phone Number of the Digital Wallet

- Transaction
    - user: Put the request.user.id
    - account: Put an account.id on which the transaction will be made
    - type: 
    ```
            {
                'Debit': deduct money from account,
                'credit': add money to account
            }
    ```
    - amount: Amount
    - reason: 
    ```
    {
            if debit: {
                'Food',
                'Gift',
                'Loan',
                'Rent',
                'Utility',
                'Transportation',
                'Medical',
                'Insurance',
                'Supplies',
                'Savings',
                'Personal',
                'Temp'
                }
            if credit: {
                'Salary',
                'Share Dividend',
                'Contract',
                'Gift',
                'Loan',
                'Temp'
                }
            }
    ```
    - reason: Ask the user for input