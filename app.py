// ----- BOOK DATA -----
let books = [
    { id: 1, title: 'The Alchemist', author: 'Paulo Coelho', price: 10 },
    { id: 2, title: 'Harry Potter', author: 'J.K. Rowling', price: 15 },
    { id: 3, title: 'Clean Code', author: 'Robert C. Martin', price: 25 },
    { id: 4, title: 'Atomic Habits', author: 'James Clear', price: 12 },
    { id: 5, title: 'The Hobbit', author: 'J.R.R. Tolkien', price: 18 },
    { id: 6, title: '1984', author: 'George Orwell', price: 14 },
    { id: 7, title: 'To Kill a Mockingbird', author: 'Harper Lee', price: 16 },
    { id: 8, title: 'The Great Gatsby', author: 'F. Scott Fitzgerald', price: 13 },
    { id: 9, title: 'Sapiens', author: 'Yuval Noah Harari', price: 20 },
    { id: 10, title: 'The Catcher in the Rye', author: 'J.D. Salinger', price: 11 },
    { id: 11, title: 'The Lord of the Rings', author: 'J.R.R. Tolkien', price: 22 },
    { id: 12, title: 'The Pragmatic Programmer', author: 'Andrew Hunt', price: 28 },
    { id: 13, title: 'Deep Work', author: 'Cal Newport', price: 18 },
    { id: 14, title: 'Thinking, Fast and Slow', author: 'Daniel Kahneman', price: 19 },
    { id: 15, title: 'Meditations', author: 'Marcus Aurelius', price: 9 }
];

let cart = [];

// ----- ADD NEW BOOK -----
function addBook() {
    const title = document.getElementById('bookTitle').value.trim();
    const author = document.getElementById('bookAuthor').value.trim();
    const price = parseFloat(document.getElementById('bookPrice').value);

    if (!title || !author || isNaN(price)) {
        alert('Please fill all fields correctly.');
        return;
    }

    books.push({ id: Date.now(), title, author, price });
    document.getElementById('bookTitle').value = '';
    document.getElementById('bookAuthor').value = '';
    document.getElementById('bookPrice').value = '';
    renderBooks();
}

// ----- RENDER BOOK LIST -----
function renderBooks() {
    const tbody = document.getElementById('bookList');
    tbody.innerHTML = '';
    const search = document.getElementById('searchInput').value.toLowerCase();

    books
        .filter(b => b.title.toLowerCase().includes(search))
        .forEach(book => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${book.title}</td>
                <td>${book.author}</td>
                <td>$${book.price.toFixed(2)}</td>
                <td><button onclick="addToCart(${book.id})">Add to Cart</button></td>
            `;
            tbody.appendChild(tr);
        });
}

// ----- ADD TO CART -----
function addToCart(bookId) {
    const book = books.find(b => b.id === bookId);
    if (!book) return;
    cart.push(book);
    renderCart();
}

// ----- RENDER CART -----
function renderCart() {
    const tbody = document.getElementById('cartList');
    tbody.innerHTML = '';
    let total = 0;

    cart.forEach((book, index) => {
        total += book.price;
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${book.title}</td>
            <td>$${book.price.toFixed(2)}</td>
            <td><button onclick="removeFromCart(${index})">Remove</button></td>
        `;
        tbody.appendChild(tr);
    });

    document.getElementById('totalPrice').textContent = total.toFixed(2);
}

// ----- REMOVE FROM CART -----
function removeFromCart(index) {
    cart.splice(index, 1);
    renderCart();
}

// ----- CHECKOUT -----
function checkout() {
    if (cart.length === 0) {
        alert('Cart is empty!');
        return;
    }
    alert(`Checkout successful! Total: $${cart.reduce((sum, b) => sum + b.price, 0).toFixed(2)}`);
    cart = [];
    renderCart();
}

// ----- SEARCH -----
document.getElementById('searchInput').addEventListener('input', renderBooks);

// ----- INITIAL RENDER -----
renderBooks();
