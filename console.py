import pdb
from models.book import Book
from models.author import Author

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Jasper Fforde")
author_repository.save(author1)

author2 = Author("George Orwell")
author_repository.save(author2)

book1 = Book("The Eyre Affair", 2001, author1, "Hodder & Stoughton")
book_repository.save(book1)

book2 = Book("1984", 1948, author2, "Viking")
book_repository.save(book2)

for book in book_repository.select_all():
    print(book.__dict__)

# for author in author_repository.select_all():
    # print(author.__dict__)



