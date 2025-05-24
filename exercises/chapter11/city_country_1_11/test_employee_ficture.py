import pytest
from employee import Employee

@pytest.fixture
def bob():
    bob = Employee('bob', 'bigs',15000)
    return bob

def test_give_raise_default(bob):
    bob.give_raise()
    assert bob.salary == 20000

def test_give_raise_custom(bob):
    bob.give_raise(10000)
    assert bob.salary == 25000

