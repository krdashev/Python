import random
import string

def generate_authentication_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

def generate_nuclear_football():
    authentication_code = generate_authentication_code()
    return authentication_code

football = generate_nuclear_football()
print("Generated Nuclear Football Authentication Code:", football)