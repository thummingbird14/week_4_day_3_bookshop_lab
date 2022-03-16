from db.run_sql import run_sql

from models.author import Author
from models.book import Book

def save(author):
    sql = "INSERT INTO authors (name) VALUES (%s) RETURNING *"
    values = [author.name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    author.id =id
    return author

def delete_all():
    sql = "DELETE FROM authors"
    run_sql(sql)