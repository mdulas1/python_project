class Library:
 def __init__(self, id, name):
  self.bookId = id
  self.bookName = name
 def setBookName(self, newBookName): #setters method to set the book name
  self.bookName = newBookName
 def getBookName(self): #getters method to get the book name
  print(f"The name of book is {self.bookName}")
 def getBookName(self):
   print(f"The name of book is {self.bookName}")
 def getBookName(self):
   print(f"The name of book is {self.bookName}")

book1 = Library(101,"SKILLS IS RATHER THAN JUST DEGREE")
book2 = Library(102,"A SCHOOLER JOURNEEY IN ACADIMIA")
book3 = Library(103,"STUDY FROM BIRTH TO DEATH")
book1.getBookName()
book2.getBookName()
book3.getBookName()
book1.setBookName("SKILLS IS RATHER THAN JUST DEGREE Returns")
book2.setBookName("A SCHOOLER JOURNEEY IN ACADIMIA RETURN")
book3.setBookName("STUDY FROM BIRTH TO DEATH RETURN")
book1.getBookName()
book2.getBookName()
book3.getBookName()