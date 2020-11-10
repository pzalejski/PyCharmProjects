import names
import random

first_name = names.get_first_name()
last_name = names.get_last_name()


def email():
    email_domain = "@testingrandomemail.com"
    number = str(random.randrange(0, 999))
    if len(last_name) > 2:
        username = first_name[0] + last_name[:3] + number
    else:
        username = first_name[0] + last_name + number

    return username + email_domain
