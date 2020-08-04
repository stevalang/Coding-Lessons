"""
Simple Operations and Calculations - Lab
07. Pet Shop
Check: https://judge.softuni.bg/Contests/Compete/Index/1011#2
Write a program that calculates the costs required to purchase dog food.
The food is bought mainly for dogs, from a pet store, but sometimes their owner also buys for his neighbor's animals.
One package of dog food costs BGN 2.50, and any other that is not for them costs BGN 4.
Login:
2 lines are read from the console:
1. The number of dogs - an integer;
2. The number of other animals - an integer.
Exit:
The following is printed on the console:
"{final amount} lv."
The result must be formatted to the second digit after the decimal point.
"""

#1. Read input data
dogs_count = input()
other_animals_count = input()

#2. Covert data to the correct type
dogs_count = int(dogs_count)
other_animals_count = int(other_animals_count)

#3. Calculate money needed for dog food
dogs_food_cost = dogs_count * 2.5

#4. Calculate money needed for other animals food
other_animals_food_cost = other_animals_count * 4

#5. Calculate total
total_cost = dogs_food_cost + other_animals_food_cost

#6. Print and format
print(f'{total_cost:.2f} lv.')


# dogs = input()
# dogs = int(dogs)
# rest_animals = input()
# rest_animals = float(rest_animals)
# dogs_food = 2.5
# other_food = 4
#
# result = dogs * dogs_food + rest_animals * other_food
#
# print(f"{result} lv.")
