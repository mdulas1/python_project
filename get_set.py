class Library:
    def __init__(self,id,name):
        self.bookid = id
        self.bookName = name

    def setBookName(self,NewBookName): # setter
        self.bookName = NewBookName


    def getBookName(self): # getter
        print(f"The name of the author is {self.bookName}")


book = Library("second flour", "fundamental of data structure using C ")
book.getBookName()

book.setBookName("ranjang gabar khan")
book.getBookName()
