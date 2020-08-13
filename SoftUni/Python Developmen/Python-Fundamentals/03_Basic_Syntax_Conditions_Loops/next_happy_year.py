'''
You're saying good-bye your best friend, "See you next happy year". Happy Year is the year with only distinct digits, (e.g) 2018. Write a program that receives an integer number and finds the next happy year.
'''

year = input()
year_as_int = int(year) + 1
year = str(year_as_int)

while True:
    symbols_count = len(year)
    unique_count = len(set(year))

    if symbols_count == unique_count:
        break
    else:
        year_as_int += 1
        year = str(year_as_int)
print(year)
