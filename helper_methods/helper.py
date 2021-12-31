import json

def format_title(text, capitalised = False):
    '''
    This function takes text with underscores and removes them. It accepts a 'capitalised'
    paramaeter as boolean. It is defaulted to false, however if it is true, it returns the
    text capitalised.
    
    '''
    if(capitalised):
        return ' '.join(text.split('_')).capitalize()
    return ' '.join(text.split('_'))

def strip_lowercase(text):
    '''Strips text of white-space before and after, and returns it as lowercase.'''
    return text.strip().lower()

def format_values(text, type):   
    ''' Returns text formated based on the 'type' parameter.'''
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