class Book:
    def __init__(self, title, year_of_publication, author, publisher, id=None):
        self.title = title
        self.year_of_publication = year_of_publication
        self.author = author
        self.publisher = publisher
        self.id = id