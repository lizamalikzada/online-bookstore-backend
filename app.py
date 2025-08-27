from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)  # Enable CORS so frontend can access backend

DB_NAME = "books.db"

# Initialize Database
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT,
            price REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM books")
    books = [{"id": row[0], "title": row[1], "author": row[2], "price": row[3]} for row in c.fetchall()]
    conn.close()
    return jsonify(books)

# Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO books (title, author, price) VALUES (?, ?, ?)",
              (data['title'], data.get('author', ''), data['price']))
    conn.commit()
    conn.close()
    return jsonify({"success": True, "message": "Book added!"})

# Start the app using Render’s port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use dynamic port for Render
    app.run(host="0.0.0.0", port=port, debug=True)
