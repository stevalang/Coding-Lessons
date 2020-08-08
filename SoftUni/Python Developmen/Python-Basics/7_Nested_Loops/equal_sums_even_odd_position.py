n1 = int(input())
n2 = int(input())

current_index = 6

for current_number in range(n1, n2 + 1):
    copy_number = current_number
    even_sum = 0
    odd_sum = 0
    while current_number > 0:
        last_digit = current_number % 10

        if current_index % 2 == 0:
            even_sum += last_digit
        else:
            odd_sum += last_digit
        current_number //= 10
        current_index -= 1

    if even_sum == odd_sum:
        print(copy_number, end=' ')

