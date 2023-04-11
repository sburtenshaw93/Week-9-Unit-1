my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

hunger_games_series = [{
    "title": "Catching Fire",
    "author": "Suzanne Collins",
    "year": 2009,
    "rating": 4.30,
    "pages": 391
},
{
    "title": "Mocking Jay",
    "author": "Suzanne Collins",
    "year": 2010,
    "rating": 4.10,
    "pages": 400
},
{   "title": "The Ballard of Songbirds and Snakes",
    "author": "Suzanne Collins",
    "year": 2020,
    "rating": 4.80,
    "pages": 517}]

# Follow the instructions in this part of the project. Define and flesh out your function below, 
# which should accept a dictionary as an argument when called, and return a string 
# of the info in that book-dictionary in a user-friendly readable format.

# Code below

def readable_format(dictionary):
    hunger_games = f"{my_book['title']}, by {my_book['author']}, made in {my_book['year']}, rating {my_book['rating']}, and number of pages{my_book['pages']}"
    return hunger_games
print(readable_format(my_book))


# Once you are finished with that function, create several more functions which return 
# individual pieces of information from the book.

# Code below

print("-------------Book Information----------------")

def book_sections_one(part_1):
    section_title = part_1["title"]
    return section_title

def book_sections_two(part_2):
    section_author = part_2["author"]
    return section_author

def book_sections_three(part_3):
    section_year = part_3["year"]
    return section_year

def book_sections_four(part_4):
    section_rating = part_4["rating"]
    return section_rating

def book_sections_five(part_5):
    section_pages = part_5["pages"]
    return section_pages

print(book_sections_one(my_book))
print(book_sections_two(my_book))
print(book_sections_three(my_book))
print(book_sections_four(my_book))
print(book_sections_five(my_book))

# Finally, create at least three new functions that might be useful as 
# we expand our home library app. Perhaps thing of a way you could accept
# additional arguments when the function is called? Also, imagine you have 
# a list filled with dictionaries like above.

# Code below
print("-------------Title---------------")
def list_one(book_list_one):
    for book_information in book_list_one:
        print(book_information["title"])
list_one(hunger_games_series)

print("-------------Pages---------------")

def list_two(book_list_two):
    total_pages_list = 0
    for book_information in book_list_two:
        total_pages_list += book_information["pages"]
    return total_pages_list
print(list_two(hunger_games_series))
list_two(hunger_games_series)

print("-------------Rating---------------")

def list_three(book_list_three):
    average_rating = 0
    for book_information in book_list_three:
        average_rating += book_information["rating"] / 3
    return round(average_rating, 2) 
print(list_three(hunger_games_series))
list_three(hunger_games_series)