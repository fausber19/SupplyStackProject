function showSection(section) {
   document.getElementById("staff-section").style.display = "none";
   document.getElementById("items-section").style.display = "none";
   document.getElementById("transactions-section").style.display = "none";
   document.getElementById("lowstock-section").style.display = "none";

   document.getElementById(section + "-section").style.display = "block";
}

function searchTable(input, tableId) {
   const filter = input.value.toLowerCase();
   const rows = document.querySelectorAll(`#${tableId} tr`);
   rows.forEach(row => {
       row.style.display = row.innerText.toLowerCase().includes(filter) ? "" : "none";
    });
}