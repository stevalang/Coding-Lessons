def perfect_number(number):
    res = 0
    for i in range(1, number):
        if number % i == 0:
            res += i
    if res == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


perfect_number(int(input()))



