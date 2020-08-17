import random

messages = ['It is certain',
            'It is decidedly so '
            'Yes definitely ',
            'Reply hazy try again ',
            'Ask again later ',
            'Concentrate and ask again '
            'My reply is no '
            'Outlook not so good ',
            'Very doubtful ']

print(messages[random.randint(0, len(messages) - 1)])

first_name = 'STEFAN'
last_name = 'ANGELOV'
for i in first_name:
    for y in last_name:
        print(f'*** {i} ***   *** {y} ***')