favourite_book = input()

books_checked = 0

current_book = input()

while current_book != "No More Books":
    if current_book == favourite_book:
        print(f"You checked {books_checked} books and found it.")
        break       # no need to read new input lines

    books_checked += 1
    current_book = input()

else:
    print(f"The book you search is not here!")
    print(f"You checked {books_checked} books.")

# Variant 2 with boolean value
# favourite_book = input()
#
# books_checked = 0
#
# current_book = input()
#
# is_found = False
#
# while current_book != "No More Books":
#     if current_book == favourite_book:
#
#         is_found = True
#         break
#
#     books_checked += 1
#     current_book = input()
#
# if is_found:
#     print(f"You checked {books_checked} books and found it.")
# else:
#     print(f"The book you search is not here!")
#     print(f"You checked {books_checked} books.")

# Variant 3
# favourite_book = input()
#
# counter_books = 0
#
# while True:
#     book = input()
#     counter_books = counter_books + 1
#     if book == favourite_book:
#         counter_books = counter_books - 1
#         print(f"You checked {counter_books} books and found it.")
#         break
#     if book == "No More Books":
#         counter_books = counter_books - 1
#         print(f"The book you search is not here!")
#         print(f"You checked {counter_books} books.")
#         break