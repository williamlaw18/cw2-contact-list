def format_title(text, capitalised = False):

    if(capitalised):
        return ' '.join(text.split('_')).capitalize()
    return ' '.join(text.split('_'))

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
