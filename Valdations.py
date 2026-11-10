def number_check(x):
    if isinstance(x,int) and x>0:
        return True
    return False

def book_review(x,books):
     for i in books:
            if x == i["name"]:
                return True
            return False


def book_id_n(books,x):
    for i in books:
        if x == i["id"]:
            return True
        return False
