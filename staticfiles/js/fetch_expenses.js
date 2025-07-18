document.addEventListener("DOMContentLoaded", function(){
    fetchExpenses();
});

function fetchExpenses(){
fetch("http://127.0.0.1:8000/api/expenses/")
.then(response => response.json())
.then(data => {
    let tableBody = document.getElementById("expense-table-body");
    tableBody.innerHTML = "";

    data.forEach(expense => {
        let row = document.createElement("tr");

        row.innerHTML = `
        <td>${expense.title}</td>
        <td>${expense.amount}</td>
        <td>${expense.category.name}</td>
        <td>${expense.date}</td>
        `;

        tableBody.appendChild(row);
        
    });
})
.catch(error => console.error("Error fetching expenses:",error));
}