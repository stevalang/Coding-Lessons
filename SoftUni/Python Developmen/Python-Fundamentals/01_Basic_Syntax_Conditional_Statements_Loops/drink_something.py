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