import matplotlib.pyplot as plot
import numpy
import re


class Library:
    def __init__(this, resCount, reserved, books):
        this.resCount = resCount
        this.reserved = reserved
        this.books = books
        this.bookHolders = []

    def findBook(this, key, value):
        for book in this.books.keys():
            if this.books[book][key] == value:
                return book

        return None

    def RegBook(this, ageGroup, author, name, ISBN):
        foundBook = this.findBook('ISBN', ISBN)
        if foundBook == None:
            title = 'Book ' + str(this.books.__len__() + 1)
            book = {
                title: {
                    "ISBN": ISBN,
                    "name": name,
                    "author": author,
                    "ageGroup": ageGroup,
                    "status": True,
                }}
            registerdBook = this.books.update(book)
            print(book[title]["name"] + ' was registerd.')
            return registerdBook
        print('This book is already registerd.')

    def DelBook(this, ISBN):
        foundBook = this.findBook('ISBN', ISBN)
        if foundBook == None:
            print('This book is not registerd.')
        else:
            this.books.pop(foundBook)
            print(foundBook + ' was deleted.')

    def List(this):
        for book in this.books.keys():
            print(book + ' : ')
            print(this.books[book])

    def Reserve(this, username, ISBN):
        foundBook = this.findBook('ISBN', ISBN)
        if foundBook == None:
            print('Could not find the book.')
            return
        else:
            if this.books[foundBook]['ISBN'] == ISBN:
                if this.books[foundBook]['status'] == bool(1):
                    this.reserved.append(ISBN)
                    # increase = lambda num : num + 1
                    # this.resCount = increase(this.resCount)
                    def increase(num): return num + 1
                    this.resCount = increase(this.resCount)
                    this.bookHolders.append(username)
                    this.books[book]["status"] = bool(0)
                else:
                    print('This book is already reserved.')

    def ReturnBook(this, username, ISBN):
        foundBook = this.findBook('ISBN', ISBN)
        if foundBook == None:
            print('Could not find this book')
            return
        else:
            if this.books[foundBook]["ISBN"] == ISBN:
                if this.books[foundBook]["status"] == bool(0):
                    if username in this.bookHolders:
                        this.bookHolders.remove(username)
                    else:
                        print('You did not reserve this book.')
                    this.reserved.remove(ISBN)
                    # decrease = lambda num : num - 1
                    # this.resCount = decrease(this.resCount)

                    def decrease(num): return num - 1
                    this.resCount = decrease(this.resCount)
                    this.books[foundBook]["status"] = bool(1)
                    print('You returned this book')
                else:
                    print('This book is not reserved.')

    def filterAgeGroup(this, val):
        group = []
        for book in this.books.keys():
            if this.books[book]['ageGroup'] == val:
                group.append(val)
        return group

    def Report(this):
        points = []
        ageGroupList = []
        for book in this.books.keys():
            if this.books[book]['ageGroup'] not in ageGroupList:
                ageGroupList.append(this.books[book]['ageGroup'])
                points.append(this.filterAgeGroup(
                    this.books[book]['ageGroup']).__len__())
        x = numpy.array(ageGroupList, dtype=str)
        y = numpy.array(points)
        colors = numpy.array([
            'lime', 'skyblue', 'hotpink', 'teal', 'coral'])
        plot.xlabel('Age Group')
        plot.ylabel('Number of Books')
        plot.bar(x, y, width=0.5, color=colors)
        plot.show()

    def Search(this, typeOfValue, keyword):
        for book in this.books:
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
        foundBook = this.findBook('ageGroup', userAge)
        if foundBook == None:
            return False
        else:
            return this.books[foundBook]['ISBN']

    def Reserve(this, username, ISBN, userAge):
        foundBook = this.findBook('ISBN', ISBN)
        if foundBook == None:
            print('Could not find the book.')
            return
        else:
            if this.books[foundBook]['status'] == bool(1):
                if this.AgeOk(userAge) == False:
                    print("You can't reserve this book.")
                    return
                this.reserved.append(ISBN)

                # increase = lambda num : num + 1
                # this.resCount = increase(this.resCount)

                def increase(num): return num + 1
                this.resCount = increase(this.resCount)
                this.bookHolders.append(username)
                this.books[foundBook]["status"] = bool(0)
                print('You reserved this book.')
            else:
                print('This book is already reserved.')
                return

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

    def displayOpration(this, inputs):
        listOfInputs = []
        if "ISBN" in inputs:
            ISBN = this.setInput('Enter the ISBN of the book : ', 'int')
            listOfInputs.append(ISBN)

        if "name" in inputs:
            name = this.setInput('Enter the name of the book : ', 'str')
            listOfInputs.append(name)

        if "author" in inputs:
            author = this.setInput('Enter the author of the book : ', 'str')
            listOfInputs.append(author)

        if "ageGroup" in inputs:
            ageGroup = this.setInput(
                'Enter the age group of the book (number) : ', 'int')
            listOfInputs.append(ageGroup)
        if "status" in inputs:
            status = this.setInput(
                'Enter the status of the book. (0/1) : ', 'bool')
            listOfInputs.append(status)

        if 'username' in inputs:
            username = this.setInput('Enter your name : ', 'str')
            listOfInputs.append(username)

        if "userAge" in inputs:
            userAge = this.setInput('Enter your age : ', 'int')
            listOfInputs.append(userAge)

        if "typeOfValue" in inputs:
            typeOfValue = this.setInput(
                'Enter the type of value your looking for (name / author) : ', 'str')
            listOfInputs.append(typeOfValue)

        if "keyword" in inputs:
            keyword = this.setInput('Enter the value : ', 'str')
            listOfInputs.append(keyword)

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
            return this.Menu()
        if opration == 1:
            ISBN, name, author, ageGroup = this.displayOpration(
                ["ISBN", "name", "author", "ageGroup"])
            this.RegBook(ageGroup, author, name, ISBN)
            print('\n')
            return this.Menu()
        elif opration == 2:
            ISBN = this.displayOpration(['ISBN'])
            this.DelBook(ISBN[0])
            print('\n')
            return this.Menu()
        elif opration == 3:
            this.List()
            print('\n')
            return this.Menu()
        elif opration == 4:
            typeOfValue, keyword = this.displayOpration(
                ['typeOfValue', 'keyword'])
            this.Search(typeOfValue, keyword)
            print('\n')
            return this.Menu()
        elif opration == 5:
            ISBN, username, userAge = this.displayOpration(
                ['ISBN', 'username', 'userAge'])
            this.Reserve(username, ISBN, userAge)
            print('\n')
            return this.Menu()
        elif opration == 6:
            ISBN, username = this.displayOpration(['ISBN', 'username'])
            this.ReturnBook(username, ISBN)
            print('\n')
            return this.Menu()
        elif opration == 7:
            this.Report()
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
        "ISBN": 56789,
        "name": "The 7 habbits of highly effective people",
        "author": "Stephen R. Covey",
        "ageGroup": 21,
        "status": True
    },
    "Book 3": {
        "ISBN": 54789,
        "name": "The Alchemist",
        "author": "Paulo Coelho",
        "ageGroup": 25,
        "status": True
    },
    "Book 4": {
        "ISBN": 14523,
        "name": "The grapes of wrath",
        "author": "John Steinbeck",
        "ageGroup": 31,
        "status": True
    },
    "Book 5": {
        "ISBN": 78523,
        "name": "Wild",
        "author": "Cheryl Strayed",
        "ageGroup": 20,
        "status": True
    },
    "Book 6": {
        "ISBN": 69587,
        "name": "Kathy Wang",
        "author": "Imposter syndrome",
        "ageGroup": 20,
        "status": True
    }
}

obj = MyLib(0, [], books,  0)

obj.Menu()
