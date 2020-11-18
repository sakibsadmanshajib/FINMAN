from rest_framework import routers
from .api import *
from django.urls import path
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register('extended', ExtendedViewSet, 'extended')
router.register('userid', UserIDViewSet, 'userid')
router.register('account', AccountViewSet, 'account')
router.register('bankaccount', BankAccountViewSet, 'bankaccount')
router.register('digitalwallet', DigitalWalletViewSet, 'digitalwallet')
router.register('transaction', TransactionViewSet, 'transaction')

urlpatterns = router.urls

urlpatterns += [
    path('get-token/', views.obtain_auth_token),
    path('change-password/', ChangePasswordViewSet.as_view(), name='change-password'),
    path('register/', UserCreateViewSet.as_view())
]