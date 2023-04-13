### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, 
# to write and read info from a .txt file. Follow the instructions to create 
# and call a function to add a book, based off of the previous dictionaries for our 
# library, to the .txt file properly formatted with commas as separators.

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
    with open(library, "i") as file:
        file.write(f"{title}, {author}, {year}, {rating}, {pages}\n")    


### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all
# the books in your library, but gets the info from a list, and make it work
# by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here

def print_library(book):
    print("\n All books listed\n")
    
    with open(book, "r") as file:
        lines = file.readlines()
        
        for line in lines:
            title, author, year, rating, pages = line.strip().split(",")
            print(f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")

### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement
# to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. 
# Clean up the code. Make your application functional. Great job getting your first Python application finished!

def main_menu(book_source):

    active = True

    while active:
        choice = input("""
Choose 1 to add a book...
Choose 2 to see all your books...
Choose 3 to see a count of your books...
Choose 4 to see a count of the pages of your books...
Choose 5 to see the your highest rated book...
Choose 6 to see your lowest rated book...
Choose 7 to see your books ranked by order of rating...
Choose 0 to exit.
Type here: """)

        if choice == "1":
            create_new_book(book_source)
        elif choice == "2":
            view_books(book_source)
        elif choice == "3":
            print(f"\nYou have a total of {len(get_books_as_list_of_dictionaries(book_source))} books.\n")
        elif choice == "4":
            print(f"\nYou books page count totals {sum([x['pages'] for x in get_books_as_list_of_dictionaries(book_source)])} pages!\n")
        elif choice == "5":
            print("\nHere is your highest rated book...\n")
            get_book_printed(get_highest_rated_book(book_source))
        elif choice == "6":
            print("\nHere is your lowest rated book...\n")
            get_book_printed(get_lowest_rated_book(book_source))
        elif choice == "7":
            get_sorted_list_by_rating(book_source)
        elif choice == "0":
            print("\nGoodbye")
            active = False
        else:
            print("\nSorry please type a number for one of the options.\n")

if __name__ == "__main__":
    main_menu("library.txt")