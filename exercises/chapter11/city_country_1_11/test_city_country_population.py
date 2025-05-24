
from city_country import city_function

def test_city_country():
    """Do cities such as Santiago Chile work?"""
    formated_pair = city_function('Santiago', 'Chile', '5000000')
    assert formated_pair == 'Santiago Chile 5000000'
