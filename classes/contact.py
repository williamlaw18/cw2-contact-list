import re 

class main:
    def __init__(self):
        self.contact_details = {
            'name': '',
            'phone': '',
            'address_1': '',
            'address_2': '',
            'postcode': '',
            'email' : '',
        }
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.__email_reg_ex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        #email regular expression from: https://www.regexlib.com/Search.aspx?k=email&AspxAutoDetectCookieSupport=1
        self.__phone_reg_ex = r"^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$"
        #phone regular expression from: https://regexr.com/3c53v
        self.__postcode_reg_ex = r"([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9][A-Za-z]?))))\s?[0-9][A-Za-z]{2})"
        # Postcode reg exhttps://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/488478/Bulk_Data_Transfer_-_additional_validation_valid_from_12_November_2015.pdf
    
# Private Methods

    def __add_contact_field (self, field_type):
        '''
        runs while loop to add field, using sanitise field and check field methods. it only breaks and
        moves to next field when input has been validated.
        To avoid multiple if statements, a parsed and formated version of field_type is stored and then used 
        as a prompt in the input call
        '''

        prompt_title = ' '.join(field_type.split('_')).capitalize()
       

        while True:
            user_input = input('Enter ' + prompt_title + ': ' )
            sanitised_input = self.__sanitise_field(user_input, field_type)
            validated = self.__check_field(sanitised_input, field_type)

            if(validated):
                self.contact_details[field_type] = sanitised_input
                break

        
    def __sanitise_field (self, user_input, field_type):
       '''
       User input here is trimmed of white space before and after, it is also converted to
       lowercase to ease comparison during search
       
       '''
       sanitised_user_input = user_input.strip().lower()

       return sanitised_user_input

    def __check_field (self, user_input, field_type):

        '''
        uses a match/case statement to run user_input against regular expressions to validate
        '''

        match field_type:
            case 'email':
                if(re.fullmatch(self.__email_reg_ex, user_input)):  
                    return True
                else:
                    print(user_input + ' Is not a valid email address')
                    return False
            case 'phone':
                if(re.fullmatch(self.__phone_reg_ex, user_input)):
                    return True
                else:
                    print(user_input + ' Is not a valid phone number ')
                    return False
            case 'postcode':
                if(re.fullmatch(self.__postcode_reg_ex, user_input)):
                    return True
                else:
                    print(user_input + ' Is not a valid postcode')
                    return False
            case _: 
                return True
        pass


       

# Public Methods
    def create_contact(self):
        
        for contact in self.contact_details:
            self.__add_contact_field(contact)

        print(self.contact_details['name'].capitalize() + ' Succesfully Added!') 

    def create_contact_from_json(self, name, phone, address_1, address_2, postcode, email):
        self.contact_details['name'] = name
        self.contact_details['phone']= phone
        self.contact_details['address_1'] = address_1
        self.contact_details['address_2'] = address_2
        self.contact_details['postcode'] = postcode
        self.contact_details['email'] = email
       




     
        




    