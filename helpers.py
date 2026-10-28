import random
import string


def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string


def generate_email():
    return f'test{generate_random_string(5)}@yandex.ru'


def generate_user_data():
    return {
        'email': generate_email(),
        'password': generate_random_string(10),
        'name': f'User{generate_random_string(5)}',
    }
