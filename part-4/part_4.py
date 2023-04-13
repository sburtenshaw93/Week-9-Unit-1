### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. 
# After that be sure to turn it into a function.
print("----------------Step 1--------------------")
# Code here
# title = input("What book are you looking for?")
# author = input("What Author are you looking for ")
# year = input("What is the year of the book was made?")
# rating = input("Enter rating from 1 - 5")
# pages = input("Enter pages amount")
# print(title)
# print(author)
# print(year)
# print(rating)
# print(pages)

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. 
# Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here
print("------------------Step 2----------------------")
# title = input("Add book name here: ")
# author = input("Name of the author: ")
# year = int(input("Enter year: "))
# rating = float(input("Enter rating from 1 - 5: "))
# pages = int(input("Enter pages count: "))

### Step 3 - Error handling

## Now take your previous function, and handle potential errors 
# should the user type an answer that doesn't convert data-type properly.

# Code here
print("-------------------Step 3------------------------")
def create_book_list():
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
    
    dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    } 
    return dictionary   

def print_library(list):
    print("\n All listed books \n")
    for book_library in list:
        title = book_library["title"]
        author = book_library["author"]
        year = book_library["year"]
        rating = book_library["rating"]
        pages = book_library["pages"]
        
        print(f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating} Pages: {pages}")

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

print("------------------------Step 4-------------------------")

def main_menu(book_information):
    
    answer = True
    
    user_choices = input("Option 1, Add book: Option 2, View book list: Option 3, Leave page")
    
    if user_choices == "1":
        book_information.append(create_book_list())
    elif user_choices == "2":
        print_library(book_information)
    elif user_choices == "3":
        print("\n Leaving page \n")
        answer = False
    else:
        print("\n Error: Please enter a number \n")

### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive,
# and continually asking for input until the user chooses to exit 
# the program. Call the main menu to ensure it functions properly.

# Code here

print("-----------------------Step 5---------------------")

library = [
    {
        "title": "Fellowship of the ring",
        "author": "J.R.R Tolkien",
        "year": "1954",
        "rating": 4.9,
        "pages": 423        
    },
    {
        "title": "The Two Towers",
        "author": "J.R.R Tolkien",
        "year": "1954", 
        "rating": 4.5,
        "pages": 352        
    },
    {
        "title": "The Return of the King",
        "author": "J.R.R Tolkien",
        "year": "1955",
        "rating": 4.9,
        "pages": 416        
    },
    {
        "title": "The Hobit",
        "author": "J.R.R Tolkien",
        "year": "1937",
        "rating": 4.3,
        "pages": 304,   
    },
    {
        "title": "Green Eggs and Ham?",
        "author": "Dr Seuss",
        "year": "1960",
        "rating": 4.9,
        "pages": 50   
    }
]


def main_menu(book_information):
    
    answer = True
    
    while answer:
        user_choices = input("Option 1, Add book: Option 2, View book list: Option 3: Total books in library, Option 4: Total pages, Option 5, Leave page ")
    
        if user_choices == "1":
            book_information.append(create_book_list())
        elif user_choices == "2":
            print_library(book_information)
        elif user_choices == "3":
            print(f"\n total {len(book_information)} books \n")
        elif user_choices == "4":
            print(f"\n Page totals {sum([i['pages'] for i in book_information])} pages \n")
        elif user_choices == "5":
            print("\n Leaving page")
            answer = False
        else:
            print("\n Error: Please enter a number")
main_menu(library)