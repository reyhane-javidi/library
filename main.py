import matplotlib.pyplot as plot
import numpy
import re


class Library:
    def __init__(this, resCount, reserved, books):
        this.resCount = resCount
        this.reserved = reserved
        this.books = books
        this.bookHolders = []

    def findBookByISBN(this, ISBN):
        for book in this.books.keys():
            if this.books[book]['ISBN'] == ISBN:
                return book

    def RegBook(this, status, ageGroup, author, name, ISBN):
        foundBook = this.findBookByISBN(ISBN)
        if foundBook != None:
            print('This book is already registerd.')
            return

        title = 'Book ' + str(this.books.__len__() + 1)
        book = {
            title: {
                "status": bool(status),
                "ageGroup": ageGroup,
                "author": author,
                "name": name,
                "ISBN": ISBN
            }}
        registerdBook = this.books.update(book)
        print(book[title]["name"] + ' was registerd.')
        return registerdBook

    def DelBook(this, ISBN):
        foundBook = this.findBookByISBN(ISBN)
        if foundBook == None:
            print('This book is not registerd.')
        else:
            this.books.pop(foundBook)
            print(foundBook + ' was deleted.')

    def List(this):
        for book in this.books.keys():
            print(book + ' : ')
            print(this.books[book])

    def Reserve(this, name, ISBN):
        for book in this.books:
            if this.books[book]['ISBN'] == ISBN:
                if this.books[book]['status'] == bool(1):
                    this.reserved.append(ISBN)
                    # increase = lambda num : num + 1
                    def increase(num): return num + 1
                    this.resCount = increase(this.resCount)
                    this.bookHolders.append(name)
                    this.books[book]["status"] = bool(0)
                else:
                    print('This book is already reserved.')

    def ReturnBook(this, name, ISBN):
        for book in this.books:
            if this.books[book]["ISBN"] == ISBN:
                if this.books[book]["status"] == bool(0):
                    if name in this.bookHolders:
                        this.bookHolders.remove(name)
                    else:
                        print('You did not reserve this book.')
                    this.reserved.remove(ISBN)
                    # decrease = lambda num : num - 1
                    def decrease(num): return num - 1
                    this.resCount = decrease(this.resCount)
                    this.books[book]["status"] = bool(1)
                    print('You returned this book')
                else:
                    print('This book is not reserved.')

    def Report(this):
        points = []
        ageGroupList = []
        for book in this.books.keys():
            if this.books[book]['ageGroup'] not in ageGroupList:
                ageGroupList.append(this.books[book]['ageGroup'])
                print(this.books[book]['ageGroup'])

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

    def Search(this, typeOfValue, keyword):
        for book in this.books.keys():
            if this.books[book][typeOfValue].lower() == keyword.lower():
                print('Found the book you wanted: ')
                print(this.books[book]["ISBN"])
                return

        print("Couldn't find the book you were looking for.")


class MyLib(Library):
    def __init__(this, resCount, reserved, books, userAge):
        super().__init__(resCount, reserved, books)
        this.userAge = userAge

    def AgeOk(this, userAge):
        for book in this.books.keys():
            if this.books[book]['ageGroup'] <= userAge:
                return this.books[book]['ISBN']
            else:
                return False

    def Reserve(this, name, ISBN, userAge):
        for book in this.books:
            if this.books[book]['ISBN'] == ISBN:
                if this.books[book]['status'] == bool(1):
                    if this.AgeOk(userAge) != False:
                        this.reserved.append(ISBN)
                        # increase = lambda num : num + 1
                        def increase(num): return num + 1
                        this.resCount = increase(this.resCount)
                        this.bookHolders.append(name)
                        this.books[book]["status"] = bool(0)
                    else:
                        print("You can't reserve this book.")
                else:
                    print('This book is already reserved.')

    def setInput(this, inputText, inputType):
        value = ''
        if inputType == 'int':
            try:
                value = int(input(inputText))
            except:
                return this.setInput(inputText, inputType)
        elif inputType == 'str':
            try:
                value = input(inputText)
            except:
                return this.setInput(inputText, inputType)
        elif inputType == 'bool':
            try:
                value = int(input(inputText))
                if value == 0 or value == 1:
                    return value
                else:
                    return this.setInput(inputText, inputType)
            except:
                return this.setInput(inputText, inputType)
        return value

    def displayRegBook(this):
        status = this.setInput(
            'Enter the status of the book. (0/1) : ', 'bool')

        ageGroup = this.setInput(
            'Enter the age group of the book (number) : ', 'int')

        author = this.setInput('Enter the author of the book : ', 'str')

        name = this.setInput('Enter the name of the book : ', 'str')

        ISBN = this.setInput('Enter the ISBN of the book : ', 'int')
        # (status, ageGroup, author, name, ISBN) = this.displayOpration(
        # [status, ageGroup, author, name, ISBN])
        this.RegBook(status, ageGroup, author, name, ISBN)
        this.Menu()

    def displayDelBook(this):
        ISBN = this.setInput('Enter the ISBN of the book : ', 'int')
        this.DelBook(ISBN)
        print('\n')
        this.Menu()

    def displayList(this):
        this.List()
        print('\n')
        this.Menu()

    def displaySearch(this):
        typeOfValue = this.setInput(
            'Enter the type of value your looking for (name / author) : ', 'str')

        keyword = this.setInput('Enter the value : ', 'str')

        this.Search(typeOfValue, keyword)
        print('\n')
        this.Menu()

    def displayReserve(this):
        userAge = this.setInput('Enter your age : ', 'int')
        name = this.setInput('Enter your name : ', 'str')
        ISBN = this.setInput('Enter the ISBN of the book : ', 'int')
        this.Reserve(name, ISBN, userAge)
        print('\n')
        this.Menu()

    def displayReturnBook(this):
        name = this.setInput('Enter your name : ', 'str')
        ISBN = this.setInput('Enter the ISBN of the book : ', 'int')
        this.ReturnBook(name, ISBN)
        print('\n')
        this.Menu()

    def displayReport(this):
        this.Report()
        print('\n')
        this.Menu()

    def displayOpration(this, **inputs):
        listOfInputs = []
        if inputs['status']:
            status = this.setInput(
                'Enter the status of the book. (0/1) : ', 'bool')
            listOfInputs.append(status)
        if ageGroup in inputs:
            ageGroup = this.setInput(
                'Enter the age group of the book (number) : ', 'int')
            listOfInputs.append(ageGroup)
        if author in inputs:
            author = this.setInput('Enter the author of the book : ', 'str')
            listOfInputs.append(author)
        if name in inputs:
            name = this.setInput('Enter the name of the book : ', 'str')
            listOfInputs.append(name)

        if ISBN in inputs:
            ISBN = this.setInput('Enter the ISBN of the book : ', 'int')
            listOfInputs.append(ISBN)

        if userAge in inputs:
            userAge = this.setInput('Enter your age : ', 'int')
            listOfInputs.append(userAge)
        return listOfInputs

    def Menu(this):
        print('''
        List of oprations :
        1. Register a new book
        2. Delete an existing book
        3. List all of the books
        4. Search and find a book
        5. Reserve a book
        6. Return a reserved book
        7. Report
        8. Exit the application
        ''')
        opration = ''
        try:
            opration = int(input('Choose what to happen : '))
        except:
            this.Menu()
        if opration == 1:
            this.displayRegBook()
        elif opration == 2:
            this.displayDelBook()
        elif opration == 3:
            this.displayList()
        elif opration == 4:
            this.displaySearch()
        elif opration == 5:
            this.displayReserve()
        elif opration == 6:
            this.displayReturnBook()
        elif opration == 7:
            this.displayReport()
        elif opration == 8:
            return
        else:
            print('Please choose one of the options above.')
            this.Menu()


books = {
    "Book 1": {
        "status": True,
        "ageGroup": 10,
        "author": "RJ Palacio",
        "name": "Wonder",
        "ISBN": 12345
    },
    "Book 2": {
        "status": True,
        "ageGroup": 21,
        "author": "Stephen R. Covey",
        "name": "The 7 habbits of highly effective people",
        "ISBN": 56789
    },
    "Book 3": {
        "status": True,
        "ageGroup": 25,
        "author": "Paulo Coelho",
        "name": "The Alchemist",
        "ISBN": 54789
    },
    "Book 4": {
        "status": True,
        "ageGroup": 31,
        "author": "John Steinbeck",
        "name": "The grapes of wrath",
        "ISBN": 14523
    },
    "Book 5": {
        "status": True,
        "ageGroup": 20,
        "author": "Cheryl Strayed",
        "name": "Wild",
        "ISBN": 78523
    },
    "Book 6": {
        "status": True,
        "ageGroup": 20,
        "author": "Imposter syndrome",
        "name": "Kathy Wang",
        "ISBN": 69587
    }
}

obj = MyLib(0, [], books,  0)

obj.Menu()
