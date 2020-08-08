start_line = int(input())
end_line = int(input())
magic_number = int(input())
combinations = 0
is_flag = False
for n1 in range(start_line, end_line + 1):
    for n2 in range(start_line, end_line + 1):
        combinations += 1
        current_sum = n1 + n2
        if current_sum == magic_number:
            print(f'Combination N:{combinations} ({n1} + {n2} = {magic_number})')
            is_flag = True
            break

    if is_flag:
        break
if not is_flag:
    print(f'{combinations} combinations - neither equals {magic_number}')