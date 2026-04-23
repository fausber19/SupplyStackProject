from django.core.management.base import BaseCommand
from api.models import Role, Status, Category, Supplier, Item, Staff


class Command(BaseCommand):
    help = "Insert Supply Stack demo seed data"

    def handle(self, *args, **kwargs):
        roles = ["Admin", "Head Chef", "Inventory Manager", "Kitchen Staff"]
        role_objs = {}
        for r in roles:
            obj, created = Role.objects.get_or_create(role_name=r)
            role_objs[r] = obj
        self.stdout.write(self.style.SUCCESS("Roles inserted"))

        statuses = ["Active", "Inactive", "On Leave"]
        status_objs = {}
        for s in statuses:
            obj, created = Status.objects.get_or_create(status_name=s)
            status_objs[s] = obj
        self.stdout.write(self.style.SUCCESS("Status inserted"))

        categories = ["Meat & Poultry", "Seafood", "Fresh Produce", "Dairy", "Dry Goods"]
        category_objs = {}
        for c in categories:
            obj, created = Category.objects.get_or_create(category_name=c)
            category_objs[c] = obj
        self.stdout.write(self.style.SUCCESS("Categories inserted"))

        suppliers = [
            {"name": "Prime Meats Co.", "contact": "James Adams", "phone": "09171112222"},
            {"name": "Fresh Valley Farms", "contact": "Carlos Sainz", "phone": "09173334444"},
            {"name": "City Wholesale Grocers", "contact": "Nate Jacobs", "phone": "09175556666"}
        ]
        supplier_objs = {}
        for sup in suppliers:
            obj, created = Supplier.objects.get_or_create(
                supplier_name=sup["name"],
                defaults={"contact_person": sup["contact"], "phone": sup["phone"]}
            )
            supplier_objs[sup["name"]] = obj
        self.stdout.write(self.style.SUCCESS("Suppliers inserted"))

        items = [
            # Meat & Poultry
            {"name": "Ribeye Steak", "sku": "MT-001", "category": "Meat & Poultry", "supplier": "Prime Meats Co.",
             "uom": "kg", "stock": 25.5, "min": 10.0},
            {"name": "Chicken Breast", "sku": "MT-002", "category": "Meat & Poultry", "supplier": "Prime Meats Co.",
             "uom": "kg", "stock": 45.0, "min": 15.0},
            {"name": "Ground Beef (80/20)", "sku": "MT-003", "category": "Meat & Poultry",
             "supplier": "Prime Meats Co.", "uom": "kg", "stock": 18.0, "min": 10.0},
            {"name": "Pork Belly", "sku": "MT-004", "category": "Meat & Poultry",
             "supplier": "Prime Meats Co.", "uom": "kg", "stock": 20.0, "min": 10.0},
            {"name": "Wagyu Cubes", "sku": "MT-005", "category": "Meat & Poultry",
             "supplier": "Prime Meats Co.", "uom": "kg", "stock": 15.0, "min": 10.0},
            {"name": "Wagyu Striploin", "sku": "MT-006", "category": "Meat & Poultry",
             "supplier": "Prime Meats Co.", "uom": "kg", "stock": 25.0, "min": 10.0},
            {"name": "Free range Eggs", "sku": "MT-007", "category": "Meat & Poultry",
             "supplier": "Prime Meats Co.", "uom": "kg", "stock": 9.0, "min": 10.0}, # low stock

            # Seafood
            {"name": "Salmon Fillets", "sku": "SF-001", "category": "Seafood", "supplier": "Prime Meats Co.",
             "uom": "kg", "stock": 8.0, "min": 15.0},  # low stock
            {"name": "Tiger Prawns", "sku": "SF-002", "category": "Seafood", "supplier": "Prime Meats Co.", "uom": "kg",
             "stock": 12.0, "min": 10.0},
            {"name": "Mud Crabs", "sku": "SF-003", "category": "Seafood", "supplier": "Prime Meats Co.", "uom": "kg",
             "stock": 20.0, "min": 10.0},
            {"name": "Tuna Fillet", "sku": "SF-004", "category": "Seafood", "supplier": "Prime Meats Co.", "uom": "kg",
             "stock": 25.0, "min": 10.0},
            {"name": "American Lobster", "sku": "SF-005", "category": "Seafood", "supplier": "Prime Meats Co.", "uom": "kg",
             "stock": 30.0, "min": 12.5},

            # Fresh Produce
            {"name": "Roma Tomatoes", "sku": "PR-001", "category": "Fresh Produce", "supplier": "Fresh Valley Farms",
             "uom": "kg", "stock": 40.0, "min": 20.0},
            {"name": "White Onions", "sku": "PR-002", "category": "Fresh Produce", "supplier": "Fresh Valley Farms",
             "uom": "kg", "stock": 35.0, "min": 15.0},
            {"name": "Garlic (Peeled)", "sku": "PR-003", "category": "Fresh Produce", "supplier": "Fresh Valley Farms",
             "uom": "kg", "stock": 4.0, "min": 5.0}, # low stock
            {"name": "Iceberg Lettuce", "sku": "PR-004", "category": "Fresh Produce", "supplier": "Fresh Valley Farms",
             "uom": "heads", "stock": 24.0, "min": 12.0},
            {"name": "Red Onions", "sku": "PR-005", "category": "Fresh Produce", "supplier": "Fresh Valley Farms",
             "uom": "kg", "stock": 10.0, "min": 12.0},

            # Dairy
            {"name": "Whole Milk", "sku": "DY-001", "category": "Dairy", "supplier": "City Wholesale Grocers",
             "uom": "liters", "stock": 30.0, "min": 20.0},
            {"name": "Unsalted Butter", "sku": "DY-002", "category": "Dairy", "supplier": "City Wholesale Grocers",
             "uom": "blocks", "stock": 45.0, "min": 20.0},
            {"name": "Sharp Cheddar Cheese", "sku": "DY-003", "category": "Dairy", "supplier": "City Wholesale Grocers",
             "uom": "blocks", "stock": 18.0, "min": 10.0},
            {"name": "Salted Butter", "sku": "DY-004", "category": "Dairy", "supplier": "City Wholesale Grocers",
             "uom": "blocks", "stock": 35.0, "min": 10.0},
            {"name": "Shredded Parmesan Cheese", "sku": "DY-005", "category": "Dairy", "supplier": "City Wholesale Grocers",
             "uom": "kg", "stock": 18.0, "min": 10.0},

            # Dry Goods
            {"name": "All-Purpose Flour", "sku": "DG-001", "category": "Dry Goods",
             "supplier": "City Wholesale Grocers", "uom": "sacks", "stock": 12.0, "min": 5.0},
            {"name": "Extra Virgin Olive Oil", "sku": "DG-002", "category": "Dry Goods",
             "supplier": "City Wholesale Grocers", "uom": "liters", "stock": 15.0, "min": 10.0},
            {"name": "Spaghetti Pasta", "sku": "DG-003", "category": "Dry Goods", "supplier": "City Wholesale Grocers",
             "uom": "packs", "stock": 60.0, "min": 30.0},
            {"name": "Kosher Salt", "sku": "DG-004", "category": "Dry Goods", "supplier": "City Wholesale Grocers",
             "uom": "kg", "stock": 22.0, "min": 10.0},
            {"name": "Black Pepper", "sku": "DG-005", "category": "Dry Goods", "supplier": "City Wholesale Grocers",
             "uom": "kg", "stock": 31.0, "min": 10.0}
        ]

        for i in items:
            Item.objects.get_or_create(
                sku=i["sku"],
                defaults={
                    "item_name": i["name"],
                    "category": category_objs[i["category"]],
                    "supplier": supplier_objs[i["supplier"]],
                    "unit_of_measure": i["uom"],
                    "current_stock": i["stock"],
                    "minimum_stock": i["min"]
                }
            )
        self.stdout.write(self.style.SUCCESS("Items inserted"))

        staff_members = [
            {"emp_num": "EMP-001", "last": "Ramsay", "first": "Gordon", "role": "Head Chef",
             "email": "gordon@supplystack.com"},
            {"emp_num": "EMP-002", "last": "Ibay", "first": "Sean", "role": "Inventory Manager",
             "email": "sean@supplystack.com"},
            {"emp_num": "EMP-003", "last": "Bernabe", "first": "Faustin", "role": "Kitchen Staff",
             "email": "faustin@supplystack.com"},
            {"emp_num": "EMP-004", "last": "Arca", "first": "Jaden", "role": "Kitchen Staff",
             "email": "jaden@supplystack.com"},
            {"emp_num": "EMP-005", "last": "Voce", "first": "Samantha", "role": "Kitchen Staff",
             "email": "samantha@supplystack.com"}
        ]
        for staff in staff_members:
            Staff.objects.get_or_create(
                employee_number=staff["emp_num"],
                defaults={
                    "last_name": staff["last"],
                    "first_name": staff["first"],
                    "role": role_objs[staff["role"]],
                    "status": status_objs["Active"],
                    "email": staff["email"]
                }
            )
        self.stdout.write(self.style.SUCCESS("Staff inserted"))
        self.stdout.write(self.style.SUCCESS("DONE: Supply Stack Database Seeded!"))