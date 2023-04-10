
// Add an item
function addItem() {
    var item = document.getElementById('item').value;
    fetch('/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({item: item})
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        updateList();
        item.value=="";
    })
    .catch(error => {
        console.error(error);
        alert('An error occurred while adding the item.');
    });
}

// Update List
function updateList() {
    fetch('/list')
        .then(response => response.json())
        .then(data => {
            console.log(data);
            var todoList = document.getElementById('todoList');
            todoList.innerHTML = '';
            data.forEach(item => {
                var li = document.createElement('li');
                li.textContent = item+'   ';
                var deleteBtn = document.createElement('button');
                deleteBtn.textContent = 'Delete';
                deleteBtn.addEventListener('click', function() {
                    deleteItem(item);
                });
                li.appendChild(deleteBtn);
                todoList.appendChild(li);
            });
        })
        .catch(error => {
            console.error(error);
            alert('An error occurred while fetching the to-do list.');
        });
}

// Delete an item
function deleteItem(item) {
    fetch('/remove', {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({item: item})
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        updateList();
    })
    .catch(error => {
        console.error(error);
        alert('An error occurred while deleting the item.');
    });
}

// Update the list when the page first loads
updateList();