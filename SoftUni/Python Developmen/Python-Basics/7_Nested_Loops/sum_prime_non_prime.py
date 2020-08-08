line = input()
sum_prime = 0
sum_non_prime = 0
while line != "stop":
    number = int(line)
    is_prime = True
    if number < 0:
        print('Number is negative.')
        is_negative = True
    else:
        for i in range(2, number):

            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            sum_prime += number
        else:
            sum_non_prime += number
    line = input()

print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_non_prime}')