from django.db import models


class Role(models.Model):
    role_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.role_name


class Status(models.Model):
    status_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.status_name


class Category(models.Model):
    category_name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.category_name


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=200, unique=True)
    contact_person = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.supplier_name


class Item(models.Model):
    item_name = models.CharField(max_length=200)
    sku = models.CharField(max_length=50, unique=True, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='items')
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True, related_name='items')
    unit_of_measure = models.CharField(max_length=50, help_text="e.g., kg, liters, boxes, pieces")
    current_stock = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    minimum_stock = models.DecimalField(max_digits=10, decimal_places=2, default=10.00)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['item_name']

    def __str__(self):
        return f"{self.item_name} ({self.current_stock} {self.unit_of_measure})"


class Staff(models.Model):
    employee_number = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, related_name='staff_members')
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='staff_members')
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    photo = models.ImageField(upload_to='staff/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.employee_number} - {self.last_name}, {self.first_name}"


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('IN', 'Stock In (Delivery/Restock)'),
        ('OUT', 'Stock Out (Usage/Wastage)'),
    ]
    item = models.ForeignKey(Item, on_delete=models.PROTECT, related_name='transactions')
    staff = models.ForeignKey(Staff, on_delete=models.PROTECT, related_name='transactions')
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-transaction_date']

    def __str__(self):
        return f"{self.transaction_type} - {self.quantity} of {self.item.item_name} by {self.staff.last_name}"