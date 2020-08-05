import math
income = float(input())
avg_score = float(input())
min_salary = float(input())


exc_scholarship = avg_score * 25
soc_scholarship = min_salary * 0.35


if avg_score >= 5.50 and income < min_salary:

    if soc_scholarship > exc_scholarship:
        print(f'You get a Social scholarship {math.floor(soc_scholarship)} BGN')

    else:
        print(f'You get a scholarship for excellent results {math.floor(exc_scholarship)} BGN')

elif avg_score >= 5.50:
    print(f'You get a scholarship for excellent results {math.floor(exc_scholarship)} BGN')

elif avg_score > 4.5 and income < min_salary:
    print(f'You get a Social scholarship {math.floor(soc_scholarship)} BGN')

else:
    print('You cannot get a scholarship!')

