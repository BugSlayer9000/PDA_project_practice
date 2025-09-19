from csv_file_handling import CSVFileHandling



class Book:
    
    csv = CSVFileHandling()
    
    def add_book(self, title, author, genre, year:int, price:float):
        
        new_book = [title, author, genre, year, price]
        
        existing_list = self.csv.load_file()
        
        existing_list.append(new_book)
        
        self.csv.save_file(existing_list)
        
        print(f"new book - {title} added ! ")
    
    def remove_book(self, title:str):
        
        is_removed = False 
        
        data = self.csv.load_file()

        for book in data:
            if book[0].lower().strip() == title.lower().strip() :
                data.remove(book)
                
                self.csv.save_file(data)
                
                print(f"{book[0]} Removed ! ")
                is_removed = True
            else:
                pass
        
        if not is_removed:
            print("Book not found !")
        
        
                
        
        
    
    


b = Book()


b.remove_book("pakaya")