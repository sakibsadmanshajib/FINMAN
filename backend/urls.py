from django.urls import path
from . import views

app_name = 'backend'

urlpatterns = [

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('account/', views.account, name='account'),
    path('account/add', views.add_account, name='add_account'),
    path('account/<int:account_id>', views.account_details, name='account_details'),
    path('transaction/', views.transaction, name='transaction'),
    path('transaction/add', views.add_transaction, name='add_transaction'),
    path('user/<str:username>', views.profile, name='profile'),

]
