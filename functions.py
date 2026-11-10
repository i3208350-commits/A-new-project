import Valdations as v
def display_books(books):

    print(f"The list of books is: {books}\n")


def search_book(books, name):
    search_list=[]
    for i in books:
        if name in i["name"]:
            search_list.append(i)
            return(search_list)
        return None


def add_book(books, name, author, year):
    v.number_check(year)
    for i in books:
        if name == i["name"] or author==i["author"]:
           print ("Such a book already exists")
           return


        new_book={"id": len(books)+1,
        "name": name,
        "author":author,
        "year": year,
        "available": True}
        books.append(new_book)
    return books




def borrow_book( books,book_id):

    if not v.number_check(book_id):
       print( "Number does not meet the criteria._2")
       return
    if not v.book_id_n(books,book_id):
        print("Number does not meet the criteria._3")
        return
    for i in books:
        if i["available"]==True:
            print("Okay, take the book.")
            i["available"] == False
        return i["available"]
    return None



def return_book(books, book_id):
    if not v.number_check(book_id):
       print( "Number does not meet the criteria._2")
       return
    if not v.book_id_n(books,book_id):
        print("Number does not meet the criteria._3")
        print("hi")
        return
    for i in books:
        if i["available"]==False:
           i["available"] == True
        return ("Okay, rturen the book.")



def get_available_books(books):
    available_books=[]
    for i in books:
        if i["available"] == True:
            available_books.append(i)
    return available_books
    # return (f"The list of available books {available_books.append}\n")

def get_books_by_author(books, author):
    for i in books:
        if i["author"]==author:
            return (i)

    return "No such book was found"











