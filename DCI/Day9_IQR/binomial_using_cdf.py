from binomial_using_pmf import binomial_pmf as binomial

'''
There are 30 cars in a used car lot. At any given time, there's a 60% chance that each car is working as-is. 
What is the probability that the 10 cars the dealer sold today are working?
'''


# n = 10
# k = 10
# p = 0.6
#
# print(p**k)
# print(binomial_pmf(n, k, p))

'''
You go to chipotle every Tuesday, there's 14 workers at chipotle and 7 
of them work on Tuesdays.
Whats the chances you'll see the same worker at the counter 5 out of the 
next 10 times that you go,
if only 3 of them work the counter at any given time?
'''

# n = 10
# k = 5
# p = 3/7
#
# print(binomial_pmf(n, k, p))

'''
In 30 vehicles, it is know that 2 of them will be motorcycles. 
Knowing this, in 40 vehicles, what is the probability of 5 of them will 
be motorcycles?
n = 40
k = 5
p = 2/30
'''


'''
"What is the probability in 12 coin flips of a fair coin,
that you get 7 or fewer heads?"
n = 12
k = 7
p= .5

'''

'''
CDF
Cumulative Density/Distribution Function
- cumulative implies "accumulator"
'''


def binomial_cdf(n, k_high, p=0.5):
    acc = 0.0
    for k in range(0, k_high + 1):
        acc += binomial(n, k, p)
    return acc


# print(binomial_cdf(12, 7, 0.5))


'''
You have 14 


'''
n = 14
p = 0.95
# print(binomial_cdf(n, 12, p) + binomial(n, 13, p) + binomial(n, 14, p))
# print(1-binomial_cdf(n, 11, p))

