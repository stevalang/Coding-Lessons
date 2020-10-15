from dataclasses import dataclass


class Book:
    def __init__(self, name, author, pages):
        self.pages = pages
        self.author = author
        self.name = name


@dataclass
class Book2:
    name: str
    author: str
    pages: int
