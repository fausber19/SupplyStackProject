from rest_framework import serializers
from .models import Role, Status, Category, Supplier, Item, Staff, Transaction

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    # this pulls the actual names instead of just showing the ID number
    category_name = serializers.CharField(source='category.category_name', read_only=True)
    supplier_name = serializers.CharField(source='supplier.supplier_name', read_only=True)

    class Meta:
        model = Item
        fields = [
            'id',
            'item_name',
            'sku',
            'category',
            'category_name',
            'supplier',
            'supplier_name',
            'unit_of_measure',
            'current_stock',
            'minimum_stock',
            'last_updated'
        ]

class StaffSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(source='role.role_name', read_only=True)
    status_name = serializers.CharField(source='status.status_name', read_only=True)

    class Meta:
        model = Staff
        fields = [
            'id',
            'employee_number',
            'last_name',
            'first_name',
            'role',
            'role_name',
            'status',
            'status_name',
            'email',
            'phone',
            'photo',
            'created_at'
        ]


class TransactionSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.item_name', read_only=True)
    staff_name = serializers.CharField(source='staff.last_name', read_only=True)
    transaction_type_display = serializers.CharField(source='get_transaction_type_display', read_only=True)

    class Meta:
        model = Transaction
        fields = [
            'id',
            'item',
            'item_name',
            'staff',
            'staff_name',
            'transaction_type',
            'transaction_type_display',
            'quantity',
            'transaction_date',
            'notes'
        ]

    def create(self, validated_data):
        transaction = super().create(validated_data)

        item = transaction.item

        if transaction.transaction_type == 'IN':
            item.current_stock += transaction.quantity
        elif transaction.transaction_type == 'OUT':
            item.current_stock -= transaction.quantity

        item.save()

        return transaction