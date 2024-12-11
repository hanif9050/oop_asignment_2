class Library:
    book_list=[]
    @classmethod
    def entry_book(self,book):
        self.book_list.append(book)
    def __repr__(self):
        for bk in self.book_list:
            # print(bk.title)
            return f"{bk.__title} {bk.__author} {bk.__availability} "
class Book:
    def __init__(self,book_id,title,author,availability):
        self.__book_id=book_id
        self.__title=title
        self.__author=author
        self.__availability=availability
        Library.entry_book(self)
    @classmethod
    def borrow_book(self,bkId):
        found =False
        validID=False
        for bk in Library.book_list:
           
            if bk.__book_id == bkId:
                validID = True
                if bk.__availability == True:
                    bk.__availability = False
                    found = True
                    print(f"Book '{bk.__title}' borrowed successfully.")


        if found == False and validID == True:
            print("Trying to borrow a book that is already borrowed.")
        elif validID == False: 
            print("Invalid Book ID.")
            

       
    @classmethod
    def return_book(self,bookId):
        isBorrow =False
        validID=False
        for bk in Library.book_list:
            if bk.__book_id == bookId:
                validID=True
                if bk.__availability == False:
                    bk.__availability = True
                    isBorrow = True

        if validID == False:
            print("Invalid Book ID.")
        elif isBorrow == False:
            print("Trying to return a book that is not borrowed.")
        else:
            print("Book returned successfully.")
        
    @classmethod
    def view_book_info(self):
         print("----All Books------")
         for bk in Library.book_list:
            print(f"ID: {bk.__book_id}, Title: {bk.__title}, Author: {bk.__author}, Availability: {"Available" if bk.__availability == True else "Not Available"}")
        
# lib=Library()
book_1=Book(101,"Advanced Python Programming","Jane Smith",True)
book_2=Book(102,"Mastering JavaScript","John Doe",True)
book_3=Book(103,"Data Structures and Algorithms in C++","Mark Johnson",True)
book_4=Book(104,"Java for Beginners","Sarah Williams",True)
book_5=Book(105,"Web Development with React","Michael Brown",True)

# print(book_1.__author)
# print(lib)
# print(Library.book_list[0].title)
# book1.return_book("han")

while True:
    print("---Welcome to the Library---")
    print("1. View All Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")


    print("Enter Your Choice: ",end="")
    userInput=int(input())
    if userInput==4:
        break
    elif userInput == 1:
      
        Book.view_book_info()
    elif userInput == 2:
        print("Enter Book Id: ",end="")
        userInput=int(input())
        Book.borrow_book(userInput)
    elif userInput == 3:
        print("Enter Return Book ID: ",end="")
        userInput=int(input())
        Book.return_book(userInput)