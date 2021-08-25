import re

def valid_phone_number(phone_number):
    if re.search(r"^(\([0-9]{3}\) ?|[0-9]{3}-)[\s][0-9]{3}-[0-9]{4}$", phone_number):
        return True
    else:
        return False

print(valid_phone_number("(123) 456-7890"))