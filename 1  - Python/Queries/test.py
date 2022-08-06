


class library:
    def __init__(self ,book_detail):
        
        with open(book_detail , "r") as file:
            self.book = file.readlines()
        
    def book_names(self):
        for i in self.book:
            print(i)



if __name__=="__main__":
    book_detail = "book_detail.txt"

    obj = library(book_detail)

    obj.book_names()










# with open("book_detail.txt","r") as file:
#     book = file.readlines()

# for i in book:
#     print(i)



