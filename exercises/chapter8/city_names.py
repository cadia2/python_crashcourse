def city_names(city,country):
    '''We will return a nice string from a city and country name'''
    return (f'"{city.title()}, {country.title()}"')

city_country = city_names("Athens", "Greece")
print(city_country)
city_country = city_names("Moscow", "Russia")
print(city_country)
city_country = city_names("Rome", "Italy")
print(city_country)
