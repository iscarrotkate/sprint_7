import random
import string
import time

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def generate_string_based_on_timestamp():
    return (str(time.time())).replace('.', '')
