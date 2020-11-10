import string
import random
import re


def pw_gen(size=random.randrange(6, 18)):
    chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(random.choice(chars) for _ in range(size))

    return password

