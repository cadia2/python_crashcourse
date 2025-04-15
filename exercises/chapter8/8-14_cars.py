def car_info(manufacturer,model_name,**cars):
    '''We will store info in a dict about cars'''
    cars['manufacturer'] = manufacturer
    cars['model_name'] = model_name
    return cars

car = car_info('subaru', 'outback', color='blue', tow_package=True)
print(car)




