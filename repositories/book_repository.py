from db.run_sql import run_sql

from models.book import Book
from models.author import Author

import repositories.author_repository as author_repository

def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)

def save(book):
    sql = "INSERT INTO books (title, year_of_publication, author_id, publisher) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [book.title, book.year_of_publication, book.author.id, book.publisher]
    results = run_sql(sql, values)
    id = results[0]["id"]
    book.id = id
    return book