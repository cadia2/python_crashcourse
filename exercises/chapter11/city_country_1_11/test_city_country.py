from city_country import city_function

def test_city_country():
    """Do cities such as Santiago Chile work?"""
    formated_pair = city_function('Santiago', 'Chile')
    assert formated_pair == 'Santiago Chile'
