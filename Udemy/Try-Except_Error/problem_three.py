def ask():
    waiting = True
    while waiting:
        try:
            number = int(input())
        except:
            print("An error occurred! Please try again.")
            continue
        else:
            waiting = False
    print(f"Input an integer: {number}")
    print(f'Thank you, your number squared is: {number ** 2}')


ask()