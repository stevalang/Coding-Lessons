import sys
snow_balls = int(input())
final_value = 0
final_snowball = 0
final_time = 0
final_quality = 0
max_value = -sys.maxsize
for i in range(1, snow_balls + 1):
    snow = int(input())
    time = int(input())
    quality = int(input())
    # snowball_value = snow / time ** quality

    def my_pow(x, y):
        return x ** y

    snowball_value = my_pow(snow / time, quality)
    if snowball_value > max_value:
        final_snowball = snow
        final_time = time
        final_quality = quality
        max_value = int(snowball_value)
print(f'{final_snowball} : {final_time} = {max_value} ({final_quality})')