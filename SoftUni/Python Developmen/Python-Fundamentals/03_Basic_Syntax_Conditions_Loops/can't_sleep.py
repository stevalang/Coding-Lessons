'''
If you can't sleep, just count sheep! Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep..." Input will always be valid, i.e. no negative integers.
'''


sheep_count = int(input())

if sheep_count > 0:
    for i in range(1,sheep_count+1):
        print(f'{i} sheep...', end="")
