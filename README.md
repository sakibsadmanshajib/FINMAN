# FINMAN

An app developed to keep record of the income and expenditure of someone.

- The plan is to create an android app which will help keep record of all your transactions and give you a daily, weekly, bi-weekly or monthly report.

- Inspired by the Apple Card's App which gives you detailed view of where you've spend your money and when.

- It'll keep track of how much money a person have iun which account and they can make transactions from each account.

- Future plan is to add data-minig capabilties to seemlessly adding transactions without the interaction of the user from Mobile phone's SMS or user's email.

# Technologies used

- Django - python web framework

# Disclaimer

Well, I did test it, but I can tell there are so manny security holes, bugs. Extra points if you can make the backend better as well.

# How to Run this API

1. Install `python` and `virtualenv` on linux system or `anaconda` on your windows system.
2. Create an environment and install the requirements using `pip install -r requirements.txt`.
3. Migrate using `python manage.py makemigrations backend` and `python manage.py migrate`
4. Create a superuser using `python manage.py createsuperuser`.
5. Run this command to start the server. `python manage.py runserver` adn the API will be available at http://localhost:8000/.
6. Get a token from http://localhost:8000/get-token/ by sending a POST request like this one.
    ```
    {
        "username": "your_superuser_username",
        "password": "your_superuser_password"
    }
    ```
7. For Authentication, use the token as a Header Key: Value \
    `Authorization: Token user_token_collected_from_get-token`
Read more about it in Django Rest Frameworks' documentation.


# Variables in Models
- Account
    - user: Put the request.user.id
    - name: Name to identify the account
    - type: 
    ```
            {
                'Cash': 'Cash',
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
    - remark: Ask the user for input

# API Endpoints
    base = http://localhost:8000/
    Use this reference: https://bezkoder.com/django-rest-api/
    1. Getting Tokens from username and password:
        url = base + get-token
        POST request
        ```
        {
            "username": "your_username",
            "password": "your_password"
        }
        ```
    2. Changing Password:
        url = base + change-password
        PUT request
        ```
        {
            "old_password": "your_old_password",
            "new_password": "your_new_password"
        }
        ```
    3. Create new user:
        url = base + register
        POST request
        ```
        {
            "username": "their_username",
            "password": "their_password"
        }
        ```
    4. extention of user:
        url = base + extended
    5. list or retrive userid:
        url = base + userid
            search parameters:
                url + ?user=<username>
    6. account:
        url = base + account
    7. bankaccount:
        url = base + bankaccount
            search parameters:
                url + ?account_id=<account.id found from 6>
    8. digitalwallet:
        url = base + digitalwallet
            search parameters:
                url + ?account_id=<account.id found from 6>
    9. transaction:
        url = base + transaction
            search parameters:
                url + ?account_id=<account.id found from 6>