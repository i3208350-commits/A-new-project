
import functions as f
books = [    {        "id": 1,        "name": "Harry Potter",        "author": "J.K. Rowling",        "year": 1997,        "available": False    },    {        "id": 2,        "name": "The Hobbit",        "author": "J.R.R. Tolkien",        "year": 1937,        "available": True    },    {        "id": 3,        "name": "Clean Code",        "author": "Robert Martin",        "year": 2008,        "available": False    },    {        "id": 4,        "name": "Atomic Habits",        "author": "James Clear",        "year": 2018,        "available": True    },    {        "id": 5,        "name": "The Pragmatic Programmer",        "author": "David Thomas",        "year": 1999,        "available": False    }]

def menu():
   while True:
       print("1. Display all books  ")
       print("2. Search book by name ")
       print("3. Add new book ")
       print("4. Borrow a book ")
       print("5. Return a book ")
       print("6. Display available books ")
       print("7. Display books by author ")
       print("8. Exit ")
       choose=input("Choose an option: ")
       if choose=="1":
           f.display_books(books)
       if choose=="2":
           name = input("Insert a book name").lower()
           examination=f.search_book(books,name)
           print(examination)
       if choose == "3":
          name = input("Insert a book name")
          author = input("Insert a book author")
          try:
              year = int(input("Insert a book year"))
          except:
              raise "Error, entered an incorrect number."

          f.add_book(books, name, author, year)

       if choose == "4":
           try:
              book_id=int(input("Enter an id number"))
              anser = f.borrow_book(books, book_id)
              print(anser)
           except:
              print( "Error, entered an incorrect number_111.")
       if choose == "5":
           try:
              book_id=int(input("Enter an id number"))
              anser=f.return_book(books, book_id)
              print(anser)
           except:
               print("Error, entered an incorrect number")
       if choose == "6":
           print(f.get_available_books(books))
       if choose == "7":
           choose_author=input("Insert super name")
           print(f.get_books_by_author(books, choose_author))
       if choose == "8":
           break
       else:
           print("Enter number again")




if __name__ == '__main__':
    menu()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
