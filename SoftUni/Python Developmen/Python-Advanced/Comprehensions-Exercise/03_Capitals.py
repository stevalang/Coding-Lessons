countries = input().split(', ')
capitals = input().split(', ')

countries_dict = {country: capital for country, capital in zip(countries, capitals)}
[print(f'{country} -> {capital}') for country, capital in countries_dict.items()]
