countries = input().split(", ")
capitals = input().split(", ")

country_with_capital = {countries[i]: capitals[i] for i in range(len(countries))}
# country_with_capital = dict(zip(countries, capitals))

for country, capital in country_with_capital.items():
    print(f"{country} -> {capital}")
