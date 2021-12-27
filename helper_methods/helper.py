def format_title(text, capitalised = False):
    '''
    This function takes text with underscores and removes them. It accepts a 'capitalised'
    paramaeter as boolean. It is defaulted to false, however if it is true, it returns the
    text capitalised
    
    '''
    if(capitalised):
        return ' '.join(text.split('_')).capitalize()
    return ' '.join(text.split('_'))

def strip_lowercase(text):
    # strips text of white-space before and after, and returns it as lowercase
    return text.strip().lower()

def format_values(text, type):   
# return text formated based on the 'type' parameter. This is ma
    match type:
        case 'postcode':
            return text.upper()
        case 'email':
            return text
        case _:
            return text.title()
