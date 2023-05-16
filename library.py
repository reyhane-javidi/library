import matplotlib.pyplot as plot
import numpy


class Library:
    def __init__(this, resCount, reserved, books):
        this.resCount = resCount
        this.reserved = reserved
        this.books = books

    def RegBook(this, status, ageGroup, author, name, ISBN):
        for book in this.books.keys():
            if this.books[book]['ISBN'] == ISBN:
                print('This book is already registerd.')
                return
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
        print(book[title]["name"] + ' ' + 'was registerd.')
        return registerdBook

    def DelBook(this, ISBN):
        for book in this.books.keys():
            if this.books[book]['ISBN'] == ISBN:
                this.books.popitem(book)

    def List(this):
        for book in this.books.keys():
            print(book + ' : ')
            print(this.books[book])

    def Reserve(this, status, ISBN):
        if status == 1:
            this.reversed.append(ISBN)
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
        points = []
        ageGroupList = []
        for book in this.books.keys():
            if this.books[book]['ageGroup'] not in ageGroupList:
                ageGroupList.append(this.books[book]['ageGroup'])
                points.append(this.filter(
                    this.books[book]['ageGroup']).__len__())
        x = numpy.array(ageGroupList, dtype=str)
        y = numpy.array(points)
        plot.xlabel('Age Group')
        plot.ylabel('Number of Books')
        plot.bar(x, y, width=0.5, color='hotpink')
        plot.show()

    def filter(this, val):
        groups = []
        for book in this.books.keys():
            if this.books[book]['ageGroup'] == val:
                groups.append(val)
        return groups

    def Search(this, type, keyword):
        for book in this.books.keys():
            if this.books[book][type] == keyword:
                print(this.books[book]["ISBN"])
                return this.books[book]["ISBN"]


objj = Library(0, [], {
    "book 1": {
        "status": 1,
        "ageGroup": 12,
        "author": "me",
        "name": "kossher",
        "ISBN": 1234
    },
    "book 2": {
        "status": 1,
        "ageGroup": 12,
        "author": "me",
        "name": "kossher",
        "ISBN": 10203
    },
    "book 3": {
        "status": 1,
        "ageGroup": 20,
        "author": "me",
        "name": "kossher",
        "ISBN": 5478
    }
})

objj.RegBook(1, 20, 'asdf', "asdf", 15462)
objj.RegBook(1, 20, 'asdf', "asdf", 151462)
objj.RegBook(1, 22, 'asdfsaf', "nameofthebook", 1512462)

objj.Search('name', 'nameofthebook')
objj.List()
