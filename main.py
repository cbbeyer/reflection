#!/usr/bin/env python3
from serialize import to_json


################################################
###   Testing objects

class Date(object):
    '''A date for a person'''
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


class Franchise(object):
    '''A franchise.'''
    def __init__(self, name, owner, started):
        self.name = name
        self.owner = owner
        self.started = started


class Person(object):
    '''A person'''
    def __init__(self, name, gender, birth_date, is_cool, net_worth, debut_year, father, mother, franchise):
        self.name = name
        self.gender = gender
        self.birth_date = birth_date
        self.is_cool = is_cool
        self.net_worth = net_worth
        self.debut_year = debut_year
        self.father = father
        self.mother = mother
        self.franchise = franchise



################################################
###   Main method

if __name__ == '__main__':
    # person 1
    fd1 = Date(1962, 8, 1)
    f1 = Franchise('Spiderman', 'Marvel', fd1)
    b1 = Date(2011, 2, 3)
    p1 = Person('Peter "Spidey" Parker', 'M', b1, False, 15000.00, 1967, None, None, f1)

    # person 2
    fd2 = Date(1962, 8, 1)
    f2 = Franchise('Superman', 'DC\\Comics', fd2)
    b2 = Date(2014, 5, 6)
    p2 = Person('Lois Lane', 'F', b2, True, 40000.50, 1981, None, None, f2)

    # person 3
    fd3 = Date(1963, 1, 1)
    f3 = Franchise('Doctor Who', 'BBC', fd3)
    b3 = Date(2017, 8, 9)
    p3 = Person('River Song/Melody Pond', 'F', b3, True, 91234.56, 2001, p1, p2, f3)

    # print
    print(to_json(p3))
