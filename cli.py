from typing import List
from day9.library_system.library_service import LibraryService, LibraryException
from day9.library_system.models import Book, Member, Loan
from day9.library_system.repositories import InMemoryBookRepository, InMemoryLoanRepository, InMemoryMemberRepository

library_service = LibraryService(books=InMemoryBookRepository(),
                                 members=InMemoryMemberRepository(),
                                 loans=InMemoryLoanRepository()
                                 )

library_service.add_book("001", "Famous Five", "enid blyton", "2000")
library_service.add_book("002", "Famous Five2", "enid blyton", "2000")

# print(library_service.list_all_book())


def list_all_books():
    books: List[Book] = library_service.list_all_book()

    for book in books:
        print(f"Book Id: {book.book_id} Book Name: {book.title} "
              f"Book Author: {book.author} "
              f"Book Published Date: {book.year}")


def add_book():
    book_id = input("Enter book id: ")
    title = input("Enter title: ")
    author = input("Enter author: ")
    year = input("Enter year: ")

    try:
        library_service.add_book(book_id, title, author, year)

    except LibraryException as e:
        print(e)


def list_all_members():
    members: List[Member] = library_service.list_all_members()

    for member in members:
        print(f"Member id: {member.member_id} Member name: {member.member_name}")


def add_members():
    member_id = input("Enter member id: ")
    member_name = input("Enter member name: ")

    try:
        library_service.add_member(member_id, member_name)

    except LibraryException as e:
        print(e)


def borrow_book():
    loan_id = input("Enter loan id: ")
    member_id = input("Enter member id: ")
    book_id = input("Enter book id: ")

    try:
        library_service.borrow_book(loan_id, member_id, book_id)

    except LibraryException as e:
        print(e)


def return_book():
     loan_id = input("Enter loan id: ")

     try:
         library_service.return_book(loan_id)

     except LibraryException as e:
         print(e)


def list_all_loans():
    loans: List[Loan] = library_service.list_all_loans()


    for loan in loans:
        print(f" Loan id is : {loan.loan_id}  Member: {loan.member_id}, Book: {loan.book_id}, Returned: {loan.returned_at}")

while True:
    print()
    print("=================Library Management System====================")
    print("press 1 to list all books")
    print("press 2 to add a book")
    print("press 3 to add member")
    print("press 4 to list all members")
    print("press 5 to borrow book")
    print("press 6 to return book")
    print("press 7 to list all loans")
    print("press 0 to exit")

    print("=============================================================")
    print()


    try:
        choice = int(input("Enter choice:"))

    except ValueError:
        print("Invalid Input! please enter valid number")
        continue

    if choice == 1:
         list_all_books()

    elif choice == 2:
        add_book()

    elif choice == 3:
        add_members()

    elif choice == 4:
        list_all_members()

    elif choice == 5:
        borrow_book()

    elif choice == 6:
        return_book()

    elif choice == 7:
        list_all_loans()

    elif choice == 0:
        exit()
