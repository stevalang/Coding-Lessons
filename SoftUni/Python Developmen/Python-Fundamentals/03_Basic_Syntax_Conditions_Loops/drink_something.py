'''
Kids drink toddy, Teens drink coke, Young adults drink beer, Adults drink whisky.
Make a program that receives an age, and returns what they drink.
Rules:
Kids under 14 years old.
Teens under 18 years old.
Young adults under 21 years old.
Adults above 21.
Note: All the values except the last one are inclusive!
'''

age = int(input())

# if age < 15:
#     print("drink toddy")
# elif age < 19:
#     print("drink coke")
# elif age < 22:
#     print("drink beer")
# elif age >= 22:
#     print("drink whisky")
drink = ""
if age <= 14:
    drink = "toddy"
elif age <= 18:
    drink = "coke"
elif age <= 21:
    drink = "beer"
else:
    drink = "whisky"

print(f"drink {drink}")
