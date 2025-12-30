from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Book:
    book_id: str
    title: str
    author: str
    year: str
    book_lend_member_id: Optional[str] = None
    # lend_member_id: str

    def is_available(self):
        return self.book_lend_member_id is None

@dataclass
class Member:
    member_id: str
    member_name: str

@dataclass
class Loan:
    loan_id: str
    member_id: str
    book_id: str
    borrowed_at: datetime
    returned_at: Optional[datetime] = None

    def is_active(self) -> bool:
        return self.returned_at is None


book = Book("589", "Home Alone", "John", "1999")
print(book.book_lend_member_id)
