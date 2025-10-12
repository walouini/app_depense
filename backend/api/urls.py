from django.urls import path
from .views import TransactionCreateView, TransactionRetrieveUpdateDestroyView

urlpatterns = [
    path('transactions', TransactionCreateView.as_view(), name='transaction-create'),
    path('transactions/<uuid:id>', TransactionRetrieveUpdateDestroyView.as_view(), name='transaction-detail'),
]