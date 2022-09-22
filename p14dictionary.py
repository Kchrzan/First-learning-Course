countries_and_capitals = {"Poland":"Warsaw", "Germany":"Berlin"}
countries_and_capitals['Czechia'] = 'Prague'
# print(countries_and_capitals)

# for country in countries_and_capitals.keys():
    # print(country)


# for country, capital in countries_and_capitals.items():
#     print(country + '-' + capital)

# print(countries_and_capitals["USA"])
# print(countries_and_capitals.setdefault("USA", 'washington DC'))
# print(countries_and_capitals)

# countries_and_capitals.pop("Poland")
# print(countries_and_capitals)

# print(countries_and_capitals.popitem())
# print(countries_and_capitals)

if "Poland" in countries_and_capitals:
    print("Znaleziono!")
else:
    print("Nie znaleziono!")