"""

samod subhasha
18/09/25

Psudo code for Library management system

File handling file 

    Csv file handling -> class 

        initialize the file path
        make sure  it exists before proceeding 
        
        def _initialize_file -> initialize the rows of the csv 
            check if the file is empty before adding the rows 
        
        def load_files -> returns a list of lists 
        
        def save_files(data:premade list of lists with modified items)
            rewrites the whole file with new content
        
    
    
book file 

    Book -> class
    
        creates an instance of the csv file 
        
        add book method 
            get the  (Title,Author,Genre,Year,Price) from the user 
        
        remove book method <- title of the book
            fectch the data from the csv as dict (easiar path)
            search for the name 
            
            remove the list from the lsit of lists 
            return it to save file method to save it to the csv
            
            print that the item was removed 
        
        search book by title <- title of the book
            fetch data from the csv file
            see if the title matches in arg
            remove if the title matches 
            rewrite the csv
        
        sort books method 
            get the list of dicts 
            
            make the "title" part lower case so it dosn't count when soritng
            create a new list which includes the sorted items 
        
        list books method (by published year)
            get the list of dicts 

            sort them out 
            "sorted_list_of_dicts = [sorted(list_of_dicts, key=lambda x: x["published_year"])]"
            
            get the last and first items to check the oldest and final items
        
        export featurs <- titles or years 
            get all the data
            if titles
                load titles into a csv
            if year
                load titles and years into another csv
        
        count titles by auther <- get the name of the author
            load the data from the csv as a dict
            check for the author and keep a diffrent list of books with authors 


main file 

    main function
        create an instace of addbook class

        options
            1.add book
            2.remove book <- title
            3.search books by title <- title
            4.sort by books by title
            5.Find oldest and newest books
            6.Export Feature 
                a.book titles
                b.titles and years
            7.count titles by author  <- author
        
        add book
            take the price as a float and year as an int
            get the inputs from user (Title,Author,Genre,Year,Price)
            make all the inputs lowercase 
            use add book method from Addbook class and pass the args
            print added sucessfully
        
        remove book by title
            get the list of books 
            show them to the user
            get the title from the user 
            make it lower case
            
            use the remove book method 
            pass in the title
            print removed sucessfully
        
        search book by title 
            get the list of books 
            show them to the user
            get the title from the user 
            make it lower case
            
            use  search book by title <- title of the book
            print details of the book (Title,Author,Genre,Year,Price)
        
        sort book by the title 
            use sort books method 
            print the sorted list of dicts
        
        find the oldest and the newest book
            use list books method (by published year)
            print data
        
        export feature 
            get the user input
                if title 
                    export featurs <- titles 
                    print sucessfull
                elif years
                    export featurs <- years
                    print sucessfull
        
        count titles by author
            show the list of the books 
            get the user input of the title 
            make it lower case 
            use count titles by auther <- get the name of the author
                    
            
            
        
        
            
            
            
            
         

                

        
        

"""  