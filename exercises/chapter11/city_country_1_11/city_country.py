#Write a function that accepts two parameters: a city name and a country name. The function should return a single string of the form City, Country, such as Santiago, Chile.

def city_function(city_name,country_name,population=""):
    '''A function which returns a string of city and country'''
    if population:

        return(f'{city_name.title()} {country_name.title()} {population.title()}')
    else:
        return(f'{city_name.title()} {country_name.title()}')


