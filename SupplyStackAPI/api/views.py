from rest_framework import generics
from .models import (
    Role,
    Status,
    Category,
    Supplier,
    Item,
    Staff,
    Transaction
)
from .serializers import (
    RoleSerializer,
    StatusSerializer,
    CategorySerializer,
    SupplierSerializer,
    ItemSerializer,
    StaffSerializer,
    TransactionSerializer
)

# list & create views (GET all, POST)

class RoleListAPIView(generics.ListCreateAPIView):
    queryset = Role.objects.all().order_by('id')
    serializer_class = RoleSerializer

class StatusListAPIView(generics.ListCreateAPIView):
    queryset = Status.objects.all().order_by('id')
    serializer_class = StatusSerializer

class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by('category_name')
    serializer_class = CategorySerializer

class SupplierListAPIView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all().order_by('supplier_name')
    serializer_class = SupplierSerializer

class ItemListAPIView(generics.ListCreateAPIView):
    queryset = Item.objects.select_related('category', 'supplier').all().order_by('item_name')
    serializer_class = ItemSerializer

class StaffListAPIView(generics.ListCreateAPIView):
    queryset = Staff.objects.select_related('role', 'status').all().order_by('last_name', 'first_name')
    serializer_class = StaffSerializer

class TransactionListAPIView(generics.ListCreateAPIView):
    queryset = Transaction.objects.select_related('item', 'staff').all().order_by('-transaction_date')
    serializer_class = TransactionSerializer

# detail, update & delete views (GET one, PUT, PATCH, DELETE)

class RoleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SupplierDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class ItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class StaffDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class TransactionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer