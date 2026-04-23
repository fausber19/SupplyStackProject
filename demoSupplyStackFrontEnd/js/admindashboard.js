const API_BASE = "http://127.0.0.1:8000/api/";

let chartInstance = null;

function loadStaff() {
    fetch(API_BASE + "staff/")
    .then(res => res.json())
    .then(data => {
        document.getElementById("total-staff").innerText = data.length;
        const body = document.getElementById("staff-body");
        body.innerHTML = "";
        data.forEach(s => {
            body.innerHTML += `
                <tr>
                    <td>${s.id}</td>
                    <td>${s.employee_number}</td>
                    <td>${s.first_name} ${s.last_name}</td>
                    <td>${s.role_name}</td>
                    <td>${s.status_name}</td>
                </tr>
            `;
        });
    });
}

function loadItems() {
    fetch(API_BASE + "items/")
    .then(res => res.json())
    .then(data => {
        const body = document.getElementById("items-body");
        const lowStockBody = document.getElementById("lowstock-body");

        body.innerHTML = "";
        lowStockBody.innerHTML = "";

        let totalStock = 0;
        let lowStock = 0;

        data.forEach(i => {
            const stock = parseFloat(i.current_stock);
            const min = parseFloat(i.minimum_stock);

            totalStock += stock;

            const isLow = stock <= min;
            if (isLow) lowStock++;

            const rowHTML = `
                <tr class="${isLow ? 'low-stock' : ''}">
                   <td>${i.id}</td>
                   <td>${i.item_name}</td>
                   <td>${i.category_name}</td>
                   <td>${i.supplier_name ?? ""}</td>
                   <td><strong>${i.current_stock}</strong></td>
                   <td>${i.minimum_stock}</td>
                   <td>
                       <button onclick="updateStock(${i.id}, ${i.current_stock})" style="background:#f39c12; color:white; border:none; padding:5px 10px; border-radius:5px; margin-right:5px;">Edit Stock</button>
                       <button onclick="deleteItem(${i.id})" style="background:#e74c3c; color:white; border:none; padding:5px 10px; border-radius:5px;">Delete</button>
                   </td>
                </tr>
           `;

           body.innerHTML += rowHTML;

           if (isLow) {
               lowStockBody.innerHTML += rowHTML;
           }
        });

        document.getElementById("total-items").innerText = data.length;
        document.getElementById("total-stock").innerText = totalStock;
        document.getElementById("low-stock").innerText = lowStock;
        document.getElementById("sidebar-low-badge").innerText = lowStock;
    });
}

function loadTransactions() {
    fetch(API_BASE + "transactions/")
    .then(res => res.json())
    .then(data => {
        document.getElementById("total-transactions").innerText = data.length;

        const body = document.getElementById("transactions-body");
        body.innerHTML = "";

        data.forEach(t => {
            body.innerHTML += `
                <tr>
                    <td>${t.id}</td>
                    <td>${t.item_name}</td>
                    <td>${t.staff_name}</td>
                    <td>${t.transaction_type_display}</td>
                    <td>${t.quantity}</td>
                    <td>${new Date(t.transaction_date).toLocaleString()}</td>
                </tr>
            `;
        });

        loadChart(data);
    });
}

function loadChart(data) {
    let inCount = 0;
    let outCount = 0;

    data.forEach(t => {
        if (t.transaction_type === "IN") inCount++;
        else outCount++;
    });

    const ctx = document.getElementById("transactionChart").getContext("2d");

    if (chartInstance) chartInstance.destroy();

    chartInstance = new Chart(ctx, {
        type: "doughnut",
        data: {
            labels: ["IN", "OUT"],
            datasets: [{
                data: [inCount, outCount]
            }]
        }
    });
}

function loadItemsDropdown() {
    fetch(API_BASE + "items/")
    .then(res => res.json())
    .then(data => {
        const select = document.getElementById("item-id");
        select.innerHTML = "";
        data.forEach(i => {
            select.innerHTML += `<option value="${i.id}">${i.item_name}</option>`;
        });
    });
}

function loadStaffDropdown() {
    fetch(API_BASE + "staff/")
    .then(res => res.json())
    .then(data => {
        const select = document.getElementById("staff-id");
        select.innerHTML = "";
        data.forEach(s => {
            select.innerHTML += `<option value="${s.id}">${s.first_name} ${s.last_name}</option>`;
        });
    });
}

function addTransaction() {
    const item = document.getElementById("item-id").value;
    const staff = document.getElementById("staff-id").value;
    const type = document.getElementById("type").value;
    const qty = document.getElementById("qty").value;

    fetch(API_BASE + "transactions/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            item: parseInt(item),
            staff: parseInt(staff),
            transaction_type: type,
            quantity: parseFloat(qty)
        })
    })
    .then(res => res.json())
    .then(() => {
        alert("Transaction added!");
        loadTransactions();
        loadItems();
    });
}

function updateStock(id, currentStock) {
    const newStock = prompt("Enter the new correct stock quantity:", currentStock);

    if (newStock === null || newStock === "") return;

    fetch(API_BASE + "items/" + id + "/", {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ current_stock: parseFloat(newStock) })
    })
    .then(res => {
        if (res.ok) {
            alert("Stock updated successfully!");
            loadItems();
        } else {
            alert("Error updating stock.");
        }
    });
}

function deleteItem(id) {
    if (!confirm("Are you sure you want to permanently delete this item?")) return;

    fetch(API_BASE + "items/" + id + "/", {
        method: "DELETE"
    })
    .then(res => {
        if (res.ok) {
            alert("Item deleted successfully!");
            loadItems();
        } else {
            alert("Error deleting item.");
        }
    });
}

function loadCategoriesDropdown() {
    fetch(API_BASE + "categories/")
    .then(res => res.json())
    .then(data => {
        const select = document.getElementById("item-category-input");
        select.innerHTML = '<option value="">Select Category</option>';
        data.forEach(c => {
            select.innerHTML += `<option value="${c.id}">${c.category_name}</option>`;
        });
    });
}

function loadSuppliersDropdown() {
    fetch(API_BASE + "suppliers/")
    .then(res => res.json())
    .then(data => {
        const select = document.getElementById("item-supplier-input");
        select.innerHTML = '<option value="">Select Supplier</option>';
        data.forEach(s => {
            select.innerHTML += `<option value="${s.id}">${s.supplier_name}</option>`;
        });
    });
}

function addNewIngredient() {
    const name = document.getElementById("item-name-input").value;
    const sku = document.getElementById("item-sku-input").value;
    const cat = document.getElementById("item-category-input").value;
    const sup = document.getElementById("item-supplier-input").value;
    const uom = document.getElementById("item-uom-input").value;
    const stock = document.getElementById("item-stock-input").value;
    const min = document.getElementById("item-min-input").value;

    if(!name || !sku || !cat || !stock || !min) {
        alert("Please fill in Name, SKU, Category, Stock, and Min Stock.");
        return;
    }

    fetch(API_BASE + "items/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            item_name: name,
            sku: sku,
            category: parseInt(cat),
            supplier: sup ? parseInt(sup) : null,
            unit_of_measure: uom,
            current_stock: parseFloat(stock),
            minimum_stock: parseFloat(min)
        })
    })
    .then(res => {
        if(res.ok) {
            alert("New ingredient added successfully!");
            document.querySelectorAll('#items-section input').forEach(input => input.value = '');
            loadItems();
        } else {
            alert("Error adding ingredient. Ensure SKU is unique.");
        }
    });
}

window.onload = function() {
   loadStaff();
   loadItems();
   loadTransactions();
   loadItemsDropdown();
   loadStaffDropdown();
   loadCategoriesDropdown();
   loadSuppliersDropdown();
};