project_type = input()
row_count = int(input())
colon_count = int(input())

ticket_price = 0
if project_type == 'Premiere':
    ticket_price = 12
elif project_type == 'Normal':
    ticket_price = 7.5
elif project_type == 'Discount':
    ticket_price = 5

hall = row_count * colon_count
income = hall * ticket_price

print(f'{income:.2f}')