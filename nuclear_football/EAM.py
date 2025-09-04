import random
import string
from datetime import datetime

def generate_authentication_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

def generate_target_package_option():
    return format(random.randint(0, 255), '02x').upper()

def generate_pal():
    return '00000000'

def generate_time_code():
    current_time = datetime.utcnow()
    return current_time.strftime('%H%M%S')

def generate_eam():
    authentication_code = generate_authentication_code()
    target_package_option = generate_target_package_option()
    pal = generate_pal()
    time_code = generate_time_code()

    return f"{authentication_code}-{target_package_option}--{pal}-{time_code}"

eam = generate_eam()
print("Generated EAM:", eam)
