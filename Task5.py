class library :

    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)



class book :
    def __init__(self, title, author, isbn, is_available):
        self.title =title
        self.author =author
        self.__isbn =isbn
        self.is_avaliable =is_available

    def desplay_info(self) :
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"ISBN : {self.__isbn}")
        print(f"Availbilty : {self.is_avaliable}")
    
    def get_isbn(self):
        return self.__isbn
    def set_isbn(self, new_isbn):
        self.__isbn = new_isbn




class member :
    def __init__(self, name, membership_id):
        self.name =name
        self.__membership_id =membership_id

    def borrow_book(self, book):
        if book.is_avaliable == True :
           return(f"{self.name}  can borrow it , it's avaliabe")
        else :
            return(f"{self.name} can't borrow it , it isn't avaliabe")
        
    def return_book(self, book):
        if book.is_avaliable == True :
            return(f"{self.name} has return the{self.title}")
        else:
            return(f"{self.name} hasn't return the{self.title} ")
    
    def get_membership_id(self):
        return self.__membership_id
    
    def set_membership_id(self, new_membership_id):
        self.__membership_id = new_membership_id
        
    
class staffmember(member):
    def __init__(self, name, membership_id, staff_id):
        self.name =name
        self.__membership_id =membership_id
        self.staff_id = staff_id

    def add_book(self, book, library):
        library.add_book(book)
        print(f"staff {self.name} has added {book.title}")


    
    

        


        

    
        