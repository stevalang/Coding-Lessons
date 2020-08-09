divisor = int(input())
bound = int(input())
max_num = 0
for i in range(1, bound+1):
    if i % divisor == 0:
        max_num = i
print(max_num)
