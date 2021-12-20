import json

def format_title(text):
    return ' '.join(text.split('_')).capitalize()

def strip_lowercase(text):
    return text.strip().lower()

def format_values(text, type):
    match type:
        case 'postcode':
            return text.upper()
        case 'email':
            return text
        case _:
            return text.title()

def toJSON(object):
    return json.dumps(object, default=lambda o: o.__dict__, 
        sort_keys=False, indent=4)