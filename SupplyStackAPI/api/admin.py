from django.contrib import admin
from .models import Role, Status, Category, Supplier, Item, Staff, Transaction

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'role_name', 'description')
    search_fields = ('role_name',)

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status_name')
    search_fields = ('status_name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'description')
    search_fields = ('category_name',)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'supplier_name', 'contact_person', 'email', 'phone')
    search_fields = ('supplier_name', 'contact_person')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'item_name',
        'sku',
        'category',
        'current_stock',
        'minimum_stock',
        'unit_of_measure',
        'last_updated'
    )
    search_fields = ('item_name', 'sku')
    list_filter = ('category', 'supplier')

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'employee_number',
        'last_name',
        'first_name',
        'role',
        'status'
    )
    search_fields = ('employee_number', 'last_name', 'first_name', 'email')
    list_filter = ('role', 'status')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'transaction_type',
        'item',
        'quantity',
        'staff',
        'transaction_date'
    )
    search_fields = ('item__item_name', 'staff__last_name')
    list_filter = ('transaction_type',)