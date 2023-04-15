### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open()function, 
# to write and read info from a .txt file.
# Follow the instructions to create 
# and call a function to add a book, 
# based off of the previous dictionaries for our 
# library, to the .txt file properly 
# formatted with commas as separators.

# Code here

def create_book_list(library):
    title = input("Add book name here: ")
    author = input("Name of the author: ")
    try:
        year = int(input("Enter year: "))
    except:
        year = int(input("Please enter a number: "))
    try:    
        rating = float(input("Enter rating from 1 - 5: "))
    except:
        rating = float(input("Please enter a number from 1 - 5: "))
    try:    
        pages = int(input("Enter pages count: "))
    except:
        pages = int(input("Please enter a number: "))
    with open(library, "a") as file:
        file.write(f"{title}, {author}, {year}, {rating}, {pages}\n")    


### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all
# the books in your library, but gets the info from a list, and make it work
# by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here

def print_library(library):
    print("\n All books listed\n")
    
    with open(library, "r") as file:
        lines = file.readlines()
        
        books = []
        for line in lines:
            title, author, year, rating, pages = line.strip().split(",")
            book = {
                "Title": title,
                "Author": author,
                "Year": year,
                "Rating": float(rating),
                "Pages": int(pages)
            }
            print(book)
            books.append(book)
            
        return books
                

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an 
# "if __name__ == '__main__':" statement
# to ensure it doesn't accidentally run if 
# this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. 
# Expand your project. 
# Clean up the code. Make your application functional.
# Great job getting your first Python application finished!

def list_library(book):
    print(f"""
          Title: {book["title"]},
          Author: {book["author"]},
          Year: {book["year"]},
          Rating: {book["rating"]},
          Pages: {book["pages"]}
          """)

    
def view_library(library):
    print("\n Here is the library list")
    for book in print_library(library):
        list_library(book)
        
        
def total_books(library):
    print(f"""\n
          You currently have {len(print_library(library))} books
          \n""")        


def main_menu(library):
    
    answer = True
    
    while answer:
        user_choices = input("""
Option 1, Add book: 
Option 2, View book list: 
Option 3: Total books in library: 
Option 4: Total pages: 
Option 5, Leave page:  """)
    
        if user_choices == "1":
            create_book_list(library)
        elif user_choices == "2":
            print_library(library)
        elif user_choices == "3":
             with open(library, "r") as file:
                lines = file.readlines()
                print(f"\n total {len(lines)} books \n")
        elif user_choices == "4":
            with open(library, "r") as file:
                lines = file.readlines()
                total_pages = 0
                for line in lines:
                    title, author, year, rating, pages = line.strip().split(",")
                    total_pages = total_pages + int(pages)
                print(f"\n Page totals {total_pages} pages \n")
        elif user_choices == "5":
            print("\n Leaving page")
            answer = False
        else:
            print("\n Error: Please enter a number")


if __name__ == '__main__':
    main_menu('library.txt')
