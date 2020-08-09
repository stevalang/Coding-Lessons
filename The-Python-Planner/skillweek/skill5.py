# Dictionaries

pets = {'cat': 'feline', 'dog':'canine'}

pets.keys()
pets.values()

pets['cat']

# Exercise 1

mydict = {1: 1**2, 2: 2**2, 3: 3**2, 4: 4**2, 5: 5**2}
mydict[3]

pets['wolf'] = 'canine'
pets

# Exercise 2 Example

pets['cat'] = ['feline','brown','female']
pets

# Exercise 3 
pets['cat'][0]

# Import

import random

a = [1,2,4,5,6]
random.shuffle(a)
a

from random import shuffle

a = [1,2,4,5,6]
shuffle(a)
a

# Exercise 4

random.randint(1,10)

import os
os.getcwd()

# Exercise 5

a = os.getcwd()
b = a[-5:]
b
