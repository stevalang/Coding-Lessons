number = float(input())
measurement_in = input()
measurement_out = input()

if measurement_in == 'mm' and measurement_out == "cm":
    number /= 10
elif measurement_in == 'cm' and measurement_out == 'm':
    number /= 100
elif measurement_in == 'mm' and measurement_out == 'm':
    number /= 1000
elif measurement_in == 'cm' and measurement_out == 'mm':
    number *= 10
elif measurement_in == 'm' and measurement_out == 'cm':
    number *= 100
elif measurement_in == 'm' and measurement_out == 'mm':
    number *= 1000

print(f'{number:.3f}')