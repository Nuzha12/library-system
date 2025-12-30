from dataclasses import dataclass
from datetime import datetime
from typing import List

from day9.library_system.models import Book, Member, Loan
from day9.library_system.repositories import BookRepository, MemberRepository, LoanRepository, InMemoryBookRepository, \
    InMemoryMemberRepository, InMemoryLoanRepository


class LibraryException(Exception):
    pass

@dataclass
class LibraryService:
    books: BookRepository       #has a relationship - composition
    members: MemberRepository    # polymorphism - if we given InMemoryMember repo it could be type error
    loans: LoanRepository

    # def __init__(self, books: BookRepository, members: MemberRepository, loans: LoanRepository ):
    #     self.books = books
    #     self.members = members
    #     self.loans = loans

    def add_book(self, book_id: str, title: str, author: str, year:str ) -> Book:
        if self.books.get_by_id(book_id) is not None:
            raise LibraryException("Book already exists.")

        book = Book(book_id, title, author, year)
        self.books.add_book(book)
        return book

    def add_member(self, member_id: str, member_name: str ) -> Member:
        if self.members.get_member_by_id(member_id) is not None:
            raise LibraryException("Member already exists.")

        member = Member(member_id, member_name)
        self.members.add_members(member)
        return member

    def borrow_book(self, loan_id: str, member_id: str, book_id: str):
        # validate book
        book = self.books.get_by_id(book_id)
        if book is None:
            raise LibraryException("Book doesn't exist.")

        # check availability
        if not book.is_available():
            raise LibraryException("Book is already borrowed.")

        # validate member
        if self.members.get_member_by_id(member_id) is None:
            raise LibraryException("Member doesn't exist.")

        # create loan
        loan = Loan(loan_id, member_id, book_id, datetime.now())
        self.loans.add(loan)

        # mark book borrowed
        book.book_lend_member_id = member_id
        self.books.update(book)

    def return_book(self, loan_id: str):
         loan = self.loans.get_by_id(loan_id)
         if loan is None:
             raise LibraryException(f"Loan with loan id - {loan_id} doesn't exists")

         if not loan.is_active():
             raise LibraryException("Loan is already closed.")

         book = self.books.get_by_id(loan.book_id)
         book.book_lend_member_id = None
         self.books.update(book)

         loan.returned_at = datetime.now()
         self.loans.update(loan)

    def list_all_book(self) -> List[Book]:
        return self.books.list_all_books()

    def list_all_members(self) -> List[Member]:
        return self.members.list_all_members()

    def list_all_loans(self) -> List[Loan]:
        return self.loans.list_all_loans()


# if __name__ == '__main__':
#     library_service = LibraryService(InMemoryBookRepository(), InMemoryMemberRepository(), InMemoryLoanRepository())
#
#     library_service.add_books("001", "Famous Five", "enid blyton", "2000")
#     library_service.add_books("002", "Famous Five2", "enid blyton", "2000")
#
#     print(library_service.list_all_book())
