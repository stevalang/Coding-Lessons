num_lines = int(input())

set_even = set()
set_odd = set()


for i in range(num_lines):
    sum_chars = sum(map(ord, input()))
    div = sum_chars // (i + 1)

    if div % 2 == 0:
        set_even.add(div)
    else:
        set_odd.add(div)

sum_even = sum(set_even)
sum_odd = sum(set_odd)


if sum_even == sum_odd:
    list_output = list(map(str, set_even | set_odd))
    print(', '.join(list_output))
elif sum_odd > sum_even:
    list_output = list(map(str, set_odd - set_even))
    print(', '.join(list_output))
else:
    list_output = list(map(str, set_odd ^ set_even))
    print(', '.join(list_output))
