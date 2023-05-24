from random import randint, choice
import string

def generate_car_code():
    number = randint(1000, 9999)
    random_letter = choice(string.ascii_letters).upper()
    car_code = str(number)+random_letter
    return car_code