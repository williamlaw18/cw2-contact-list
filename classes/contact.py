import re 
import constant

class Contact:
    def __init__(self):
        self.__contact_details = {
            'name': None,
            'phone': None,
            'address_1': None,
            'address_2': None,
            'postcode': None,
            'email' : None,
        }

        # initialise group ID to be empty.
        self.__group_id = None
        self.__group_name = None

 
#-------------------------- Private Methods --------------------------------

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
                self.__contact_details[field_type] = sanitised_input
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
                if(re.fullmatch(constant.EMAIL_REG_EX, user_input)):  
                    return True
                else:
                    print(user_input + ' Is not a valid email address')
                    return False
            case 'phone':
                if(re.fullmatch(constant.PHONE_REG_EX, user_input)):
                    return True
                else:
                    print(user_input + ' Is not a valid phone number ')
                    return False
            case 'postcode':
                if(re.fullmatch(constant.POSTCODE_REG_EX, user_input)):
                    return True
                else:
                    print(user_input + ' Is not a valid postcode')
                    return False
            case _: 
                return True
        pass
       

#-------------------------- Public Methods --------------------------------

    def create_contact(self):
        
        for contact in self.__contact_details:
            self.__add_contact_field(contact)

        print(self.__contact_details['name'].capitalize() + ' Succesfully Added!') 

    def create_contact_from_json(self, json_dict):
        #uses a loop to pass params into method based on key strings
        for key in json_dict:
            if key == 'group_id':
                self.__group_id = json_dict[key]
            else:
                self.__contact_details[key] = json_dict[key]

    def edit_contact():
        print('Select the number of the field you want to edit:\n1: Name \n2: Phone \n3: Address Line 1 \n4 Address Line 2 \n5 Postcode \n  ')

    def display_user(self):
        for detail in self.__contact_details:
            detail_title = ' '.join(detail.split('_')).capitalize()
            print(detail_title + ': ' + self.__contact_details[detail])


#-------------------------- Getters and Setters --------------------------------

    def get_group_id(self):
        return self.__group_id

    def get_group_name(self):
        return self.__group_name 

    def get_contact_details(self):
        return self.__contact_details        



     
        




    