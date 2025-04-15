def sandwich_order(*sandwiches):
    '''We will print a desired sandwich order'''
    print("The sandwiches that you have ordered are:")
    for sandwich in sandwiches:
        print(f"\t- {sandwich}")

sandwich_order('ham','cheese')
sandwich_order('bacon','cheese','mushroom')
sandwich_order('ham','cheese','chedar','special')
