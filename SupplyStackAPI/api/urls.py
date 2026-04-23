from django.urls import path
from .views import (
    RoleListAPIView, RoleDetailAPIView,
    StatusListAPIView, StatusDetailAPIView,
    CategoryListAPIView, CategoryDetailAPIView,
    SupplierListAPIView, SupplierDetailAPIView,
    ItemListAPIView, ItemDetailAPIView,
    StaffListAPIView, StaffDetailAPIView,
    TransactionListAPIView, TransactionDetailAPIView,
)

urlpatterns = [
    # list and create endpoints (GET all, POST)
    path('roles/', RoleListAPIView.as_view(), name='role-list'),
    path('status/', StatusListAPIView.as_view(), name='status-list'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('suppliers/', SupplierListAPIView.as_view(), name='supplier-list'),
    path('items/', ItemListAPIView.as_view(), name='item-list'),
    path('staff/', StaffListAPIView.as_view(), name='staff-list'),
    path('transactions/', TransactionListAPIView.as_view(), name='transaction-list'),

    # detail, update, and delete endpoints (GET one, PUT, PATCH, DELETE)
    path('roles/<int:pk>/', RoleDetailAPIView.as_view(), name='role-detail'),
    path('status/<int:pk>/', StatusDetailAPIView.as_view(), name='status-detail'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('suppliers/<int:pk>/', SupplierDetailAPIView.as_view(), name='supplier-detail'),
    path('items/<int:pk>/', ItemDetailAPIView.as_view(), name='item-detail'),
    path('staff/<int:pk>/', StaffDetailAPIView.as_view(), name='staff-detail'),
    path('transactions/<int:pk>/', TransactionDetailAPIView.as_view(), name='transaction-detail'),
]