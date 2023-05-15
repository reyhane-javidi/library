import matplotlib.pyplot as plot
import numpy


class Library:
    def __init__(this, resCount, reserved=[], books={}):
        this.resCount = resCount
        this.reserved = reserved
        this.books = books

    def RegBook(this, status, ageGroup, author, name, ISBN):
        title = 'Book ' + str(this.books.__len__() + 1)
        book = {
            title: {
                "status": status,
                "ageGroup": ageGroup,
                "author": author,
                "name": name,
                "ISBN": ISBN
            }}
        registerdBook = this.books.update(book)
        return registerdBook

    def DelBook(this, ISBN):
        for book in this.books.keys():
            if this.books[book]['ISBN'] == ISBN:
                this.books.popitem(book)

    def List(this):
        for book in this.books.keys():
            print('\n')
            print(this.books[book].items())

    def Reserve(this, status, ISBN):
        if status == 1:
            this.reversed.insert(ISBN)
            # increase = lambda num : num + 1
            def increase(num): return num + 1
            this.resCount = increase(this.resCount)
            this.status = 0
        else:
            print('This book is already reserved.')

    def ReturnBook(this, status, ISBN):
        if status == 0:
            this.reserved.remove(ISBN)
            # decrease = lambda num : num - 1
            def decrease(num): return num - 1
            this.resCount = decrease(this.resCount)
            this.status = 1
        else:
            print('You did not reserve this book.')

    def Report(this):
        # points = []
        # lables = []
        # for b in this.books.keys():
        #     (groups, counter) = this.counter(this.books[b]['ageGroup'])
        #     points.insert(counter)
        #     lables.insert(groups)
        pass

    def Search():
        pass
