import re 

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# def is_valid_phone(phone):
#     pattern = r'^\+?1?\s*\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$'
#     return re.match(pattern, phone) is not None

def is_valid_name(name):
    pattern = r"^[a-zA-Z]+(?:[-'\s][a-zA-Z]+)*$"
    return re.match(pattern, name) is not None
