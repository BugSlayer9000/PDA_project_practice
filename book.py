from csv_file_handling import CSVFileHandling
from pathlib import Path
import csv

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
    
    def search_book_by_title(self, title:str):
        
        is_found = False
        
        data = self.csv.load_file()
        
        for book in data:
            if book[0].lower().strip() == title.lower().strip() :
                print("Book found ! ")
                print(f"\nTitle - {book[0]}\nAuthor - {book[1]}\nGenre - {book[2]}\nYear - {book[3]}\nPrice - £ {book[4]}")
                is_found = True
        
        
        if not is_found:
            print("Book not found ! ")
    
    def sort_books(self):
        
        data = self.csv.load_file()
        
        sorted_list_of_lists = [sorted(data, key=lambda book: book[0].lower())]
        
        for i in sorted_list_of_lists:
            self.csv.save_file(i)
        
        print("Sorted all the items")
    
    def oldest_and_newsest_book(self):
        
        data = [i for i in self.csv.get_list_of_dicts()]
        
        sorted_list_of_books = [i for i in (sorted(data, key=lambda x: x["year"]))]
        
        
        first_book = sorted_list_of_books[0]
        
        last_book = sorted_list_of_books[len(sorted_list_of_books)-1]
        
        print(f"\nOldest Book\nTitle = {first_book["title"]}\nYear = {first_book["year"]}")
        print(f"\nNewest Book\nTitle = {last_book["title"]}\nYear = {last_book["year"]}")
    
    
    # this privet method will be used to use for title finding by author method.
    # after finding the author exists the method asks for the list of books under that author from using this privet method.
    def _get_books_for_author(self, author):
        
        list_of_books = []
        
        for i in self.csv.get_list_of_dicts():
            if i["author"].lower().strip() == author:
                list_of_books.append(i["title"])
        
        return list_of_books
    
    def count_titles_by_author(self, author_name):
        
        """
        Plan - go through the saved SVG and collect the authors names 
        then show them
        """
        self.list_of_authors = []
        
        for i in self.csv.get_list_of_dicts():
            if i["author"].lower().strip() not in self.list_of_authors:
                self.list_of_authors.append(i["author"].lower().strip())
        
        
        if  author_name.lower().strip() in self.list_of_authors:
            print("\nAuthor found ! ")
            
            data = self._get_books_for_author(author_name.lower().strip())
            
            print("\nName of the books. \n")
            for number,i in enumerate(data, 1):
                print(f"{number}.{i}")
            
        else:
            print("\nAuthor not found !")
    
    # this method is is meant for main file to get the authors to show th user 
    
    @property
    def get_list_of_authors(self):
        return self.list_of_authors
    
    def get_separate_titles_file(self):
        # get a list of titles then write it into a new cv
        
        title_list = []
        
        data = self.csv.get_list_of_dicts()
        
        if len(data) == 0:
            print("No data in the system")
            return
        
        for i in data:
            title_list.append(i["title"])
        
        
        
        file_path = Path("files/titles.csv")
        file_path.touch(exist_ok=True)
        
        # initialize file
        with open(file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["titles"])
            writer.writerows([[title] for title in title_list])
    
    def get_separate_titles_and_year_file(self):
        # get a list of titles then write it into a new cv
        
        title_list = []
        
        data = self.csv.get_list_of_dicts()
        
        if len(data) == 0:
            print("No data in the system")
            return
        
        for i in data:
            title_list.append([i["title"],i["year"]])
        
        
        
        file_path = Path("files/titles_year.csv")
        file_path.touch(exist_ok=True)
        
        # initialize file
        with open(file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["titles","year"])
            writer.writerows([title for title in title_list])
    
    
    
       
        
        
    
    
    
    

        
        
        
                
        
        
    
    


