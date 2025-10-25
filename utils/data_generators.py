import random
import string

def random_name(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

def random_email():
    return f"{random_name(6)}@example.com"

def user_payload():
    return {
        "name": random_name(),
        "username": random_name(),
        "email": random_email()
    }
