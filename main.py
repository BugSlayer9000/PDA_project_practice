from book import Book

book_func = Book()

def print_titles():
    books_available = book_func.get_dict_of_books
    
    for number,i in enumerate(books_available,1):
        print(f"{number} - {i["title"]}")


def main():
    
    
    print(f"{"#"*50}")
    print(f"📚 Anniesland Library - Book Management Application")
    print(f"{"#"*50}\n")
    
    genres = ['fiction', 'non-fiction', 'mystery', 'thriller', 'fantasy', 'science fiction', 
                'romance', 'historical fiction', 'biography', 'memoir', 'self-help', 'adventure', 
                'horror', 'crime', 'drama', 'poetry', 'young adult', "children’s", 'graphic novel', 
                'dystopian', 'classical', 'literary fiction', 'philosophical', 'travel', 'cookbooks', 
                'reference', 'guide', 'paranormal', 'supernatural', 'short stories', 'contemporary', 
                'spiritual']
    
    while True:    
        print("Main Menu")
        print("\n1.Add Book")
        print("2.Remove Book")
        print("3.Search books by title")
        print("4.Sort Books by title")
        print("5.Find oldest and newest books")
        print("6.Export Features")
        print("7.Count titles by author")
        print("8.Exit")
        
        try:
            user_input = int(input("\nEnter you choice down below : "))
            
        except ValueError:
            print("Invalid Input ! ")
            continue
            
        if user_input == 1:
            
            print("\nAdd a book")
            
            book_title = input("Enter the title of the book : ").lower().strip()
            if len(book_title) < 2:
                print("Name is too short !")
                continue
            
            book_author = input("Enter the author of the book : ").lower().strip()
            if len(book_author) < 2:
                print("Name is too short ! ")
            
            book_genre = input("Enter the book genre : ").lower().strip()
            if book_genre not in genres:
                print("Warning - not a valid book genre ! ")
                continue
            
            try:
                book_year = int(input("Enter the year of the book : "))
                book_price = float(input("Enter a the price of the book : £"))
            except ValueError:
                print("Invalid input ! must be a number ! ")
                continue
            
            book_func.add_book(book_title,book_author,book_genre,book_year,book_price)
            
        elif user_input == 2:
             
            books_available = book_func.get_dict_of_books
            
            if books_available == 0:
                print("No books available in the system !")
                continue
            
            print_titles()
            
            title_input = input("Enter the title of the book to remove : ").lower().strip()
            
            if title_input in [i["title"] for i in books_available]:
                print("book found ! Removing now ! ")
                book_func.remove_book(title_input)
            else:
                print("Book not found !")
        
        elif user_input == 3:
            
            print_titles()
            
            title_input = input("Enter the name of the title you wanna search : ").lower().strip()
            
            if title_input in [(i["title"]).lower().strip() for i in book_func.get_dict_of_books]:
                book_func.search_book_by_title(title_input)
            else:
                print("\nBook not found ! ")
                continue
        
        
            
        
            
            
            
            
            
        
        

if __name__ == "__main__":
    main()