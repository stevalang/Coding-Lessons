movie_name = input()

student = 0
standard = 0
kid = 0
tickets_sold = 0
while movie_name != 'Finish':
    total_seats = int(input())
    free_seats = total_seats
    ticket_type = input()
    while free_seats > 0 and ticket_type != 'End':
        tickets_sold += 1
        free_seats -= 1
        if ticket_type == "student":
            student += 1
        elif ticket_type == "standard":
            standard += 1
        else:
            kid += 1
        if free_seats > 0:
            ticket_type = input()
    full_seats_percentage = 100 - (free_seats / total_seats * 100)
    print(f'{movie_name} - {full_seats_percentage:.2f}% full.')
    movie_name = input()
print(f'Total tickets: {tickets_sold}')
print(f'{(student/tickets_sold*100):.2f}% student tickets.')
print(f'{(standard/tickets_sold*100):.2f}% standard tickets.')
print(f'{(kid/tickets_sold*100):.2f}% kids tickets.')


