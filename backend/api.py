
from backend.models import *
from rest_framework import viewsets, permissions, status, generics
from .serializer import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from django.contrib.auth.models import User

class ChangePasswordViewSet(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserCreateViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class UserIDViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserIDSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        TokenAuthentication
    ]
    def get_queryset(self):
        queryset = User.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = User.objects.filter(username=user)
        return queryset

class ExtendedViewSet(viewsets.ModelViewSet):
    queryset = Extended.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        TokenAuthentication
    ]
    serializer_class = ExtendedSerializer

class AccountViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        TokenAuthentication
    ]
    serializer_class = AccountSerializer

    def get_queryset(self):
        queryset = Account.objects.filter(user=self.request.user.id)
        return queryset

class BankAccountViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        TokenAuthentication
    ]
    serializer_class = BankAccountSerializer

    def get_queryset(self):
        queryset = BankAccount.objects.all()
        account_id = self.request.query_params.get('account_id', None)
        if account_id is not None:
            queryset = BankAccount.objects.filter(account=account_id)
        return queryset

class DigitalWalletViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        TokenAuthentication
    ]
    serializer_class = DigitalWalletSerializer

    def get_queryset(self):
        queryset = DigitalWallet.objects.all()
        account_id = self.request.query_params.get('account_id', None)
        if account_id is not None:
            queryset = DigitalWallet.objects.filter(account=account_id)
        return queryset

class TransactionViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    authentication_classes = [
        TokenAuthentication
    ]
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = Transaction.objects.all()
        account_id = self.request.query_params.get('account_id', None)
        if account_id is not None:
            queryset = queryset.filter(account_id=account_id, user=self.request.user.id)
        else:
            queryset = queryset.filter(user=self.request.user.id)
        return queryset
