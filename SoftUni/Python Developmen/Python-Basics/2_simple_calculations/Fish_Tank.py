# 1. Read input data and convert data types
lenght = int(input())
width = int(input())
height = int(input())
percent_stuff = float(input())

# 2. Calculating aquarium volume
acquarium_volume = lenght * width * height

#3. Convert volume (cm3) -> liters
volume_liters= acquarium_volume * 0.001

#4. Calculating litter taken from stuffs
volume_stuff = (volume_liters*percent_stuff)/100

#5. Calculating volume left
final_volume = volume_liters- volume_stuff

#4. Print and format

print(f'{final_volume:.3f}')




# a = 5
# b = 2
# result = a % b
# print(result)
# print(type(result))