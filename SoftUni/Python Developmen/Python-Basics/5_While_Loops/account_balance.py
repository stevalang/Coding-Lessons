deposits_number = int(input())
count = 0

deposits_total = 0


while True:
    deposits = float(input())
    if deposits < 0:
        print("Invalid operation!")
        break
    print(f'Increase: {deposits:.2f}')
    deposits_total += deposits
    count += 1
    if count == deposits_number:
        break


print(f'Total: {deposits_total:.2f}')
