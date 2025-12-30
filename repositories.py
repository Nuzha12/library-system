from abc import ABC, abstractmethod
from typing import Dict, List
from day9.library_system.models import Book, Member, Loan


class BookRepository(ABC):

    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def get_by_id(self, book_id: str) -> Book:
        pass

    @abstractmethod
    def update(self, book: Book) -> None:
        pass

    @abstractmethod
    def list_all_books(self) -> List[Book]:
        pass


class MemberRepository(ABC):

    @abstractmethod
    def add_members(self, member: Member) -> None:
        pass

    @abstractmethod
    def get_member_by_id(self, member_id) -> Member:
        pass

    @abstractmethod
    def list_all_members(self) -> list[Member]:
        pass


class LoanRepository(ABC):

    @abstractmethod
    def add(self, loan: Loan) -> None:
        pass

    @abstractmethod
    def get_by_id(self, loan_id) -> Loan:
        pass

    @abstractmethod
    def update(self, loan: Loan) -> None:
        pass

    @abstractmethod
    def list_all_loans(self) -> list[Loan]:
        pass


class InMemoryBookRepository(BookRepository):  #class InMemoryBookRepo is a BookRepo

    def __init__(self):
        self.__books: Dict[str, Book] = {}

    def add_book(self, book: Book) -> None:
        self.__books[book.book_id] = book

    def get_by_id(self, book_id) -> Book:
        return self.__books.get(book_id)

    def update(self, book: Book) -> None:
        self.__books[book.book_id] = book

    def list_all_books(self) -> list[Book]:
         return list(self.__books.values())


class InMemoryMemberRepository(MemberRepository):

    def __init__(self):
        self.__member: Dict[str, Member] = {}

    def add_members(self, member: Member) -> None:
        self.__member[member.member_id] = member

    def get_member_by_id(self, member_id) -> Member:
         return self.__member.get(member_id)

    def list_all_members(self) -> list[Member]:
         return list(self.__member.values())


class InMemoryLoanRepository(LoanRepository):

    def __init__(self):
        self.__loans: Dict[str, Loan] = {}

    def add(self, loan: Loan) -> None:
        self.__loans[loan.loan_id] = loan

    def get_by_id(self, loan_id) -> Loan:
        return self.__loans.get(loan_id)

    def update(self, loan: Loan) -> None:
        self.__loans[loan.loan_id] = loan

    def list_all_loans(self) -> list[Loan]:
        return list(self.__loans.values())
