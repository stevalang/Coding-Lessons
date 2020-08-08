book_name = input()
library_capacity = int(input())
current_book_name = input()
book_counter = 0
is_book_found = False

while True:
    if current_book_name == book_name:
        is_book_found = True
        print(f'You checked {book_counter} books and found it.')
        break
    book_counter += 1
    if book_counter >= library_capacity:
        break

    current_book_name = input()

if not is_book_found:
    print(f'The book you search is not here!\nYou checked {library_capacity} books.')

