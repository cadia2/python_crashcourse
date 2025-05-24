from employee import Employee

def test_give_raise_default():
    Bob = Employee('Bob', 'Bigs',15000)
    Bob.give_raise()
    assert Bob.salary == 20000

def test_give_raise_custom():
    Bob = Employee('Bob', 'Bigs',15000)
    Bob.give_raise(10000)
    assert Bob.salary == 25000

